# 02.12.2019
# Webcrwalin and save to file

import requests
import sys
from bs4 import BeautifulSoup

def main():
    base_url = 'https://www.zeit.de/politik/ausland/2019-11/polen-marsch-unabhaengigkeit-nationalisten-rechtsextreme'
    #base_url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture#'
    r = requests.get(base_url)
    print(base_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    f_name = input("Please enter filename: ")

    with open(f_name + ".txt", "w")as file:
        for article in soup.find_all(class_="paragraph"):
            if article.a:
                file.write(article.a.text.replace("\n", " ").strip())
            else:
            # exit
                file.write(article.contents[0].strip())

if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise Exception("Python 3 or a more recent version is required.")
    main()