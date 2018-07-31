import requests
from bs4 import BeautifulSoup

response = requests.get('http://codedemos.com/sampleblog/')

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.body)