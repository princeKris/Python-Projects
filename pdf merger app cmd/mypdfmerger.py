from PyPDF2 import PdfFileMerger
import os
os.chdir("C:\\Users\\kris\\Desktop\\New folder\\pdf")
pdfs=os.listdir('.')
print(pdfs)
merger=PdfFileMerger()
for pdf in pdfs:
	merger.append(pdf)
merger.write("result.pdf")
merger.close()
