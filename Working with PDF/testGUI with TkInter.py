from tkinter import *
from TkinterDnD2 import *
from tkinter.filedialog import askopenfilename
import PyPDF2
class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.create_drop_files_here()

    def create_drop_files_here(self):
        self.entry_sv = StringVar()
        self.entry_sv.set('Drop Files Here...')
        self.entry = Entry(root, textvar=self.entry_sv, width=80)
        self.entry.pack(side="bottom", padx=10, pady=10)
        self.entry.drop_target_register(DND_FILES)
        self.entry.dnd_bind('<<Drop>>', self.drop)

    def create_widgets(self):
        self.hi_there = Button(self)
        self.hi_there["text"] = "Choose a File"
        self.hi_there["command"] = self.add_fileChooser
        self.hi_there.pack(side="top")
        self.file_list = []
        self.joinFiles = Button(self, text="Join",
                              command=self.joinPDFs)
        self.joinFiles.pack(side="bottom")


    def add_fileChooser(self):
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        print(filename)
        self.file_list.append(filename)
        onlyName = filename.split("/")[-1]
        self.label = Label(text=onlyName, fg="black")
        self.label.pack(side="bottom")
        self.remove = Button(self, text="remove", fg="red", command=self.remove_file)
        self.remove.pack(side="left")

    def remove_file(self):
        print("test")

    def drop(self,event):
        #self.entry_sv.set(list(event.data))
        print(type(event))
        #print(str(event.data).replace("}","").replace("{",""))
        print(event.data)

    def joinPDFs(self):
        count = len(self.file_list)
        pdfWriter = PyPDF2.PdfFileWriter()
        finalName = self.getProperFileName("Enter Final PDF Name:")
        pdfOutputFile = open(finalName,'wb')
        for i in self.file_list:
        	name = i
        	pdfFile = open(name,'rb')
        	pdfReader = PyPDF2.PdfFileReader(pdfFile)
        	for pageNum in range(pdfReader.numPages):
        		pageObj = pdfReader.getPage(pageNum)
        		pdfWriter.addPage(pageObj)
        	pdfOutputFile = open(finalName,'ab')
        	pdfWriter.write(pdfOutputFile)
        	pdfFile.close()
        pdfOutputFile.close()

    def getProperFileName(self,strToPrint):
    	name = ''
    	while True:
    		name = input(strToPrint)
    		if len(name)>4:
    			if name[-1:-4:-1]!='.pdf':
    				name = name + '.pdf'
    		else:
    			name = name + '.pdf'
    		print(name)
    		nonAcceptedFileNameChar = ['/','\\',';','*','?','\"','<','>','|']
    		if any(letter in nonAcceptedFileNameChar for letter in name):
    			print("File Name cannot contain /\\;*?\"<>|.. Retry ")
    			continue
    		else:
    			break
    	return name
root = TkinterDnD.Tk()
app = Application(master=root)
app.master.title("My PDF joiner")
app.master.geometry("250x250")
app.mainloop()
