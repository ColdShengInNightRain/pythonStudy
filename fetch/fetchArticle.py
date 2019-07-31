from bs4 import BeautifulSoup
from urllib import request


def get_soup(url):
    req_result = request.urlopen(url)
    return BeautifulSoup(req_result.read().decode("utf-8"), "html.parser")


def main(a, b):
    if a < b:
        url = "https://www.baidu.com"
        soup = get_soup(url)
        print(soup)
    else:
        print("bii")


main(1, 2)
