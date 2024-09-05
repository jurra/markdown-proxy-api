---
id: "step1_repository_pattern"
title: "Step 1: Repository Pattern"
tags: ["repository", "design-pattern", "backend"]
version: 1
created_at: "2024-09-01"
updated_at: "2024-09-02"
---

# Step 1: Repository Pattern

The first step in designing the FastAPI backend is to implement the **Repository Pattern**. This pattern provides an abstraction over data access, making it easy to swap out the data source (e.g., from file system to PostgreSQL) without changing the business logic.

We define an abstract base class `BaseRepository` with methods like `get_by_id()`, `list_files()`, and `get_version()`. Other repositories (such as `FileRepository`) will inherit from this base class.

By using the repository pattern, we achieve separation of concerns and make the codebase modular and maintainable.
