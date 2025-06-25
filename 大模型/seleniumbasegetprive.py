from seleniumbase import SB
import time

with SB(test=True, uc=True, headless=True) as sb:
    try:
        while True:
            # 打开网页
            sb.open("https://cn.tradingview.com/symbols/XAUUSD/")
            # 等待指定元素加载完成，最多等待 10 秒
            sb.wait_for_element(".last-zoF9r75I.js-symbol-last", timeout=20)
            # 定位元素并获取黄金价格
            element = sb.get_element(".last-zoF9r75I.js-symbol-last")
            print("黄金现货价格:", element.text)
            # 等待 5 秒
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n程序已退出。")
    
    input("按回车键退出...")