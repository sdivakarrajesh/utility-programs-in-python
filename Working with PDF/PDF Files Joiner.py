import PyPDF2
def getProperFileName(strToPrint):
	name = ''
	while True:
		name = input(strToPrint)
		if len(name)>4:
			if name[-1:-4:-1]!='.pdf':
				name = name + '.pdf'
		print(name)
		nonAcceptedFileNameChar = ['/','\\',';','*','?','\"','<','>','|']
		if any(letter in nonAcceptedFileNameChar for letter in name):
			print("File Name cannot contain /\\;*?\"<>|")
			continue
		else:
			break
	return name

count = int(input('Enter Number of PDFs to join:'))
pdfWriter = PyPDF2.PdfFileWriter()
finalName = getProperFileName("Enter Final PDF Name:")
pdfOutputFile = open(finalName,'wb')
for i in range(count):
	name = getProperFileName("Enter File name:")
	pdfFile = open(name,'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFile)
	for pageNum in range(pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)
	pdfOutputFile = open(finalName,'ab')
	pdfWriter.write(pdfOutputFile)
	pdfFile.close()

pdfOutputFile.close()
