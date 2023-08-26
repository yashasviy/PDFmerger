import PyPDF2

files = []
x = int(input("enter no. of pdfs"))
for i in range(x):
    y = input("enter pdf file name")
    files.append(y)

merger = PyPDF2.PdfMerger()

for filename in files:
    pdf = open(filename, 'rb')
    pdfreader = PyPDF2.PdfReader(pdf)
    merger.append(pdfreader)
pdf.close()
y=input("enter the you want for your merged pdf")
y=y+".pdf"
merger.writ e(y)