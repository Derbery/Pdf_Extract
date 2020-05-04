import PyPDF2


def main():
    pdfFile = "Data Structures and Algorithms Using Python.pdf"

    pdfRead = PyPDF2.PdfFileReader(pdfFile)
    page = pdfRead.getPage(0)
    pageContent = page.extractText()

    print(pageContent)



if __name__ == "__main__":
    main()

