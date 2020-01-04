import requests
from bs4 import BeautifulSoup
import csv
url = 'https://1000mostcommonwords.com/1000-most-common-german-words/'
cont = requests.get(url)
soup = BeautifulSoup(cont.content,'html.parser')
filename = "1000 Most Common German Words.csv"#soup.title.text

with open(filename,'w') as csvfile:
    writer = csv.writer(csvfile)
    for tables in soup.find_all("tr"):
        writer.writerow(list(tables.text.strip().split("\n")))
    #print(text)

        #data.append()

#for i in range(0,len(data)):
#print(data)


