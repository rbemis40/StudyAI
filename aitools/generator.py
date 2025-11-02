from typing import Union
from parsedpdf import ParsedPage
import openai

class ResponseGenerator:

    def __init__(self):
        self.stream = None

    def generate(self, query: str, pages: list[ParsedPage], model="gpt-5") -> str:
        prompt = self._prepare_prompt(pages) 

        response = self.client.responses.create(
            model= model,
            instructions= prompt,
            input= query
        )

        return response.output_text
    def stream_begin_gen(self, query: str, pages: list[ParsedPage], model="gpt-5") -> None:
        prompt = self._prepare_prompt(pages)

        self.stream = self.client.responses.create(
            model= model,
            instructions= prompt,
            input= query,
            stream= True,
        )


    def stream_get_next(self) -> Union[str, None]:
        if self.stream is None:
            return None

        event = next(self.stream) 
        match event.type:
            case "response.output_text.delta":
                return event.delta
            case "response.completed":
                self.stream = None
                return None
            case "error":
                raise RuntimeError(event.message)
            case _:
                return "" # Keep generating

    def _prepare_prompt(self, pages: list[ParsedPage], filename="prompt.txt") -> str:
        prompt = None
        with open(filename) as file:
            prompt = file.read()

        references = []
        for page in pages:
            references.append({
            "title": page.doc_title,
            "page_number": page.page_num,
            "text": page.text
            })    

        complete_prompt = prompt.format(str(references))

        return complete_prompt 
    
    def __enter__(self):
        self.client = openai.Client()

        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.client.close()