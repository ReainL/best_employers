#!/usr/bin/env python2.7
# encoding: utf-8
"""
Created on 18-1-2

@author: Xu
"""
import requests
import json
import re
import random
import sys
import time
import datetime  #处理日期和时间的标准库
import threading  #引入多线程
from random import choice  #choice() 方法返回一个列表，元组或字符串的随机项
from bs4 import BeautifulSoup
from fake_useragent import UserAgent #引入userAgent


def get_ip():
    '''获取代理IP'''
    url = 'http://www.xicidaili.com/nn'
    my_headers = {
        'Accept': 'text/html, application/xhtml+xml, application/xml;',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Referer': 'http: // www.xicidaili.com/nn',
        'User-Agent': 'Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 45.0.2454.101Safari / 537.36'
    }
    r = requests.get(url,headers=my_headers)
    soup = BeautifulSoup(r.text,'html.parser')
    data = soup.find_all('td')

    #定义IP和端口Pattern规则
    ip_compile = re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')  #匹配IP
    port_compile = re.compile(r'<td>(\d+)</td>')  #匹配端口
    ip = re.findall(ip_compile,str(data))    #获取所有IP
    port = re.findall(port_compile,str(data))  #获取所有端口
    z = [':'.join(i) for i in zip(ip,port)]  #列表生成式
    print z
    #组合IP和端口
    return z

# 设置user-agent列表,每次请求时，随机挑选一个user-agent
ua_list = UserAgent()
print ua_list.random

def get_url(url,code=0,ips=[]):
    '''
    投票
    如果因为代理IP已失效造成投票失败，则会自动换一个代理IP后继续投票
    :param code:
    :param ips:
    :return:
    '''
    try:
        ip = choice(ips)
    except:
        return False

    else:
        #指定IP
        proxies = {
            'http':ip
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'best.zhaopin.com',
            'Origin': 'https: // best.zhaopin.com',
            'Referer':'https//best.zhaopin.com/?sid=121128100&site=sou',
            # 'User-Agent':choice(ua_list)
            'User-Agent': ua_list.random
        }
        print ua_list.random

    try:
        data = {"bestid": "3713", "score": "5,5,5,5,5,5","source": "best",}

        result = requests.post(url=url,data=data, proxies=proxies,)  # 跳过证书的验证 verify=False
    except requests.exceptions.ConnectionError:
        print 'ConnectionError'
        if not ips:
            print 'ip 已失效'
            sys.exit()
        #删除不可用的代理IP
        if ip in ips:
            ips.remove(ip)
        #重新请求url
        get_url(url,code=0,ips=[])
    else:
        date = datetime.datetime.now().strftime('%H:%M:%S')
        # result.text() 投票成功显示1  失败显示0
        print u"第%s次 [%s] [%s]：投票%s (剩余可用代理IP数：%s)" % (code, date, ip, result.text, len(ips))

def get_num(num):
    #点赞的请求
    url1 = 'https://best.zhaopin.com/API/Vote.ashx'
    #投票的请求
    url2 = 'https://best.zhaopin.com/API/ScoreCompany.ashx'
    if num == 1:
        url=url1
        main(url)
    elif num == 2:
        url =url2
        main(url)
    else:
        print '您的输入有误，请重新输入！！！'
        num = int(raw_input('自主刷赞请选1，自动投票请选2：'))
        get_num(num)


def main(url):
    ips = []
    #xrange() 生成的是一个生成器
    for i in xrange(6000):
        # 每隔1000次重新获取一次最新的代理IP，每次可获取最新的100个代理IP
        if i % 1000 == 0:
            ips.extend(get_ip())
            print '--------------------------------------'
            print ips
        #启动线程，每隔1s产生一个线程，可通过控制时间加快投票速度
        t1 = threading.Thread(target=get_url,args=(url,i,ips))
        t1.start()
        time.sleep(1)  #time.sleep的最小单位是毫秒




if __name__ == '__main__':
    # #点赞的请求
    # url1 = 'https://best.zhaopin.com/API/Vote.ashx'
    # #投票的请求
    # url2 = 'https://best.zhaopin.com/API/ScoreCompany.ashx'
    print '欢迎使用自助刷票小工具QAQ'
    num = int(raw_input('自主刷赞请选1，自动投票请选2：'))
    get_num(num)