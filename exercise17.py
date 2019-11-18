import requests
import html5lib
from bs4 import BeautifulSoup

r1 = requests.get('https://www.zeit.de/politik/ausland/2019-11/polen-marsch-unabhaengigkeit-nationalisten-rechtsextreme')
#coverpage = r1
soup1 = BeautifulSoup(r1.text, 'html.parser')
res_soup = soup1.find_all("p", class_="paragraph article__item")
art = []
for a in res_soup:
    #art.append(a)
    #art.append(a.text.strip())
    art.append(a.text.strip('\n'))
result = str(art)
new_result = result.replace("[", "").replace("]", "").replace("'", "").replace("*\n", "").replace("', ", " ").replace(".,", ". ").replace("\xa0\xa0\xa0", "")
print(new_result)





















#for elements in soup1.find_all("p", class_="paragraph article__item"):
#    print(elements.get_text())
#    for elements in soup1.stripped_strings:
#        print(repr(elements))

#print(text)
#articles = []

#for news in soup1:
#    print(soup1.find("p", class_="paragraph article__item").text)

#print(articles)
#print(soup1.p['class': 'paragraph article__item'])