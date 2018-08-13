import tkinter as tk
from tkinter.filedialog import askopenfilename

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Choose a File"
        self.hi_there["command"] = self.add_fileChooser
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")
        self.file_list = []
    def add_fileChooser(self):
        tk.Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        print(filename)
        self.file_list.append(filename)
        onlyName = filename.split("/")[-1]
        self.label = tk.Label(text=onlyName, fg="black")
        self.label.pack(side="bottom")
        self.remove = tk.Button(self, text="remove", fg="red", command=self.remove_file)
        self.remove.pack(side="left")
    def remove_file(self):
        print("test")

root = tk.Tk()
app = Application(master=root)
app.master.title("My PDF joiner")
app.master.geometry("250x250")
app.mainloop()
