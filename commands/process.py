from argparse import _SubParsersAction, ArgumentParser, Namespace
from parsedpdf import ParsedPdf
from .command import Command
from .tools import get_embeddings, save_processed_pages

class ProcessCommand(Command):
    def __init__(self):
        super().__init__("process")
    
    def setup_parser(self, sub_parser: _SubParsersAction[ArgumentParser]):
        process_parser = sub_parser.add_parser(self.get_name())
        process_parser.add_argument("doc_path")
        process_parser.add_argument("class_name")
        process_parser.add_argument("doc_title")

    def execute(self, args: Namespace):
        doc_path, class_name, doc_title = (args.doc_path, args.class_name, args.doc_title)

        print("Parsing pdf...")
        parsed_pdf = ParsedPdf(doc_title, doc_path) 

        print("Generating page embeddings...")
        embeddings = get_embeddings(parsed_pdf)

        print("Saving pages...")
        save_processed_pages(class_name, doc_title, parsed_pdf.pages, embeddings)

        print("Done!")  