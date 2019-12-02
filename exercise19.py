# 02.12.2019
# Webcrwalin part 2

import requests
import sys
from bs4 import BeautifulSoup

def main():
    url_fetch = requests.get('https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture#').text
    soup = BeautifulSoup(url_fetch, 'html.parser')
    #print(str(soup.select("article")))
    page = soup.find_all('p')
    print(page)

if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise Exception("Python 3 or a more recent version is required.")
    main()
