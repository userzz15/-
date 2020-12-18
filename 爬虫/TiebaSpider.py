import requests

class TiebaSpider():
    def __init__(self, url_name):
        self.url = "https://tieba.baidu.com/f"
        self.url_name = url_name

    def run(self):
        params = {'kw': "李毅"}
        herders = {
            'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) '
                            'AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 84.0.4147.135Safari / 537.36'
        }
        response = requests.get(self.url, params=params, headers = herders)
        # print(response.content.decode())
        print(response.url)

if __name__ == "__main__":
    tbspider = TiebaSpider("李毅")
    tbspider.run()