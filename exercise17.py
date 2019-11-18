from bs4 import BeautifulSoup
import requests


response = requests.get('http://www.zeit.de/politik/index')
print(response.status_code)
print(response.headers['content-type'])
print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())



#import faster_than_requests as req



#import requests



#url = req.gets("https://zeit.de/politik/index")
#print(url)


# print (response.status_code)
# print (response.content)
# requests
# print(req.gets("https://www.zeit.de/politik/index"))

# print("hello")
# soup = bs4(html_doc, 'html.parser')
