
# Proxy API to Serve Markdown Files with FastAPI

This repository provides a minimal FastAPI backend that serves a collection of markdown files, including features like filtering by tags and versioning. The backend is designed using the **Repository Pattern** to allow flexibility in the source of markdown files. Initially, markdown files are read from the file system, but the system can be extended to support other data sources like PostgreSQL.

## Features

- **Modular Design**: Uses the Repository Pattern to allow swapping the file system with a database later (e.g., PostgreSQL).
- **Serve Markdown Files**: Exposes markdown files and their metadata via a FastAPI-based API.
- **Versioning**: Supports fetching specific versions of markdown files.
- **Tag-Based Filtering**: Allows filtering markdown files based on tags provided in the file's metadata.

## Project Structure

The project is structured as follows:

```
markdown_service/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints.py     # API endpoints for interacting with markdown files
│   ├── core/
│   │   ├── config.py            # Configuration files
│   ├── models/
│   │   ├── markdown_file.py     # Pydantic model for markdown files
│   ├── repositories/
│   │   ├── base.py              # Base repository class (Repository Pattern)
│   │   ├── file_repository.py   # File-based repository implementation
│   ├── services/
│   │   ├── markdown_service.py  # Business logic for handling markdown files
│   └── main.py                  # FastAPI entry point
└── tests/                       # (Optional) Test cases
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- [Poetry](https://python-poetry.org/) for dependency management

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/fastapi-markdown-service.git
   cd fastapi-markdown-service
   ```

2. **Install dependencies** using Poetry:
   ```bash
   poetry install
   ```

3. **Create a directory** to store markdown files:
   ```bash
   mkdir -p path/to/markdown/files/
   ```

4. **Add some example markdown files** to the directory with YAML frontmatter. Here's an example markdown file:

   ```markdown
   ---
   id: "example-file"
   title: "Example Markdown File"
   tags: ["example", "markdown"]
   version: 1
   created_at: "2024-09-05"
   updated_at: "2024-09-05"
   ---
   
   # Example Markdown Content

   This is an example markdown file served by FastAPI.
   ```

### Running the Application

1. **Start the FastAPI server**:
   ```bash
   poetry run uvicorn app.main:app --reload
   ```

2. The API will now be available at `http://127.0.0.1:8000`.

### API Endpoints

- **List all markdown files**:
  ```http
  GET /api/v1/markdowns/
  ```

- **Get a specific markdown file by ID**:
  ```http
  GET /api/v1/markdowns/{file_id}
  ```

- **Get a specific version of a markdown file**:
  ```http
  GET /api/v1/markdowns/{file_id}/versions/{version}
  ```

- **Filter markdown files by tags**:
  ```http
  GET /api/v1/markdowns/?tags=example,markdown
  ```

### Example Markdown Directory Structure

You can organize markdown files in your file system like this:

```
path/to/markdown/files/
├── example-file.md
├── guide.md
└── tutorial.md
```

Each markdown file should include a YAML frontmatter that defines the file's metadata, such as `id`, `title`, `tags`, and `version`.

### Markdown File Example

Here is an example of what a markdown file with frontmatter looks like:

```markdown
---
id: "my-guide"
title: "My Guide to FastAPI"
tags: ["guide", "fastapi"]
version: 1
created_at: "2024-09-05"
updated_at: "2024-09-05"
---

# My Guide to FastAPI

This guide explains how to create a FastAPI application...
```

### Extending the Project

- **PostgreSQL Support**: To extend this project to work with PostgreSQL, implement a new `PostgresRepository` that inherits from `BaseRepository` and queries the database.
  
- **Testing**: Add unit tests in the `tests/` directory, especially focusing on the service and repository layers. You can mock the file system repository for testing.