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

if not found: print("You might have entered a wrong name. Try Again!")
else: print(imgFile.size)
width, height = input("Enter the resolution to resize: ").lower().strip().split("x")
finalName = input("Enter the new name to save the image: ")
extension = input("Enter the File Format in which you would like to save the image: ")
finalImage = imgFile.resize((int(width),int(height)),Image.ANTIALIAS)
finalImage.save(finalName+'.'+extension)
