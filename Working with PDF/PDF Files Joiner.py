import PyPDF2
def nameFormat(name):
	if len(name)>4:
		if name[-1:-4:-1]!='.pdf':
			name = name + '.pdf'
	print(name)
	return name

count = int(input('Enter Number of PDFs to join:'))
pdfWriter = PyPDF2.PdfFileWriter()
finalName = input("Enter Final PDF Name:")
finalName = nameFormat(finalName)
pdfOutputFile = open(finalName,'wb')
for i in range(count):
	name = input("Enter File name:")
	name = nameFormat(name)
	pdfFile = open(name,'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFile)

	for pageNum in range(pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)

	pdfOutputFile = open(finalName,'ab')
	pdfWriter.write(pdfOutputFile)
	pdfFile.close()
pdfOutputFile.close()
