from aitools.generators.respgen import ResponseGenerator, ResponseIterable
from parsedpdf import ParsedPage


class StreamedResponseGenerator(ResponseGenerator):
    def __init__(self):
        super().__init__()

    def get_response(self, query: str, pages: list[ParsedPage], model="gpt-4") -> StreamedResponseIterable:
        prompt = self._prepare_prompt(pages)

        stream = self.client.responses.create(
            model= model,
            instructions= prompt,
            input= query,
            stream= True,
        )

        return StreamedResponseIterable(stream)

class StreamedResponseIterable(ResponseIterable):
    def __init__(self, stream):
        super().__init__()
        self.stream = stream

    def __next__(self) -> str:
        event = next(self.stream) 
        match event.type:
            case "response.output_text.delta":
                return event.delta
            case "response.completed":
                raise StopIteration
            case "error":
                raise RuntimeError(event.message)
            case _:
                return "" # Keep generating