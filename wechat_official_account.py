import json
from settings import COOKIE,USERVID
import requests
from bs4 import BeautifulSoup

def get_wechat(bookId):
    """获取书的详情"""
    headers = {
       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
        #  wr_vid=377902464; wr_skey=IwHc_Q9g;
        "Cookie": COOKIE,
    }
    url = "https://weread.qq.com/wrpage/book/share/%s?ref=app" % bookId
    r = requests.get(url,headers=headers).text

    # 开始解析html
    soup = BeautifulSoup(r)
    # 找到文章列表
    news = soup.find_all("li")
    # 遍历列表
    for new in news:
        # 获取单篇文章的链接
        if new['class'][1] == "js_mp_scheme_link":
            print("链接：%s" % new["data-url"])

        # 获取单篇文章的其他信息
        items = new.find_all("div")
        for item in items:
            try:
                if item['class'][0] == "detail_mpArticle_item_title":
                    print("标题：%s" % item.string)
                elif item['class'][0] == "detail_mpArticle_item_desc":
                    print("介绍：%s" % item.string)
                elif item['class'][0] == "wr_feedMeta_date":
                    print("时间：%s" % item.string)
            except Exception as e:
                pass
        # 结束收尾
        print("-"*50)

if __name__ == '__main__':
    get_wechat("MP_WXS_3584965877")