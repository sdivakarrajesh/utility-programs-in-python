from PIL import Image
from tkinter import *
from TkinterDnD2 import *
from tkinter import ttk

class Application(Frame):
	def __init__(self,master=None):
		super().__init__(master)
		self.option = IntVar()
		self.create_widgets()
		self.create_list_box()

	def create_widgets(self):
		option1 = Radiobutton(text="PreDefined Resolutions",variable=self.option,value=1,command=self.perspective)
		option1.select()
		self.option.set(1)
		option2 = Radiobutton(text="Custom Resolutions", variable=self.option, value=2,command=self.perspective)
		option1.grid(row=0,column=0,padx=10, pady=5,sticky=W)
		option2.grid(row=2,column=0,padx=10, pady=5,sticky=W)
		self.box = ttk.Combobox(root)
		self.box['values'] = ("320x240","640X480","600x600","800x600","1024x768","1280x800","1280x960","1680x1050","1600x1200")
		self.box.current(0)
		self.box.bind("<<ComboboxSelected>>", self.handle_drop_down_selection)
		self.box.grid(row=1,column=0)
		self.resizeBtn = Button(text="Resize",command=self.resizeImages).grid(row=99,column=99,padx=5,pady=5,ipadx=5,ipady=2)
	def handle_drop_down_selection(self,event):
		print(self.box.get())
	def resizeImages(self):
		print('test')
	def perspective(self):
		if self.option.get() == 1:
			print('option1')
			self.box['state'] = NORMAL
		elif self.option.get() == 2:
			self.box['state'] = DISABLED
			print('option2')
	def create_list_box(self):
		self.lb = Listbox(width = 35)
		self.lb.drop_target_register(DND_FILES)
		self.lb.dnd_bind('<<Drop>>', self.drop)
		self.lb.grid(row=3,padx=10,pady=10,rowspan=1)
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
app.master.geometry("320x320")
root.resizable(False,False)
app.mainloop()

def getProperFileName(strToPrint):
	name = ''
	while True:
		name = input(strToPrint)
		nonAcceptedFileNameChar = ['/','\\',';','*','?','\"','<','>','|']
		if any(letter in nonAcceptedFileNameChar for letter in name):
			print("File Name cannot contain /\\;*?\"<>|.. Retry ")
			continue
		else:
			break
	return name

def addExtension(name,extension):
	if len(name)<5:
		name = name + '.'+extension
	if len(name)>4:
	    if name[-1:-4:-1]!='.'+extension:
		    name = name + '.'+extension
	print(name)
	return name
def resizeImage(imgFile):
	while True:
		try:
			width, height = input("Enter the resolution to resize: ").lower().strip().split("x")
		except:
			print("Invalid resolution.. try Example: 100X200")
		else:
			break
	finalName = input("Enter the new name to save the image: ")
	extension = input("Enter the File Format in which you would like to save the image: ")
	finalImage = imgFile.resize((int(width),int(height)),Image.ANTIALIAS)
	finalImage.save(finalName+'.'+extension)

def rotateImage(imgFile):
	degree = int(input("How much degree to rotate? "))
	finalName = input("Enter the new name to save the image: ")
	extension = input("Enter the File Format in which you would like to save the image: ")
	imgFile.rotate(degree).save(finalName+'.'+extension)

extensions = ['png','jpg','gif']
name = getProperFileName('Enter the name of the image file: ')
found = False
while True and len(extensions)>0:
    nameWithExtension = addExtension(name,extensions[0])
    try: imgFile = Image.open(nameWithExtension)
    except FileNotFoundError: extensions.pop(0)
    except: pass
    else:
        found = True
        break
#todo terminate program
if not found: print("You might have entered a wrong name. Try Again!")
else: print(imgFile.size)
while True:
	try:
		option = int(input("Enter the Action number: \n1.Resize\n2.Rotate"))
	except:
		print("Enter a valid option number")
	else:
		break
if option == 1:
	resizeImage(imgFile)
elif option == 2:
	rotateImage(imgFile)
