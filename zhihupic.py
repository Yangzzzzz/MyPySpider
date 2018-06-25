import os
import re
import string

from bs4 import BeautifulSoup
from lxml import etree
import requests

filePath = 'C://zhihuPic/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}


def getPic(url):
    global headers
    rsp = requests.get(url, headers=headers)
    i = url.rfind('/')
    pic = open(filePath + url[i + 1:], 'wb')
    pic.write(rsp.content)
    pic.close()


if __name__ == '__main__':
    if not os.path.exists(filePath):
        os.makedirs(filePath)
    i = 1
    for j in range(1, 30):
        rsp = requests.get(
            "https://www.zhihu.com/api/v4/questions/263952082/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=" + str(
                i) + "&limit=20&sort_by=default", headers=headers)
        et = rsp.json()['data']
        print(rsp.text)
        # nodes = re.compile('https://pic.*?(?=\")').findall(rsp.text)

        for node in et:
            node = etree.HTML(node['content'])
            node = node.xpath('//figure/img/@data-original')
            for n in node:
                getPic(n)
        i += 20
