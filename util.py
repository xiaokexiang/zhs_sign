"""
工具类
"""
import json
import config
import requests
import time
from lxml import etree


# 解析响应，并获取key的值和res进行比较，相同返回true，其他情况返回false
def parse(source, key, res):
    if not all([source, key, res]):
        return None
    body = dict(json.loads(source))
    value = body.get(key)
    return (False, True)[str(value) == str(res) or str(res) in str(value)]


def now():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# 简单判断是不是html
def is_html(html):
    return len(etree.HTML(html).xpath("/html/head/title")) > 0


"""
推送相关
"""


# 基于server酱推送到微信
def push(caption, desc, _secret_key_):
    url = config.SERVER_PUSH_URL.format(_secret_key_)
    session = requests.session()
    data = {'text': caption, 'desp': desc}
    resp = session.post(url, data)
    if resp.status_code == 200 and parse(resp.text, 'errmsg', 'success'):
        print('push message succeed!')
    else:
        print(resp.content)
        print('push message failed!')


# 基于bark推送消息
def push_bark(caption, desc, _bark_secret_key_):
    url = config.BARK_PUSH_URL.format(_bark_secret_key_, caption, desc)
    session = requests.session()
    resp = session.get(url)
    if resp.status_code == 200 and parse(resp.text, 'code', 200):
        print('push bark message succeed!')
    else:
        print(resp.text)
        print('push bark message failed!')
