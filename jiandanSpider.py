import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

targetUrl = 'http://jandan.net/ooxx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}


def main():
    brows = webdriver.Chrome('C:/Users/Administrator/Downloads/chromedriver_win32/chromedriver.exe')
    brows.get(targetUrl)
    while 1:
        src = brows.page_source
        bs = BeautifulSoup(src, 'lxml')
        imgs = bs.select('img')
        for img in imgs:
            attr = img.attrs['src']
            try:
                if attr != '' or attr[-3:] != 'jpg':
                    getPic(attr)
            except Exception as e:
                print(e)

        # imgs = brows.find_element_by_css_selector('img');
        nextpage = brows.find_element_by_css_selector('[title="Older Comments"]')
        nextpage.send_keys(Keys.ENTER)


def getPic(url):
    rsp = requests.get(url, headers=headers)
    i = url.rfind('/')
    pic = open('C://testFile1/' + url[i + 1:], 'wb')
    pic.write(rsp.content)
    pic.close()


if __name__ == '__main__':
    main()
