from PIL import Image

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
