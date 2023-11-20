from ..databases_holder import database_container
from fastapi import HTTPException


def get_databases():
    parsed_databases = {}
    for key, value in database_container.items():
        if value is None:
            parsed_databases[key] = None
        else:
            parsed_databases[key] = value.docstore._dict
    return parsed_databases


def create_database(name: str):
    if name in database_container:
        raise HTTPException(status_code=409, detail="database is already created")
    else:
        database_container[name] = None  # starts with an empty database


def delete_database(name: str):
    if name not in database_container:
        raise HTTPException(status_code=404, detail="database is not created")
    else:
        del database_container[name]


def similarity_search(name: str, query: str):
    if name not in database_container:
        raise HTTPException(status_code=404, detail="database is not created")
    db = database_container[name]
    parsed_results = []
    results_with_scores = db.similarity_search_with_score(query)

    for doc, score in results_with_scores:
        parsed_result = {
            "content": doc.page_content,
            "score": str(
                score
            ),  # we need to convert score to a foramt that fastAPI can parse
        }
        parsed_results.append(parsed_result)
    return parsed_results
