from aitools.embedding import Embedder
from database import EmbeddingDatabase
from parsedpdf import ParsedPage, ParsedPdf


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
