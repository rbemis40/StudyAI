import sys
import parsedpdf

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print(f'Usage: python {sys.argv[0]} [pdf file name]')
        sys.exit(1)
    
    parsed_pdf = parsedpdf.ParsedPdf(sys.argv[1])
    print(parsed_pdf)