import PIL.Image
from tkinter import *
from TkinterDnD2 import *
from tkinter import ttk

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.option = IntVar()
        self.create_widgets()
        self.create_list_box()
        self.file_list = []
        self.count = 0
        self.res_option = "320x200"

    def create_widgets(self):
        option1 = Radiobutton(text="PreDefined Resolutions",variable=self.option,value=1,command=self.perspective)
        option1.select()
        self.option.set(1)
        option2 = Radiobutton(text="Custom Resolutions", variable=self.option, value=2,command=self.perspective)
        self.frame = Frame(root)
        self.width_label = Label(self.frame,text="width")
        self.width_label.grid(row=0,column=0)
        self.height_label = Label(self.frame,text="height")
        self.height_label.grid(row=0,column=2)
        self.custom_res_entry_width =  Entry(self.frame,width=10)
        self.custom_res_entry_width.grid(row=0,column=1)
        self.custom_res_entry_height = Entry(self.frame,width=10)
        self.custom_res_entry_height.grid(row=0,column=3)
        option1.grid(row=0,column=0,padx=10, pady=5,sticky=W)
        option2.grid(row=2,column=0,padx=10, pady=5,sticky=W)
        self.box = ttk.Combobox(root)
        self.box['values'] = ("320x240","640X480","600x600","800x600","1024x768","1280x800","1280x960","1680x1050","1600x1200")
        self.box.current(0)
        self.box.bind("<<ComboboxSelected>>", self.handle_drop_down_selection)
        self.box.grid(row=1,column=0)
        self.frame.grid(row=3, column=0,sticky=W,padx=10, pady=5)
        self.resizeBtn = Button(text="Resize",command=self.resizeImages).grid(row=99,column=0,padx=10,pady=5,ipadx=10,ipady=2,sticky=E)
        self.perspective()
    def handle_drop_down_selection(self,event):
        self.res_option = self.box.get()
    def resizeImages(self):
        if self.option.get() == 1:
            self.res_option = self.box.get()
        elif self.option.get() == 2:
            self.res_option = str(self.custom_res_entry_width.get())+ "x" + str(self.custom_res_entry_height.get())
            print(self.res_option)
        for i in self.file_list:
            fp = open(i, "rb")
            imgFile = PIL.Image.open(fp)
            aspect_ratio = imgFile.size[0]/imgFile.size[1]
            print(aspect_ratio)
            extension = "jpg"
            width,height = self.res_option.split('x')
            height = int(width) / float(aspect_ratio)
            finalImage = imgFile.resize((int(width), int(height)), PIL.Image.ANTIALIAS)
            finalName = i
            fileName, temp = finalName.rsplit(".", maxsplit=1)
            res = str(int(width)) + "x" + str(int(height))
            finalName = finalName + res
            finalImage.save(finalName+"."+extension)

    def perspective(self):
        if self.option.get() == 1:
            print('option1')
            self.box['state'] = NORMAL
            for child in self.frame.winfo_children():
                child.configure(state="disabled")

        elif self.option.get() == 2:
            self.box['state'] = DISABLED
            for child in self.frame.winfo_children():
                child.configure(state="normal")

            print('option2')
    def create_list_box(self):
        self.lb = Listbox(width = 35)
        self.lb.drop_target_register(DND_FILES)
        self.lb.dnd_bind('<<Drop>>', self.drop)
        self.lb.grid(row=4,padx=10,pady=10,rowspan=1)
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
root = TkinterDnD.Tk()
app = Application(master=root)
app.master.title("Image Resizer")
app.master.geometry("250x375")
root.resizable(False,False)
app.mainloop()