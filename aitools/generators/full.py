from aitools.generators.respgen import ResponseGenerator, ResponseIterable
from parsedpdf import ParsedPage


class FullResponseGenerator(ResponseGenerator):
    def __init__(self):
        super().__init__()

    
    def get_response(self, query: str, pages: list[ParsedPage], model="gpt-5") -> FullResponseIterable:
        prompt = self._prepare_prompt(pages) 

        response = self.client.responses.create(
            model= model,
            instructions= prompt,
            input= query
        )

        return FullResponseIterable(response)

class FullResponseIterable(ResponseIterable):
    def __init__(self, response):
        super().__init__()
        self.response = response

    def __next__(self):
        if self.response is None:
            raise StopIteration
        
        text = self.response.output_text
        self.response = None
        
        return text