from argparse import _SubParsersAction, ArgumentParser, Namespace
from parsedpdf import ParsedPdf
from .command import Command
from .tools import get_embeddings, save_processed_pages

class ProcessCommand(Command):
    def __init__(self):
        super().__init__("process")
    
    def setup_parser(self, sub_parser: _SubParsersAction[ArgumentParser]):
        process_parser = sub_parser.add_parser(self.get_name(),
            description="Prepares and processes the given document's text for searching."
        )
        process_parser.add_argument("doc_path",
            help="path to the document to add"
        )
        process_parser.add_argument("class_name",
            help="the class to add the document to"
        )
        process_parser.add_argument("doc_title",
            help="the name the document will be referred to"                            
        )

    def execute(self, args: Namespace):
        doc_path, class_name, doc_title = (args.doc_path, args.class_name, args.doc_title)

        print("Parsing pdf...")
        parsed_pdf = ParsedPdf(doc_title, doc_path) 

        print("Generating page embeddings...")
        embeddings = get_embeddings(parsed_pdf)

        print("Saving pages...")
        save_processed_pages(class_name, doc_title, parsed_pdf.pages, embeddings)

        print("Done!")  