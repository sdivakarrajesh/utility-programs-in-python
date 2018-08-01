import requests
from bs4 import BeautifulSoup

response = requests.get('http://codedemos.com/sampleblog/')

soup = BeautifulSoup(response.text, 'html.parser')
#printing the body
print(soup.body)

#printing the head
print(soup.head)

#printing the title tag within the head
print(soup.head.title)

#finding a div -> return just the first div
print(soup.find('div'))

#finding all the divs -> returns a list of divs
#findAll or find_all
print(soup.find_all('div'))
#use index if particular element is to be returned

#finding by id name
print(soup.find(id='section-1'))

#finding by class name -> class is a reserved keyword so -> use class_
print(soup.find(class_='items'))


#finding by attributes
print(soup.find(attrs={'data-hello':'hi'}))


#using CSS selectors

#finding by id
print(soup.select('#section-1'))

#finding by class name
print(soup.select('.item'))


#getting only the text without tag name
print(soup.find(class_='item')).get_text()


#iterating over a list of items
for i in soup.select('.item'):
    print(i.get_text())

#getting the contents -> can also use indexes to get particular elements
print(soup.body.contents)

#find_next_sibling, find_previous_sibling, find_parent methods can be used to navigate around
#passing in the type of the element in the method as argument returns the particular element
