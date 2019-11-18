import requests
from bs4 import BeautifulSoup

base_url = 'https://www.zeit.de/politik/ausland/2019-11/polen-marsch-unabhaengigkeit-nationalisten-rechtsextreme'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')

for story_heading in soup.find_all(class_="paragraph"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    #else:
    #    print(story_heading.contents[0].strip())