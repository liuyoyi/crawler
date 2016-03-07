#coding=utf-8
import urllib
import re
import os
import time
import sys

def getHtml(url,dir):
  page=urllib.urlopen(url)
  html=page.read()
  urllib.urlretrieve(url,dir+'/index.html')
  return html         

def getImg(html,dir):
  reg=r'src="(.+?\.jpg)" '
  imgre=re.compile(reg)
  imglist=re.findall(imgre,html)
  x=0
  for imgurl in imglist:
    urllib.urlretrieve(imgurl,dir+'/images/%s.jpg'%x)
    x+=1

def getCss(html,dir):
  reg=r'href="(.+?\.css)" '
  cssre=re.compile(reg)
  csslist=re.findall(cssre,html)
  x=0
  for cssurl in csslist:
    urllib.urlretrieve(cssurl,dir+'/css/%s.css'%x)
    x+=1

def getJs(html,dir):
  reg=r'src="(.+?\.js)"'
  jsre=re.compile(reg)
  jslist=re.findall(jsre,html)
  x=0
  for jsurl in jslist:
    urllib.urlretrieve(jsurl,dir+'/js/%s.js'%x)
    x+=1

if __name__=='__main__':
  while True:
    dir=sys.argv[6]+'/'+time.strftime("%Y%m%d%H%M",time.localtime())
    os.makedirs(dir)
    dirlist=['/images','/css','/js']
    for d in dirlist:
      dird=dir+d
      os.mkdir(dird)
    html=getHtml(sys.argv[4],dir)
    getImg(html,dir)
    getCss(html,dir)
    getJs(html,dir)
    time.sleep(float(sys.argv[2]))
