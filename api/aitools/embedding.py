import openai

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