import requests
from bs4 import BeautifulSoup
import os
import re

workingDirectory = os.path.dirname(os.path.realpath(__file__))
baseurl = "https://www.starbucks.com"
imageURLs = []
imageFileNames = []
myFoldername = "starbucks images"

response = requests.get(
    baseurl+"/menu/catalog/product?drink=espresso#view_control=product")
soup = BeautifulSoup(response.text,'html.parser')
#print(soup.body)
container = soup.find(class_='results')
drinks = container.find(class_='category drinks')
items = drinks.select("ol > li")
print("current working directory {}".format(workingDirectory))

for item in items:
    imagetag = item.select("a > dl > dt > img")[0] #returns a list. There is only one image tag -> at position 0
    src = imagetag.get("src")
    imageURLs.append(src)
    name = item.select("a > dl > dd > strong > span")[0].get_text()
    imageFileNames.append(name)
try:
    os.makedirs(r"C:\Users\DivakarRajesh\Desktop\Coders\Basic Programming Concepts using C\utility-programs-in-python\web scraper\{}".format(myFoldername))
    print("Directory Created")
except FileExistsError:
    print("Directory already exists")

os.chdir(r"{}\{}".format(workingDirectory,myFoldername))

for i in range(len(imageURLs)):
    filename = imageFileNames[i] 
    url = imageURLs[i]
    qualifiedURL = '{}{}'.format(baseurl, url)
    qualifiedFilename = workingDirectory+'\\'+myFoldername+'\\'+filename
    print("getting {} image from {}".format(qualifiedFilename, qualifiedURL))
    extension = re.search(r'(\.jpg|\.gif|\.png)$', qualifiedURL).group(1)
    with open(qualifiedFilename+extension, 'wb') as f:
        response = requests.get(qualifiedURL)
        f.write(response.content)


