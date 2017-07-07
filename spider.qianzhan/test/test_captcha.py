# -*- coding:utf-8 -*-
__author__ = 'zhaojm'
import requests
# from ..captcha import read_body_to_string
from captcha import read_body_to_string, read_file_to_string

default_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6',
    # Cache-Control:no-cache
    'Connection': 'keep-alive',
    # 'Cookie': 'qznewsite.uid=rssbv51ml0mwomw4k4mkycz2; qz.newsite=41A3A9C8ADE5F5073B86647E6C185D2272112F0E96AD14B275E442ED8A2B85688F50512A00FAD14DB2D485EF57054E35ECB028B44D155EE32D029A4352C6617B74BE83EB551C4D66024D7F4913B053785964ED37F3061D43BA0E8663791A1E143AC458E738C7484453887CEAB6EDEC359632DDDEAF6D585D0BD31087077296B6D97CF68F',
    'Host': 'qiye.qianzhan.com',
    # Pragma:no-cache
    'Referer': 'http://qiye.qianzhan.com/',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
}

session = requests.Session()
session.headers.update(default_headers)

if __name__ == "__main__":
    # response = session.get("http://qiye.qianzhan.com/usercenter/varifyimage?0.0856926187338")
    # print response.content
    varifycode = read_file_to_string("varifyimage.gif")
    print varifycode
    pass