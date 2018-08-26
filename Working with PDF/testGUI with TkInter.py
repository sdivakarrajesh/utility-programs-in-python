from tkinter import *
from TkinterDnD2 import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
import PyPDF2
from tkinter import messagebox
class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.create_widgets()
        self.create_drop_files_here()
        self.create_list_box()

    def create_list_box(self):
        self.lb = Listbox(width = 35)
        self.removeBtn = Button(text=" Remove ",command=self.remove_file())
        self.removeBtn.grid(row=1,column=1,pady=5,padx=5,sticky=N)
        self.moveUpBtn = Button(text=" Move Up ",command = self.move_up())
        self.moveUpBtn.grid(row=1,column=1,pady=5,padx=5,sticky=S)
        self.count = 1
        self.lb.grid(row=1)

    def move_up(self):
        print('test')

    def create_drop_files_here(self):
        self.entry_sv = StringVar()
        self.entry_sv.set('Drop Files Here...')
        self.entry = Entry(root, textvar=self.entry_sv, width=35)
        self.entry.grid(row=98, padx=5, pady=5)
        self.entry.drop_target_register(DND_FILES)
        self.entry.dnd_bind('<<Drop>>', self.drop)

    def create_widgets(self):
        self.file_chooser = Button(self)
        self.file_chooser["text"] = " Choose a File "
        self.file_chooser["command"] = self.add_fileChooser
        label = Label(self,text="Choose PDFs to join: ",fg="black")
        label.grid(row=0,column=0,padx=5,pady=5)
        self.file_chooser.grid(row=0,column=1,pady=5)
        self.file_list = []
        self.joinFiles = Button(text="     Join     ",command=self.joinPDFs)
        self.joinFiles.grid(row=99,column=1)

    def add_fileChooser(self):
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        print(filename)
        if filename!="" and filename!=None:
            self.file_list.append(filename)
            onlyName = filename.split("/")[-1]
            self.count = self.count+1
            self.lb.insert(self.count,onlyName)

    def remove_file(self):
        print("test")

    def drop(self,event):
        self.returnedFilePaths = event.data
        self.filePaths()

    def filePaths(self):
        curr = self.returnedFilePaths[1:-1]
        list = curr.split("} {")
        self.file_list = self.file_list+list
        print(list)
        for i in list:
            onlyName = i.split("/")[-1]
            self.count = self.count+1
            self.lb.insert(self.count,onlyName)

    def joinPDFs(self):
        try:
            count = len(self.file_list)
            pdfWriter = PyPDF2.PdfFileWriter()
            #finalName = self.getProperFileName("Enter Final PDF Name:")
            finalName = asksaveasfilename(defaultextension=".pdf", filetypes=(("PDF", "*.pdf"),("All Files", "*.*") ))
            pdfOutputFile = open(finalName,'wb')
            for i in self.file_list:
                name = i
                pdfFile = open(name,'rb')
                print("Joining "+i)
                pdfReader = PyPDF2.PdfFileReader(pdfFile, strict=False)
                for pageNum in range(pdfReader.numPages):
            	    pageObj = pdfReader.getPage(pageNum)
            	    pdfWriter.addPage(pageObj)
                pdfOutputFile = open(finalName,'ab')
                pdfWriter.write(pdfOutputFile)
                pdfFile.close()
            pdfOutputFile.close()
        except Exception as e:
            print(e)
            #pass
        messagebox.showinfo("My PDF Joiner", "        Done!        ")

root = TkinterDnD.Tk()
app = Application(master=root)
app.master.title("My PDF joiner")
app.master.geometry("300x300")
app.mainloop()
