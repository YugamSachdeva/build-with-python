from pypdf import PdfWriter

merger = PdfWriter()
pdfs=["pdf1.pdf","pdf2.pdf","pdf3.pdf"]
for pdf in pdfs:
    merger.append(pdf)

merger.write("out-basic.pdf")
merger.close()