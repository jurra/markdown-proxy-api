---
id: "step2_markdown_model"
title: "Step 2: Markdown File Model"
tags: ["pydantic", "models", "fastapi"]
version: 1
created_at: "2024-09-02"
updated_at: "2024-09-03"
---

# Step 2: Markdown File Model

In this step, we define a Pydantic model called `MarkdownFile` to represent the markdown files. This model will hold the file metadata, such as:

- `id`: A unique identifier for the file.
- `title`: The title of the markdown document.
- `content`: The actual markdown content of the file.
- `tags`: A list of tags associated with the file (for collections).
- `version`: The version of the file.
- `created_at`: The timestamp when the file was created.
- `updated_at`: The timestamp when the file was last updated (optional).

By defining this model, we can ensure that the data conforms to a specific structure when serving markdown files via the FastAPI backend.
