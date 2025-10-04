import sys
from parsedpdf import ParsedPdf, ParsedPage
from dotenv import load_dotenv
from embedder import Embedder
from database import EmbeddingDatabase

def get_embeddings(parsed_pdf: ParsedPdf) -> list[float]:
    embeddings = []
    with Embedder() as embedder:
        for page in parsed_pdf.pages:
            embeddings.append(embedder.gen_embedding(str(page)))
    
    return embeddings

def save_processed_pages(doc_title: str, pages: list[ParsedPage], embeddings: list[float]):
    if (len(pages) != len(embeddings)):
        raise IndexError("Length of pages and embeddings must be equal")

    with EmbeddingDatabase() as database:
        for i in range(len(pages)):
            database.add_page(doc_title, str(pages[i]), pages[i].page_num, embeddings[i]) 


def process(doc_path: str, doc_title: str):
    print("Parsing pdf...")
    parsed_pdf = ParsedPdf(doc_title, doc_path) 

    print("Generating page embeddings...")
    embeddings = get_embeddings(parsed_pdf)

    print("Saving pages...")
    save_processed_pages(doc_title, parsed_pdf.pages, embeddings)

    print("Done!")

def search(query: str):
    print("Converting query to embedding...")
    with Embedder() as embedder:
        embedding = embedder.gen_embedding(query)
    
    print("Performing search...")
    with EmbeddingDatabase() as database:
        results = database.search(embedding, 5)
    
    for result in results:
        print("\n")
        print(result)
        print("\n")

    
def remove(field: str, value: str):
    with EmbeddingDatabase() as database:
        database.removeByField(field, value)

if __name__ == "__main__":
    if (len(sys.argv) < 2 
        or (
            not (sys.argv[1] == "process" and len(sys.argv) == 4) 
            and not (sys.argv[1] == "search" and len(sys.argv) == 3))
            and not (sys.argv[1] == "remove" and len(sys.argv) == 4)
        ):
            print(f"Usage: python {sys.argv[0]} process [pdf file name] [doc title]")
            print(f"Usage: python {sys.argv[0]} search [query]")
            print(f"Usage: python {sys.argv[0]} remove [field] [value]")
            sys.exit(1)
    
    load_dotenv()

    command = sys.argv[1]    
    if command == "process":
        process(sys.argv[2], sys.argv[3])
    elif command == "search":
        search(sys.argv[2])
    elif command == "remove":
        remove(sys.argv[2], sys.argv[3])