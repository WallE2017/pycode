#coding=utf-8
import urllib
import urllib2
import re
import os
import socket
import sys

# this program is using to download "https://image.baidu.com"'s image
# first parameter is search word
# second parameter is save path
# third parameter is the suffix you choose

socket.setdefaulttimeout(3)
def isThisSuffix(filename, suffix):
    if filename.endswith(suffix):
        return True
    else:
        return False

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'"objURL":"(.*?)"'
    imgre = re.compile(reg)
    print imgre
    imglist = re.findall(imgre,html)
    print len(imglist)
    return imglist
'''
def download(urls,path,pages):
    index=1+pages
    for url in urls:
        print "Downloading:"+url
        try:
            res=urllib2.Request(url)
            if str(res.status_Code)[0]=="4":
		print "Failed!!!"
                continue
	
        except Exception as e:
            print index," Downloaded!!! "
        filename=os.path.join(path,str(index)+".jpg")
	try:
            urllib.urlretrieve(url,filename)
	except Exception as e:
	    print "timeout"
	    index+=1
	    continue
        index+=1
        if index>20+pages:
            break
'''
def download(url, path, pages)
    print "Downloading:"+url
    res=urllib2.Request(url)
    if str(res.status_Code)[0]=="4":
        raise IOError
    filename=os.path.join(path,str(index)+".jpg")
    urllib.urlretrieve(url,filename)
#main
word= sys.argv[1]
Savepath=sys.argv[2]
suffix= sys.argv[3]

for pages in ["0","20","40","60","80"]:
	html = getHtml("https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="+word+"&pn="+pages)
	for url in getImg(html):
            if isJPEG(url,suffix):
                try:
                    download(url,Savepath,int(pages))
                except urllib2.URLError, e:
                    if isinstance (e.reason, socket.timeout):
                        print "timeout"
                        continue
                    elif isinstance (e.reason, urllib2.HTTPError):
                        print " Downloaded!!! "
                    elif isinstance (e.reason, IOError):
                        print "Failed!!!"
                        continue
                    else:
                        print "unknown error"



