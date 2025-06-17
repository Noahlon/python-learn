import re
from time import sleep
import requests

url = "https://cn.tradingview.com/symbols/BTCUSD/"

# 获得数据
def get_data(url):
    headers = {
        "User-Agent": "baiduSpider",
        "Referer": "https://www.baidu.com"
    }
    response = requests.get(url, headers=headers)
    # 直接返回响应文本
    return response.text




html_text = get_data(url)
pattern = r"[^\u4e00-\u9fa5\d]"
# 将非中文和数字的字符替换为空
result = re.sub(pattern, "", html_text)

print(result)  # 输出：这是一些文本123
price_index = html_text.find("last-zoF9r75I js-symbol-last")

if price_index != -1:
    print(html_text[price_index:price_index + 300])
