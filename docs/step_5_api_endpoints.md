---
id: "step5_api_endpoints"
title: "Step 5: API Endpoints"
tags: ["fastapi", "api", "endpoints"]
version: 1
created_at: "2024-09-05"
updated_at: "2024-09-06"
---

# Step 5: API Endpoints

In this step, we define the API endpoints that will expose our markdown files. Using FastAPI, we create three main routes:

1. `GET /markdowns/{file_id}`: Fetches a markdown file by its ID.
2. `GET /markdowns/`: Lists all markdown files, optionally filtered by tags.
3. `GET /markdowns/{file_id}/versions/{version}`: Fetches a specific version of a markdown file.

These endpoints use the `MarkdownService` to retrieve data from the repository and return it to the user in a structured format.
