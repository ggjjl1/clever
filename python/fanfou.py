#!/usr/bin/env python
# -*- coding: utf-8 -*_

"一个尝试用Python编写的饭否客户端"

from __future__ import print_function

import re
import urllib
import requests
import datetime
import argparse
import getpass


class Fanfou(object):
    def __init__(self, username, password):
        # 输入用户名密码
        self.username = username
        self.password = password
        self.useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        self.max_id = ''
        self.session = None

    def login(self):
        login_url = "http://fanfou.com/login"
        datas = {
            'loginname': self.username,
            'loginpass': self.password
        }
        headers = {
            'User-Agent': self.useragent
        }
        # 获取登录参数
        r = requests.get('http://fanfou.com/login?fr=%2F',headers=headers)
        s = re.search('<p class="act">[\s\S]*?name="token" value="(.*?)"[\s\S]*?name="urlfrom" value="(.*?)"[\s\S]*?</p>', r.text)
        token = s.group(1)
        urlfrom = s.group(2)
        datas.update({'action': 'login', 'token': token, 'urlfrom': urlfrom})
        # 通过session方式登录
        self.session = requests.Session()
        rs = self.session.post(login_url, data=datas, headers=headers)

    # 获取首页用户消息
    def getNews(self, max_id=''):
        if self.session is None:
            # print('未登录状态，开始登录')
            self.login()
        url = 'http://fanfou.com/home' if max_id == '' else 'http://fanfou.com/home?max_id=' + max_id
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Cookie': '__utmc=208515845; __utmz=208515845.1586240220.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=208515845.visitor; u=ggjjl1; uuid=fb047ba2fd4e33b348d8.1586240218.6; PHPSESSID=g5ud8uarvjgth1c0rq52splee7; m=ggjjl1; __utma=208515845.1428455074.1586240220.1586939540.1586952014.16; __utmt=1; __utmb=208515845.1.10.1586952014'
        }
        # r = requests.get(url, headers=headers)
        r = self.session.get(url)
        pattern = re.compile(r'<div id="stream" class="message"><ol[\s\S]*</ol></div>')
        pattern1 = re.compile(r'<li><a.*?<img.*?></a><a.*?<span class="op">.*?</span></li>')
        s = pattern.search(r.text)
        messages = re.findall(pattern1, s.group())
        for m in messages:
            head = re.search('<a href="/(.*?)" title="(.*?)" class="avatar"><img src="(.*?)" alt="(.*?)" /></a>.*?<span.*?id="(.*?)" class="content" >(<a href="(.*?)".*?</a>)*(.*?)</span>.*?<span class="stamp"><a.*?stime="(.*?)">', m)
            if head is not None:
                uid = head.group(1)
                uname = head.group(2)
                avatar = head.group(3)
                ffid = head.group(5)
                photo = head.group(7)
                content = head.group(8)
                stime = head.group(9)
                
                content = re.sub('<a href=.*?>','',content)
                content = re.sub('</a>','',content)
                print("[%s] %s: %s"%(ffid,uname,content))
                # now = datetime.datetime.now().strftime('%a %b %d %H:%M:%S +0000 %Y')
                self.max_id = ffid
            else:
                print("head匹配失败。")

    # 获取更多用户消息
    def getNext(self, max_id=''):
        max_id = self.max_id if max_id == '' else max_id
        self.getNews(max_id)

    def getHtml(self):
        url = "http://fanfou.com/"
        html = urllib.urlopen(url)
        text = html.read()
        info = html.info()
        rurl = html.geturl()
        rcode = html.getcode()
        print(rcode)

def main():
    uname = input("用户名: ")
    pwd = getpass.getpass('密码: ')
    fanfou = Fanfou(uname, pwd)
    # fanfou.login()
    # fanfou.getNews()
    # print("max_id: %s"%fanfou.max_id)
    # fanfou.getNext()
    while True:
        entry = input(">")
        if entry == 'quit' or entry == 'exit':
            break
        elif entry == 'home':
            fanfou.getNews()
        elif entry == 'next':
            fanfou.getNews(fanfou.max_id)

if __name__ == '__main__':
    main()
