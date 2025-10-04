from pymongo.mongo_client import MongoClient
from parsedpdf import ParsedPage
import os

class EmbeddingDatabase:
    con_str_template = "mongodb+srv://{}:{}@cluster0.cbscrmv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    def add_page(self, doc_title: str, text: str, embedding: list[float]):
        self.collection.insert_one({
            "title": doc_title,
            "text": text,
            "embedding": embedding
        })

    def __enter__(self):
        self.user = os.environ['MONGODB_USER']
        self.password = os.environ['MONGODB_PASSWORD']

        self.client = MongoClient(
            EmbeddingDatabase.con_str_template.format(self.user, self.password)
        )

        database = self.client['StudyAIDatabase']
        self.collection = database['Pages']

        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.client.close()