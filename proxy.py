import time

from lxml import etree
import requests


class IpProxy:
    def __init__(self, config):
        self.config = config
        self.session = requests.Session()
        self.session.headers = config.HEADERS
        self.post_ips = self.get_proxy()  # 获取符合条件的https + post 代理地址

    def get_proxy(self):
        ips = []
        resp = self.session.get(self.config.PROXY_URL)
        if resp.status_code != 200:
            return ips
        else:
            root = etree.HTML(resp.text)
            convert = root.xpath('/html/body/div[2]/div[2]/table/tbody/tr')
            for ip in convert:
                i = ip.xpath('td')
                if i[4].text == '支持' and i[5].text == '支持' and '中国' not in i[2].xpath('a'):  # 国外 & https & POST
                    href = dict(i[0].xpath('a')[0].attrib).get('href')
                    ips.append(self.config.PROXY_URL + href)
            return ips

    def proxy(self):
        for ip in self.post_ips:
            resp = requests.session().get(ip)
            time.sleep(2)
            if resp.status_code == 200:
                proxies = ('https://' + dict(etree.HTML(resp.text).xpath('//*[@id="ip"]')[0].attrib).get('value'))
                self.config.PROXIES['https'] = proxies
                break
        print(self.config.PROXIES)
