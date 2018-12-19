# # import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

foreclosures_page = "https://sso.eservices.jud.ct.gov/Foreclosures/Public/PendPostbyTownList.aspx"
base_url = "https://sso.eservices.jud.ct.gov/Foreclosures/Public/"

# # query the website and return the html to the variable page
page = urlopen(foreclosures_page)

soup = BeautifulSoup(page, 'html.parser')

towns = soup.find(attrs={'id': 'ctl00_cphBody_Panel1'})

town_links = []

# Loop through list of towns and get all hrefs
for link in towns.find_all('a'):
    town_links.append(link.get('href'))

town_foreclocures = []

i = 1

for link in town_links:
    if i < 20:
        full_link = base_url + link
        town_page = urlopen(full_link)
        i = i + 1
        town_soup = BeautifulSoup(town_page, 'html.parser')
        town_foreclocures.append(town_soup.find(attrs={'id': 'ctl00_cphBody_GridView1'}))

print(town_foreclocures)