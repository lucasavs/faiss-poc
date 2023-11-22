# FAISS + Hugging Face + FastAPI

This application creates a vector store database in memory using FAISS and allows you to embed documents with the all-MiniLM-L12-v2 Hugging Face model. This way, you can add vetorize documents in the database, delete them, and search for similar results documents. All this using FastAPI as a framework to generate the external APIs, so you can use a browser to manipulate all this data.

## How to use

To use this application, you need to run `make run` or if you want to run a container with this, please run `make build` and `make run`

Then you can access localhost:8000/docs, where you will find a Swagger with all the APIs

### Endpoints
#### GET /knowledge_base/
Used for reading all the knowledge bases. You can read also the id of the documents here

#### POST /knowledge_base/
You can create knowledge bases with this endpoint. You just need to pass a valid username as a parameter.
```
{
  "name": "string"
}
```
#### DELETE /knowledge_base/
Similar to the creation one, you need to pass the knowledge_base name as a parameter to delete the desired knowledge_base
```
{
  "name": "string"
}
```
#### GET /knowledge_base/compare/{knowledge_base}?query={query}
You can retrieve similar documents to a query inside a specific knowledge base. It will return the documents in order, where closer to zero means the documents are more similar

#### POST /document/
You create a document and add it to one desired knowledge base. 
``` 
{
  "knowledge_base": "string",
  "payload": "string"
}
```

#### DELETE /document/
You can delete documents from knowledge bases. You need to look for the correct document id inside the knowledge base. To find the document id for a specific document, use the `GET /knowledge_base/` endpoint

```
{
  "knowledge_base": "string",
  "id": "string"
}
```
## Notes

* You can easily change the tools that we use in this application, but since we are using an in-memory database all the endpoints are synchronous. If you desire to make requests to external APIs or databases you gonna need to change the endpoints and other parts of the code to make async calls, or you may have problems with the latency of the application. FastAPI can handle async pretty well, so you don't need to worry about that
* For now, we only have some unit tests, but we can expand our test horizon. FastAPI has a TestCliente that allows you to test your application without creating HTTP connections. Be aware that if you write tests and take into consideration the results of the model (score, which results come first, etc) you may have broken tests if you change the model or the API.
* Please note, that new databases are created null while empty databases that are empty due to deletion of documents will show as an empty object. This is by design to help debug the application, but going to a production environment you may want to return empty objects to newly created databases as well.
