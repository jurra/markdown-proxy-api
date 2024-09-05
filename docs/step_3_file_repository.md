---
id: "step3_file_repository"
title: "Step 3: File Repository"
tags: ["repository", "file-system", "backend"]
version: 1
created_at: "2024-09-03"
updated_at: "2024-09-04"
---

# Step 3: File Repository

In this step, we implement the `FileRepository` class, which extends the `BaseRepository`. This repository will read markdown files from the file system and return metadata and content.

Each markdown file will have a YAML frontmatter that contains metadata such as `id`, `title`, `tags`, and `version`. We use Python's `yaml` package to parse the frontmatter and extract the metadata. The rest of the file will be treated as the markdown content.

By implementing the file repository, we can now fetch markdown files from the file system and serve them through our FastAPI backend.
