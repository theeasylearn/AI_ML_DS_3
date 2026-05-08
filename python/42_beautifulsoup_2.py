webpage = 'https://www.divyabhaskar.co.in/rashifal/13/today?ref=inbound_RHS'
# from package-name import module name
from bs4 import BeautifulSoup
import requests
html = requests.get(webpage)
soup = BeautifulSoup(html.text, 'html.parser')
mytext = soup.find('div',class_='a6b3d8fe')
for item in mytext.find_all('p'):
    print(item.text)
    # print('_'*100)