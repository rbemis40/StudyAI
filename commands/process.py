from parsedpdf import ParsedPdf
from .command import Command
from .tools import get_embeddings, save_processed_pages

class ProcessCommand(Command):
    def __init__(self):
        super().__init__("process", ["pdf file path", "class name", "doc_title"])
    
    def execute(self, args: list[str]):
        doc_path, class_name, doc_title = args

        print("Parsing pdf...")
        parsed_pdf = ParsedPdf(doc_title, doc_path) 

        print("Generating page embeddings...")
        embeddings = get_embeddings(parsed_pdf)

        print("Saving pages...")
        save_processed_pages(class_name, doc_title, parsed_pdf.pages, embeddings)

        print("Done!")  