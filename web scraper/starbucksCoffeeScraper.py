import requests
from bs4 import BeautifulSoup
import os
import re
import time
from selenium import webdriver
#selenium is required to open up a browser and control it. As the websites are dynamic we must open it up in a real browser to allow content manipulation by Js

workingDirectory = os.path.dirname(os.path.realpath(__file__))
baseurl = "https://www.starbucks.com"

myFoldername = "starbucks images"
drinktype = ["iced-coffee",
             "evolution-fresh",
             "refreshers",
             "iced-tea",
             "bottled-drinks",
             "brewed-coffee",
             "espresso",
             "frappuccino-blended-beverages",
             "kids-drinks-and-other"]

try:
    os.makedirs(r"C:\Users\DivakarRajesh\Desktop\Coders\Basic Programming Concepts using C\utility-programs-in-python\web scraper\{}".format(myFoldername))
    print("Main Directory Created")
except FileExistsError:
    print("Main Directory already exists")


for currDrink in drinktype:
    browser = webdriver.Chrome()
    imageURLs = []
    imageFileNames = []
    time.sleep(5)

    browser.get(
        baseurl+"/menu/catalog/product?drink=espresso#view_control=product&drink="+currDrink)
    print("url made=", baseurl +
          "/menu/catalog/product?drink=espresso#view_control=product&drink="+currDrink)

    container = browser.find_element_by_class_name(
        'results').get_attribute("innerHTML")
    container = BeautifulSoup(container, 'html.parser')
    drinks = container.find(class_='category drinks')
    items = drinks.select("ol > li")
    #print("current working directory {}".format(workingDirectory))

    for item in items:
        # returns a list. There is only one image tag -> at position 0
        imagetag = item.select("a > dl > dt > img")[0]
        src = imagetag.get("src")
        imageURLs.append(src)
        name = item.select("a > dl > dd > strong > span")[0].get_text()
        imageFileNames.append(name)
    try:
        os.makedirs(r"C:\Users\DivakarRajesh\Desktop\Coders\Basic Programming Concepts using C\utility-programs-in-python\web scraper\{}\{}".format(myFoldername, currDrink))
        print("Sub-Directory Created")
    except FileExistsError:
        print("Sub-Directory already exists")

    os.chdir(r"{}\{}\{}".format(workingDirectory, myFoldername, currDrink))

    for i in range(len(imageURLs)):
        filename = imageFileNames[i]
        url = imageURLs[i]
        qualifiedURL = '{}{}'.format(baseurl, url)
        qualifiedFilename = workingDirectory+'\\' + \
            myFoldername+'\\'+currDrink+'\\'+filename
        #print("getting {} image from {}".format(qualifiedFilename, qualifiedURL))
        extension = re.search(r'(\.jpg|\.gif|\.png)$', qualifiedURL).group(1)
        with open(qualifiedFilename+extension, 'wb') as f:
            response = requests.get(qualifiedURL)
            f.write(response.content)
    browser.close()
