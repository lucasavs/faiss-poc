from fastapi import FastAPI
from .router import router_knowledge_base, router_document

app = FastAPI()

app.include_router(router_knowledge_base.router)
app.include_router(router_document.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
