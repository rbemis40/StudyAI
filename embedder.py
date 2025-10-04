import openai
from parsedpdf import ParsedPage

class PageEmbedder:
    model_small = 'text-embedding-3-small'
    model_large = 'text-embedding-3-large'

    def __enter__(self):
        self.client = openai.Client()
        return self

    def gen_embedding(self, page: ParsedPage) -> list[float]:
        response = self.client.embeddings.create(
            input= str(page),
            model= PageEmbedder.model_large
        )

        # TODO: Error handling        
        return response.data[0].embedding

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.client.close()
