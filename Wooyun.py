#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__ = 'croxy'

from bs4 import BeautifulSoup
import requests
import re
import sys
#from lxml import *

headers = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
'Accept-Encoding': 'gzip, deflate, compress',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
"Accept-Language": "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0"
}


def getwooyun(page):
    for i in range(1,page):
        url = 'http://www.wooyun.org/bugs/new_public/page/%s' %(i)
        q = requests.get(url,headers=headers)
        content = q.content
        soup = BeautifulSoup(content)
        alltext =  soup.find_all('th')
        lens =  len(alltext)
        #print lens
        for j in range(lens):
            #print alltext[j]
            bugs = re.findall(r"href=\"(.+?)#comment\"",str(alltext[j]))
            focus = re.findall(r"评论一下\">(.+?)</a>", str(alltext[j]))
            #print len(focus)
            if focus:
                focuser =  str(focus).split("/")
                number =  focuser[1].strip("']")
                if int(number) > 20:
                    print "<a href=\"http://wooyun.org"+bugs[0]+'"></a>'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Please : Python %s page" % sys.argv[0]
        sys.exit()
    else:
        pages = sys.argv[1]
        getwooyun(int(pages))
