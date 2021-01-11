import config
import json
import os
import requests
import time


def now():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# 基于server酱推送到微信
def push(title, desc, _secret_key_):
    url = config.PUSH_URL.format(_secret_key_)
    session = requests.session()
    data = {'text': title, 'desp': desc}
    resp = session.post(url, data)
    if resp.status_code == 200 and parse(resp.text, 'errmsg', 'success'):
        print('push message succeed!')
    else:
        print('push message failed!')


# 解析响应，并获取key的值和res进行比较，相同返回true，其他情况返回false
def parse(source, key, res):
    if not all([source, key, res]):
        return None
    body = dict(json.loads(source))
    value = body.get(key)
    return (False, True)[value == res or str(value).index(res) > 0]


class Sign:

    # 初始化header相关参数
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = config.HEADERS
        user_cookie = os.environ.get('ZHS_COOKIE')
        if user_cookie is None:
            print('No arg: ZHS_COOKIE')
            exit(101)
        self.session.headers['Cookie'] = user_cookie
        self.session.proxies = config.PROXIES

    # 执行签到逻辑
    def check_in(self):
        resp = self.session.post(config.CHECK_IN_URL)
        if resp.status_code == 200:
            return resp
        else:
            return None


if __name__ == '__main__':
    sign = Sign()
    msg = ''
    _response_ = sign.check_in()
    if _response_ is None:
        msg = '###抱歉，今日签到失败！ \r' + _response_.reason
    else:
        if parse(_response_.text, 'msg', '已经'):
            msg = '###您已经签到过，无需再签到！ \r' + now()
        else:
            msg = '###恭喜您，今日签到成功！ \r' + now()
            print("check in success!")
    secret_key = os.environ.get('PUSH_KEY')
    if isinstance(secret_key, str) and len(secret_key) > 0:
        push('Vpn自动签到', msg, secret_key)
