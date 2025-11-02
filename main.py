import sys
from parsedpdf import ParsedPdf, ParsedPage
from dotenv import load_dotenv
from aitools.embedding import Embedder
from aitools.generators import StreamedResponseGenerator, FullResponseGenerator
from database import EmbeddingDatabase
from command import Command

def get_embeddings(parsed_pdf: ParsedPdf) -> list[float]:
    embeddings = []
    with Embedder() as embedder:
        for page in parsed_pdf.pages:
            embeddings.append(embedder.gen_embedding(str(page)))
    
    return embeddings

def save_processed_pages(class_name: str, doc_title: str, pages: list[ParsedPage], embeddings: list[float]):
    if (len(pages) != len(embeddings)):
        raise IndexError("Length of pages and embeddings must be equal")

    with EmbeddingDatabase() as database:
        for i in range(len(pages)):
            database.add_page(class_name, doc_title, str(pages[i]), pages[i].page_num, embeddings[i]) 

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
            #print("\n")
            #print(result)
            #print("\n")

        print("Generating response...")
        with FullResponseGenerator() as resp_gen:
            response = resp_gen.get_response(query, relevant_pages, model="gpt-4")
            for text in response:
                print(text, end="", flush=True) 
            
            print("")

class RemoveCommand(Command):
    def __init__(self):
        super().__init__("remove", ["field", "value"])
    
    def execute(self, args: list[str]):
        field, value = args
        with EmbeddingDatabase() as database:
            database.remove_by_field(field, value)

class ListCommand(Command):
    def __init__(self):
        super().__init__('list', ['class name'])
    
    def execute(self, args: list[str]):
        class_name, = args

        print("Getting unique titles...")
        with EmbeddingDatabase() as database:
            titles = database.get_doc_titles_for_class(class_name)

        print("\n")
        for title in titles:
            print(title)

        print("\nDone!")

def print_usage(prog_name: str, commands: list[Command]):
    for command in commands:
        print(command.get_usage(prog_name))

if __name__ == "__main__":
    commands = [
        ProcessCommand(),
        SearchCommand(),
        RemoveCommand(),
        ListCommand()
    ]

    if len(sys.argv) < 2:
        print_usage(sys.argv[0], commands)
        sys.exit(-1)
    
    load_dotenv()

    given_command = sys.argv[1]   
    for command in commands:
        if command.is_valid(given_command, len(sys.argv) - 2):
            command.execute(sys.argv[2:])
            break
    else:
        print_usage(sys.argv[0], commands)
        sys.exit(-1)
