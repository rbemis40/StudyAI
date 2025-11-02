from typing import Union
from parsedpdf import ParsedPage
import openai

class ResponseGenerator:
    def get_response(self, query: str, pages: list[ParsedPage], model="gpt-5") -> ResponseIterable:
        raise NotImplementedError

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

class ResponseIterable:
    def __iter__(self):
        return self

    def __next__(self) -> str:
        raise NotImplementedError