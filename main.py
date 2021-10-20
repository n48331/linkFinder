import requests
from bs4 import BeautifulSoup

links = []
url = 'https://oceanovgames.com/vegas-crime-simulator-game-download-free-for-pc/'
website = requests.get(url)

website_text = website.text

soup = BeautifulSoup(website_text)
for link in soup.find_all('a'):
    links.append(link.get('href'))

l = len(links)
print(f'{l} links found')
for link in links:
    print(link)
