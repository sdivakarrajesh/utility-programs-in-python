from tkinter import *
from TkinterDnD2 import *
from tkinter.filedialog import askopenfilename

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

        self.quit = Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")
        self.file_list = []

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

root = TkinterDnD.Tk()
app = Application(master=root)
app.master.title("My PDF joiner")
app.master.geometry("250x250")



app.mainloop()
