from argparse import _SubParsersAction, ArgumentParser, Namespace
from aitools.embedding import Embedder
from database import EmbeddingDatabase
from parsedpdf import ParsedPage
from .command import Command
from aitools.generators import StreamedResponseGenerator


class SearchCommand(Command):
    def __init__(self):
        super().__init__("search")

    def setup_parser(self, sub_parser: _SubParsersAction[ArgumentParser]):
        search_parser = sub_parser.add_parser(self.get_name(),
            description="Search a class using plain text and ask questions about the material."
        )
        search_parser.add_argument("class_name",
            help="the class to search in"
        )
        search_parser.add_argument("query",
            help="what to search for or questions to answer"
        )

    def execute(self, args: Namespace):
        class_name, query = (args.class_name, args.query)
        
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