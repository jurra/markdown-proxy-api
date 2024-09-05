from typing import List, Optional
from pydantic import BaseModel

class MarkdownFile(BaseModel):
    id: str
    title: str
    content: str
    tags: List[str]
    version: int
    created_at: str
    updated_at: Optional[str]
