import requests
import logging
import threading
import time
import os
from flask import Flask, Response

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# GitLab API Settings from environment variables
GITLAB_URL = os.getenv("GITLAB_URL", "https://gitlab.huemer-it.com")  # Default URL if not set
ACCESS_TOKEN = os.getenv("GITLAB_ACCESS_TOKEN", "XXXXXXX")  # Default token if not set

if not ACCESS_TOKEN:
    logging.error("GitLab Access Token is not set in the environment variables.")
    exit(1)

headers = {"PRIVATE-TOKEN": ACCESS_TOKEN}
params = {"statistics": "true", "per_page": 100, "page": 1}

# Flask App for Prometheus Metrics
app = Flask(__name__)

# Store project sizes globally
project_sizes = []

def fetch_projects():
    """Fetch all GitLab projects with their sizes."""
    global project_sizes
    logging.info("Fetching project list from GitLab...")

    projects = []
    params["page"] = 1  # Reset pagination

    while True:
        logging.debug(f"Requesting page {params['page']}...")
        response = requests.get(f"{GITLAB_URL}/api/v4/projects", headers=headers, params=params)

        if response.status_code != 200:
            logging.error(f"Failed to fetch data: {response.status_code} - {response.text}")
            break

        data = response.json()
        if not data:
            logging.info("No more projects found.")
            break

        projects.extend(data)
        params["page"] += 1

    logging.info(f"Total projects fetched: {len(projects)}")

    # Convert size to MB and sort from largest to smallest
    project_sizes = sorted(
        [
            {
                "name": project["name"],
                "size_mb": round(project.get('statistics', {}).get('storage_size', 0) / (1024 * 1024), 2)
            }
            for project in projects
        ],
        key=lambda p: p["size_mb"],
        reverse=True
    )

def periodic_fetch():
    """Runs the fetch_projects function every 10 minutes in a background thread."""
    while True:
        fetch_projects()
        logging.info("Sleeping for 10 minutes before next fetch...")
        time.sleep(600)  # 10 minutes

# Start background thread
threading.Thread(target=periodic_fetch, daemon=True).start()

@app.route('/metrics')
def prometheus_metrics():
    """Expose project sizes in Prometheus format."""
    metrics = [
        f'gitlab_project_size_mb{{project="{project["name"]}"}} {project["size_mb"]}'
        for project in project_sizes
    ]
    return Response("\n".join(metrics), mimetype="text/plain")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9400)
