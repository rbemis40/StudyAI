import sys
from parsedpdf import ParsedPdf, ParsedPage
from dotenv import load_dotenv
from embedder import PageEmbedder
from database import EmbeddingDatabase

def get_embeddings(parsed_pdf: ParsedPdf) -> list[float]:
    embeddings = []
    with PageEmbedder() as embedder:
        for page in parsed_pdf.pages:
            embeddings.append(embedder.gen_embedding(page))
    
    return embeddings

def save_processed_pages(doc_title: str, pages: list[ParsedPage], embeddings: list[float]):
    if (len(pages) != len(embeddings)):
        raise IndexError("Length of pages and embeddings must be equal")

    with EmbeddingDatabase() as database:
        for i in range(len(pages)):
            database.add_page(doc_title, str(pages[i]), embeddings[i]) 


if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print(f"Usage: python {sys.argv[0]} [pdf file name] [doc title]")
        sys.exit(1)
    
    load_dotenv()

    doc_path = sys.argv[1]
    doc_title = sys.argv[2]

    print("Parsing pdf...")
    parsed_pdf = ParsedPdf(doc_path) 

    print("Generating page embeddings...")
    embeddings = get_embeddings(parsed_pdf)

    print("Saving pages...")
    save_processed_pages(doc_title, parsed_pdf.pages, embeddings)

    print("Done!")
