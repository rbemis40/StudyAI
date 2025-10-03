import pypdf

class ParsedPage:
    def __init__(self, page_num: int, text: str):
        self.page_num = page_num
        self.text = text

    def __str__(self) -> str:
        return f'{{"real_page_number": {self.page_num}, "text": "{self.text}"}}'

class ParsedPdf:
    def __init__(self, pdf_path: str):
        self.pages = []
        
        reader = pypdf.PdfReader(pdf_path)
        for i, page in enumerate(reader.pages):
            self.pages.append(ParsedPage(i, page.extract_text()))

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