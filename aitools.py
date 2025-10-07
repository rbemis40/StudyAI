import openai
from parsedpdf import ParsedPage

class Embedder:
    model_small = 'text-embedding-3-small'
    model_large = 'text-embedding-3-large'

    def __enter__(self):
        self.client = openai.Client()
        return self

    def gen_embedding(self, text: str) -> list[float]:
        response = self.client.embeddings.create(
            input= text,
            model= Embedder.model_large
        )

        # TODO: Error handling        
        return response.data[0].embedding

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.client.close()


class ResponseGenerator:
    def generate(self, query: str, pages: list[ParsedPage], model="gpt-5"):
        prompt = load_prompt("prompt.txt")
        references = []
        for page in pages:
            references.append({
                "title": page.doc_title,
                "page_number": page.page_num,
                "text": page.text
            })    

        complete_prompt = prompt.format(str(references))

        response = self.client.responses.create(
            model=model,
            instructions=complete_prompt,
            input=query
        )

        return response.output_text

    def __enter__(self):
        self.client = openai.Client()

        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.client.close()

def load_prompt(filename: str) -> str:
    prompt = None
    with open(filename) as file:
        prompt = file.read()
    
    return prompt