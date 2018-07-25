import re
consumerEmailProviders = ['gmail','ymail','yahoo','orkut','hotmail','aol','orange','live','rediffmail','outlook','googlemail','rockermail']
def checkemail(str):
	pattern = r"([\w\.\d-]+)@([\w\.=]+)(\.[\w\.]+)"
	match = re.match(pattern,str)
	return match
def checkIfConsumerEmail(str):
	startFrom = str.find('@')
	endAt = str.rfind('.')
	serviceProvider = str[startFrom+1:endAt]
	if serviceProvider in consumerEmailProviders:
		return True
	else:
		return False
	

str = input()
match = checkemail(str)
if match:
	print("Entered email is Valid")
	match = checkIfConsumerEmail(str)
	if match:
		print("Entered email is a consumer email")
	else:
		print("Entered email is not a consumer email")
else:
	print("Entered email is not valid")


	

	
