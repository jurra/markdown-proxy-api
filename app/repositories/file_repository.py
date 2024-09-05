import os
from typing import List, Optional
from app.models.markdown_file import MarkdownFile
from app.repositories.base import BaseRepository
import markdown
import yaml

class FileRepository(BaseRepository):

    def __init__(self, base_dir: str):
        self.base_dir = base_dir

    def get_by_id(self, file_id: str) -> Optional[MarkdownFile]:
        file_path = os.path.join(self.base_dir, f"{file_id}.md")
        if not os.path.exists(file_path):
            return None

        with open(file_path, 'r') as file:
            content = file.read()
            return self._parse_markdown(content)

    def list_files(self, tags: Optional[List[str]] = None) -> List[MarkdownFile]:
        files = []
        for filename in os.listdir(self.base_dir):
            if filename.endswith(".md"):
                file_path = os.path.join(self.base_dir, filename)
                with open(file_path, 'r') as file:
                    content = file.read()
                    md_file = self._parse_markdown(content)
                    if tags is None or set(tags).issubset(md_file.tags):
                        files.append(md_file)
        return files

    def get_version(self, file_id: str, version: int) -> Optional[MarkdownFile]:
        # Simple versioning by adding version to filename e.g., "file_v1.md"
        file_path = os.path.join(self.base_dir, f"{file_id}_v{version}.md")
        if not os.path.exists(file_path):
            return None

        with open(file_path, 'r') as file:
            content = file.read()
            return self._parse_markdown(content)

    def _parse_markdown(self, content: str) -> MarkdownFile:
        # Assume the markdown files contain YAML frontmatter with metadata
        metadata, md_content = content.split('---\n', 2)[1:]
        meta_data = yaml.safe_load(metadata)

        return MarkdownFile(
            id=meta_data['id'],
            title=meta_data['title'],
            content=md_content,
            tags=meta_data['tags'],
            version=meta_data['version'],
            created_at=meta_data['created_at'],
            updated_at=meta_data.get('updated_at')
        )
