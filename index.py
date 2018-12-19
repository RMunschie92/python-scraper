# # import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

quote_page = "https://en.wikipedia.org/wiki/Ada_Lovelace"

# # query the website and return the html to the variable page
page = urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

name = soup.find(attrs={'id': 'firstHeading'})
name = name.text.strip()
print(name)
