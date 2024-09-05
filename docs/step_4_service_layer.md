---
id: "step4_service_layer"
title: "Step 4: Service Layer"
tags: ["service", "business-logic", "backend"]
version: 1
created_at: "2024-09-04"
updated_at: "2024-09-05"
---

# Step 4: Service Layer

The service layer acts as an intermediary between the API and the repository. In this step, we implement a `MarkdownService` class that interacts with the `FileRepository` to fetch markdown files and their metadata.

The service layer handles business logic such as filtering files by tags, retrieving specific versions of files, and more. By keeping the logic in the service layer, we keep our API endpoints clean and focused solely on request handling.
