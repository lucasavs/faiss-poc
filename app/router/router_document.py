from fastapi import APIRouter
from pydantic import BaseModel
from ..controller import controller_document

router = APIRouter()


class Document_base(BaseModel):
    knowledge_base: str
    payload: str


class Document_delete(BaseModel):
    knowledge_base: str
    id: str


class Document_create(Document_base):
    pass


@router.post("/document/", tags=["document"])
async def add_document(document_create: Document_create):
    controller_document.add_document(
        document_create.knowledge_base, document_create.payload
    )


@router.delete("/document/", tags=["document"])
async def delete_document(document_delete: Document_delete):
    return controller_document.delete_document(
        document_delete.knowledge_base, document_delete.id
    )
