from abc import ABC, abstractmethod
from typing import List, Optional
from app.models.markdown_file import MarkdownFile

class BaseRepository(ABC):

    @abstractmethod
    def get_by_id(self, file_id: str) -> Optional[MarkdownFile]:
        pass

    @abstractmethod
    def list_files(self, tags: Optional[List[str]] = None) -> List[MarkdownFile]:
        pass

    @abstractmethod
    def get_version(self, file_id: str, version: int) -> Optional[MarkdownFile]:
        pass
