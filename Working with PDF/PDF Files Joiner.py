import PyPDF2
count = int(input('Enter Number of PDFs to join:'))
pdfWriter = PyPDF2.PdfFileWriter()
finalName = input("Enter Final PDF Name:")
for i in range(count):
	name = input("Enter File name:")
	pdfFile1 = open(name,'rb')
	pdfReader1 = PyPDF2.PdfFileReader(pdfFile1)
	
	for pageNum in range(pdfReader1.numPages):
		pageObj = pdfReader1.getPage(pageNum)
		pdfWriter.addPage(pageObj)

	pdfOutputFile = open(finalName,'ab')
	pdfWriter.write(pdfOutputFile)
	pdfFile1.close()

