from typing import List, Optional
from app.repositories.base import BaseRepository
from app.models.markdown_file import MarkdownFile

class MarkdownService:
    def __init__(self, repository: BaseRepository):
        self.repository = repository

    def get_markdown(self, file_id: str) -> Optional[MarkdownFile]:
        return self.repository.get_by_id(file_id)

    def list_markdown_files(self, tags: Optional[List[str]] = None) -> List[MarkdownFile]:
        return self.repository.list_files(tags)

    def get_markdown_version(self, file_id: str, version: int) -> Optional[MarkdownFile]:
        return self.repository.get_version(file_id, version)
