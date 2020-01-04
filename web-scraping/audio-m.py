import wget
import requests
from bs4 import BeautifulSoup

'''
url = 'https://www.goethe.de/en/spr/ueb/rod/da2/l30.html'
cont = requests.get(url)
soup = BeautifulSoup(cont.content,'html.parser')
for x in soup.find_all("div",class_="jw-media jw-reset"):
    print(x)
'''
#silly fun stuff down 
new_url = "https://goethemp4s.akamaized.net/resources/files/mp34/"
con = requests.get(new_url)
print(con.status_code)

'''
soup = BeautifulSoup(con.content,'html.parser')
print(soup.prettify())
'''