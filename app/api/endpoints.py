from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
from app.services.markdown_service import MarkdownService
from app.models.markdown_file import MarkdownFile
from app.repositories.file_repository import FileRepository

router = APIRouter()

# Dependency injection: for now, we use FileRepository, but it can be swapped later
def get_service() -> MarkdownService:
    repository = FileRepository(base_dir="docs")
    print("Creating service with repository", repository)
    return MarkdownService(repository)

@router.get("/markdowns/{file_id}", response_model=MarkdownFile)
def get_markdown(file_id: str, service: MarkdownService = Depends(get_service)):
    file = service.get_markdown(file_id)
    if not file:
        raise HTTPException(status_code=404, detail="Markdown file not found")
    return file

@router.get("/markdowns/", response_model=List[MarkdownFile])
def list_markdown_files(tags: Optional[List[str]] = None, service: MarkdownService = Depends(get_service)):
    return service.list_markdown_files(tags)

@router.get("/markdowns/{file_id}/versions/{version}", response_model=MarkdownFile)
def get_markdown_version(file_id: str, version: int, service: MarkdownService = Depends(get_service)):
    file = service.get_markdown_version(file_id, version)
    if not file:
        raise HTTPException(status_code=404, detail="Markdown file version not found")
    return file
