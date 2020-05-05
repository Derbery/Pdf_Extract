import PyPDF2 as pyPdf

file = "c:\\Users\\Derby\\Desktop\\pdf_extract\\Data Structures and Algorithms Using Python.pdf"
pdf = pyPdf.PdfFileReader(open(file,"rb"))
for page in pdf.pages:
    print(page.extractText())

