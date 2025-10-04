import pypdf

class ParsedPage:
    def __init__(self, doc_title: str, page_num: int, text: str):
        self.doc_title = doc_title
        self.page_num = page_num
        self.text = text

    def __str__(self) -> str:
        return f'{{"page_number": {self.page_num}, "document_title": {self.doc_title}, "text": "{self.text}"}}'

class ParsedPdf:
    def __init__(self, doc_title: str, pdf_path: str):
        self.pages = []
        self.title = doc_title
        
        reader = pypdf.PdfReader(pdf_path)
        for i, page in enumerate(reader.pages):
            self.pages.append(ParsedPage(self.title, i+1, page.extract_text()))

    def get_page(self, page_num: int) -> str:
        return self.pages[page_num]

    def get_num_pages(self) -> int:
        return len(self.pages)

    def __str__(self) -> str:
        out = ['[']
        
        for i, page in enumerate(self.pages):
            out.append(f'\n')
            if i > 0:
                out.append(',')

            out.append(str(page))
        
        out.append(']')
        return ''.join(out)