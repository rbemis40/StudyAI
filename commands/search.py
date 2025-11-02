from aitools.embedding import Embedder
from database import EmbeddingDatabase
from parsedpdf import ParsedPage
from .command import Command
from aitools.generators import StreamedResponseGenerator


class SearchCommand(Command):
    def __init__(self):
        super().__init__("search", ["class name", "query"])
    
    def execute(self, args: list[str]):
        class_name, query = args
        print("Converting query to embedding...")
        with Embedder() as embedder:
            embedding = embedder.gen_embedding(query)
        
        print("Performing search...")
        with EmbeddingDatabase() as database:
            results = database.search(class_name, embedding, 5)
        
        relevant_pages = []
        for result in results:
            relevant_pages.append(ParsedPage(result['document_title'], result['page'], result['text']))

        print("Generating response...")
        with StreamedResponseGenerator() as resp_gen:
            response = resp_gen.get_response(query, relevant_pages, model="gpt-4")
            for text in response:
                print(text, end="", flush=True) 
            
            print("")