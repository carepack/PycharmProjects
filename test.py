import requests
from bs4 import BeautifulSoup

base_url = 'https://www.zeit.de/politik/ausland/2019-11/polen-marsch-unabhaengigkeit-nationalisten-rechtsextreme'
r = requests.get(base_url)
print(base_url)
soup = BeautifulSoup(r.text, 'html.parser')

for article in soup.find_all(class_="paragraph"):
    if article.a:
        #break
        #print(article.a)
        print(article.a.text.replace("\n", " ").strip())

    else:
        #exit
        print(article.contents[0].strip())
