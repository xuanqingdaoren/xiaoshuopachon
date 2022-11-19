#基于笔趣阁小说下载的网络爬虫#
import os
import requests
from lxml import etree
import time
import random
while True:
    name = input("请输入小说名字：")
    url_x = input("请输入该小说的url(也就是网址！):")
    try:
        os.mkdir(r'D:\桌面\test')
    except:
        print('已经存在相同的文件夹了,程序无法在继续进行！')
        continue
    
    path = r'D:\桌面\test\ '
    headers = {
        "Referer": "%s"%(url_x),
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1"
    }


    def get_urls():
        url = "%s"%(url_x)
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        html = etree.HTML(response.text)
        # 所有章节的url列表
        url_list = ['http://www.xbiquge.la' + x for x in html.xpath('//div[@id="list"]/dl/dd/a/@href')]
        return url_list


    def get_text(url):
        rep = requests.get(url, headers=headers)
        rep.encoding = 'utf-8'
        dom = etree.HTML(rep.text)
        name = dom.xpath('//div[@class="bookname"]/h1/text()')[0]
        text = dom.xpath('//div[@id="content"]/text()')
        with open(path + f'{name}.txt', 'w', encoding='utf-8') as f:
            for con in text:
                f.write(con)
        print(f'{name} 下载完成')


    def main():
        urls = get_urls()
        for url in urls:
            get_text(url)
            time.sleep(random.randint(1, 3))


    if __name__ == '__main__':
        main()

    rename = r'D:\桌面\%s'%(name)
    os.rename(path,rename)

    num = input("是否退出？<y/n>")
    if num == "y":
        break
