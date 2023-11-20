from fastapi import APIRouter
from pydantic import BaseModel
from ..controller import controller_knowledge_base

router = APIRouter()


class Knowledge_base(BaseModel):
    name: str


@router.get("/knowledge_base/", tags=["knowledge_base"])
async def get_all_knowledge_bases():
    return controller_knowledge_base.get_databases()


@router.post("/knowledge_base/", tags=["knowledge_base"])
async def create_knowledge_base(knowledge_base: Knowledge_base):
    return controller_knowledge_base.create_database(knowledge_base.name)


@router.delete("/knowledge_base/", tags=["knowledge_base"])
async def delete_knowledge_base(knowledge_base: Knowledge_base):
    return controller_knowledge_base.delete_database(knowledge_base.name)


@router.get(
    "/knowledge_base/compare/{knowledge_base}", tags=["knowledge_baseknowledge_base"]
)
async def query_similar_documents(knowledge_base: str, query):
    result = controller_knowledge_base.similarity_search(knowledge_base, query)
    return result
