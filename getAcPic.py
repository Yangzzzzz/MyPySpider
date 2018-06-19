import requests
import multiprocessing
import re
from bs4 import BeautifulSoup

picApiUrl = 'http://webapi.aixifan.com/query/article/list?&size=10&realmIds=21&originalOnly=false&orderType=2&periodType=-1&filterTitleImage=true'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}


def getPic(url):
    rsp = requests.get(url, headers=headers)
    i = url.rfind('/')
    pic = open('C://testFile1/' + url[i + 1:], 'wb')
    pic.write(rsp.content)
    pic.close()


def getOnePageView(url):
    res = requests.get(url, headers=headers).content.decode('utf-8')
    sb = BeautifulSoup(res, 'lxml')
    picac = sb.select('#article-content p img')
    for picadd in picac:
        getPic(picadd.attrs['src'])
    # http: // imgs.aixifan.com / o_1cfpcckmr1s8c1se01srn1jfk6ru1f.jpg


if __name__ == '__main__':
    # getOnePageView('http://www.acfun.cn/a/ac4403575')
    res = requests.get(picApiUrl + '&pageNo=1', headers=headers).json()
    total = res['data']['totalPage']
    for i in range(1, total):
        pageNo = i
        getUrl = picApiUrl + '&pageNo=' + str(i)
        res = requests.get(getUrl, headers=headers).json()
        for j in res['data']['articleList']:
            acid = j['id']
            # getOnePageView('http://www.acfun.cn/a/ac'+str(acid))
            pool = multiprocessing.Process(target=getOnePageView, args=['http://www.acfun.cn/a/ac' + str(acid)])
            pool.start()
            pool.join()