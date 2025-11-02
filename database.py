from pymongo.mongo_client import MongoClient
from parsedpdf import ParsedPage
import os

class EmbeddingDatabase:
    con_str_template = "mongodb+srv://{}:{}@cluster0.cbscrmv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    def add_page(self, class_name: str, doc_title: str, text: str, page_num: int, embedding: list[float]):
        self.collection.insert_one({
            "document_title": doc_title,
            "class_name": class_name,
            "text": text,
            "page": page_num,
            "embedding": embedding
        })

    def search(self, class_name: str, search_embedding: list[float], num_results: int) -> list[dict]:
        num_candidates = num_results * 20 # The minimum recommended by vector search docs

        with self.collection.aggregate([
            {
                "$vectorSearch": {
                    "exact": False,
                    "index": "vector_index",
                    "path": "embedding",
                    "numCandidates": num_candidates,
                    "limit": num_results,
                    "queryVector": search_embedding,
                    "filter": {
                        "class_name": class_name
                    }
                }
            },
            {
                "$set": {
                    "score": {"$meta": "vectorSearchScore"}
                }
            },
            {
                "$project": {
                    "embedding": 0
                }
            }
        ]) as cursor:
            docs = []
            for doc in cursor:
                docs.append(doc)
        
        return docs

    def remove_by_field(self, field: str, value: str):
        self.collection.delete_many({
            field: value
        })

    def get_class_names(self):
        return self.collection.distinct("class_name")

    def get_doc_titles_for_class(self, class_name: str) -> list[str]:
        return self.collection.distinct("document_title", {
            "class_name": class_name
        })
    
    def rename_class(self, old_name: str, new_name: str) -> int:
        update_result = self.collection.update_many(
        {
            "class_name": old_name
        },
        {
            "$set": {
                "class_name": new_name
            }
        })

        return update_result.modified_count

    def __enter__(self):
        self.user = os.environ["MONGODB_USER"]
        self.password = os.environ["MONGODB_PASSWORD"]

        self.client = MongoClient(
            EmbeddingDatabase.con_str_template.format(self.user, self.password)
        )

        database = self.client["StudyAIDatabase"]
        self.collection = database["Pages"]

        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.client.close()
