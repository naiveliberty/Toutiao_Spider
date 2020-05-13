import requests
import urllib3

urllib3.disable_warnings()


class Toutiao():
    def __init__(self):
        self.index_url = 'https://www.toutiao.com/'
        self.session = requests.Session()
        self.news_list = ['https://www.toutiao.com/a6824330213816533518/',
                          'https://www.toutiao.com/a6813910751485362696/']
        self.nodejs_server = 'http://127.0.0.1:8000/toutiao'

    def get_news_info(self):
        for index, url in enumerate(self.news_list):
            headers = {
                'authority': 'www.toutiao.com',
                'pragma': 'no-cache',
                'cache-control': 'no-cache',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-dest': 'document',
                'accept-language': 'zh-CN,zh;q=0.9',
            }
            if index == 0:
                # 第一次获取请求在 response 中获取 key为：__ac_nonce 的值，用来生成 __ac_signature
                res = self.session.get(url=url, headers=headers, verify=False)
                nonce = res.cookies['__ac_nonce']
                userAgent = headers['user-agent']
                params = {
                    'nonce': nonce,
                    'url': url,
                    'userAgent': userAgent
                }
                signature = requests.get(self.nodejs_server, params=params).text
                self.session.cookies['__ac_signature'] = signature
                res = self.session.get(url=url, headers=headers, verify=False)
                print(res.text)
            else:
                res = self.session.get(url=url, headers=headers, verify=False)
                print(res.text)

    def run(self):
        self.get_news_info()


if __name__ == '__main__':
    tt = Toutiao()
    tt.run()
