# git-repo-size-exporter
GitLab Repository Size Exporter

A Python-based exporter for GitLab that exposes repository sizes via a custom metrics endpoint for monitoring and analysis. This tool helps you track and monitor repository sizes across your GitLab instance, making it easier to optimize and manage your repositories.


Features:

    Exposes repository sizes as custom metrics via a Prometheus-compatible endpoint.
    Provides insights into repository growth and storage usage.
    Can be integrated with Prometheus for visualization and alerting.

    Setup
Step 1: Create a GitLab Access Token

To interact with the GitLab API, create an access token with the following permissions:

    API
    Read Repositories
    Read Users
    Admin Mode

Step 2: Run the Exporter

Once your access token is ready, you can run the exporter using Docker. Here's how to start it:

```
docker run -it -p 9400:9400 -e GITLAB_ACCESS_TOKEN="XXX" -e GITLAB_URL=https://gitlab.example.com farshadnikfetrat/gitrepo-size-exporter:latest
```

Replace XXX with your GitLab access token. The exporter will be available on http://localhost:9400 for Prometheus scraping.

Step 3: Verify It
Result:

After running the container and accessing the metrics endpoint, the logs should appear as follows:
2025-02-22 09:13:21,929 - INFO - [Port: 9400] - Fetching project list from GitLab...
2025-02-22 09:13:21,929 - INFO - [Port: 9400] - Starting Flask app on port 9400...
 * Tip: There are .env or .flaskenv files present. Do "pip install python-dotenv" to use them.
 * Serving Flask app 'main'
 * Debug mode: off
2025-02-22 09:13:21,931 - INFO - [Port: 9400] - WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:9400
 * Running on http://172.17.0.2:9400
2025-02-22 09:13:21,931 - INFO - [Port: 9400] - Press CTRL+C to quit
2025-02-22 09:13:31,177 - INFO - [Port: 9400] - No more projects found.
2025-02-22 09:13:31,177 - INFO - [Port: 9400] - Total projects fetched: **402**
2025-02-22 09:13:31,180 - INFO - [Port: 9400] - Sleeping for 10 minutes before next fetch...
