import config
import json
import os
import requests
import util
from proxy import IpProxy


class Sign:

    # 初始化header相关参数
    def __init__(self):
        if os.environ.get('PROXY_LOCK') is not None and os.environ.get('PROXY_LOCK'):
            IpProxy(config).proxy()
        self.session = requests.Session()
        self.session.headers = config.HEADERS
        user_cookie = os.environ.get('ZHS_COOKIE')
        if user_cookie is None:
            print('No arg: ZHS_COOKIE')
            exit(101)
        self.session.headers['Cookie'] = user_cookie

    # 执行签到逻辑
    def check_in(self):
        return self.session.post(config.CHECK_IN_URL, proxies=config.PROXIES, timeout=20)


if __name__ == '__main__':
    sign = Sign()
    title = ''
    _response_ = sign.check_in()
    if _response_.status_code != 200:
        title = 'VPN签到： 今日签到失败！代理问题：' + str(_response_.status_code) + ' \r'
    elif util.is_html(_response_.text):
        title = "VPN签到：你的cookie已经失效！\r"
    else:
        print(dict(json.loads(_response_.text)).get('msg'))
        if util.parse(_response_.text, 'msg', '已经'):
            title = 'VPN签到：您已经签到过，无需再签到！ \r'
        else:
            title = 'VPN签到：恭喜您，今日签到成功！ \r'
    print(title)
    secret_key = os.environ.get('PUSH_KEY')
    bark_secret_key = os.environ.get('BARK_PUSH_KEY')
    if isinstance(secret_key, str) and len(secret_key) > 0:
        util.push(title, util.now(), secret_key)
    if isinstance(bark_secret_key, str) and len(bark_secret_key) > 0:
        util.push_bark(title, util.now(), bark_secret_key)
