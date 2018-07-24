import re
str = input()
pattern = r"([\w\.\d-]+)@([\w\.=]+)(\.[\w\.]+)"
match = re.match(pattern,str)
if match:
	print("Entered email is Valid")
else:
	print("Entered email is not valid")