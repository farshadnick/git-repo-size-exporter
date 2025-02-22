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
