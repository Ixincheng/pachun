# coding=utf-8
import urllib
import re


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    # print html
    return html


def getimage(html):
    reg = r'src="(.*?\.png)"/>'
    # reg = r'src="(.+?\.jpg)" '
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    print 4,imglist
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg'%x)
        x += 1


html = getHtml("http://tieba.baidu.com/f?kw=http&fr=fenter&prequery=http%3A%2F%2Fwww.cnblogs.com%2Ffnng%2Fp%2F3576154.html")
print getimage(html)