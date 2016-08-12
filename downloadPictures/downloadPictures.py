#  爬取极客学院首页图片的爬虫

import re
import urllib.request

response  = urllib.request.urlopen('http://www.jikexueyuan.com/')
html = str(response.read())

pic_urls = re.findall('img src="(.*?)"',html,re.S)
i = 0
for url in pic_urls:
    print("downloading:",i,'.jpg...')
    urllib.request.urlretrieve(url,'pic\\'+str(i)+'.jpg')
    i+=1