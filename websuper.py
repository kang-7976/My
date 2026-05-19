import requests
import random
import re
from time import sleep

# 模拟浏览器UA池，防止被拦截
ua_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
]

def super_spider_search():
    word = input("请输入搜索关键词：")
    print("\n超级爬虫正在全网检索中...\n")

    headers = {"User-Agent": random.choice(ua_list)}
    url = f"https://www.baidu.com/s?wd={word}"

    try:
        # 随机延时，模拟人浏览，降低被封概率
        sleep(random.uniform(1, 3))
        res = requests.get(url, headers=headers, timeout=20)
        res.encoding = "utf-8"
        html = res.text

        # 同时提取标题和链接
        pattern = r'<h3.*?href="(.*?)".*?>(.*?)</h3>'
        results = re.findall(pattern, html, re.S)

        print("===== 精选5条搜索结果 =====")
        for i in range(5):
            if i < len(results):
                link, title = results[i]
                # 清理标题里的HTML标签
                clean_title = re.sub(r'<[^>]+>', '', title.strip())
                print(f"{i+1}. {clean_title}")
                print(f"   链接：{link}\n")
            else:
                print(f"{i+1}. 暂无更多相关内容\n")

    except Exception as e:
        print("访问失败！错误信息：", e)

if __name__ == "__main__":
    while True:
        super_spider_search()
        print("-" * 30)


