from bs4 import BeautifulSoup
import requests

source = requests.get('https://en.wikipedia.org/wiki/LeBron_James').text

soup = BeautifulSoup(source, features='html.parser')
# Whole page
output = soup.find_all('dir')
print(output.pretiffy())