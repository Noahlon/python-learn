import wx
from seleniumbase import SB
import time
import threading    

# 定义两个 URL，分别对应 BTCUSD 和 XAUUSD
btc_url = "https://cn.tradingview.com/symbols/BTCUSD/"
xau_url = "https://cn.tradingview.com/symbols/XAUUSD/"


class RealTimeDataFrame(wx.Frame):
    def __init__(self, parent, title="小提示"):
        # 设置 wx.STAY_ON_TOP 样式，让窗口固定在前台
        super().__init__(parent, title=title, size=(200, 100), style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP)

        # 创建面板
        panel = wx.Panel(self)

        # 创建垂直布局的 sizer
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 创建静态文本控件，用于显示比特币价格
        self.btc_label = wx.StaticText(panel, label="0", style=wx.ALIGN_CENTER)

        # 创建静态文本控件，用于显示黄金价格
        self.xau_label = wx.StaticText(panel, label="0", style=wx.ALIGN_CENTER)

        # 设置字体（可选）
        font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.btc_label.SetFont(font)
        self.xau_label.SetFont(font)

        # 添加到布局管理器
        vbox.Add(self.btc_label, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(self.xau_label, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        panel.SetSizer(vbox)

        # 启动获取比特币和黄金价格的线程
        self.btc_price_thread = threading.Thread(target=self.get_price, args=(btc_url, self.btc_label, "BTC"))
        self.btc_price_thread.daemon = True
        self.btc_price_thread.start()

        self.xau_price_thread = threading.Thread(target=self.get_price, args=(xau_url, self.xau_label, "XAU"))
        self.xau_price_thread.daemon = True
        self.xau_price_thread.start()

        # 显示窗口
        self.Show()

    def get_price(self, url, label, symbol):
        max_retries = 5  # 最大重试次数
        retry_delay = 10  # 每次重试间隔时间（秒）

        with SB(test=True, uc=True, headless=True) as sb:
            while True:
                retries = 0
                while retries < max_retries:
                    try:
                        # 打开网页
                        sb.open(url)
                        # 等待指定元素加载完成，最多等待 100 秒
                        sb.wait_for_element(".last-zoF9r75I.js-symbol-last", timeout=100)
                        # 定位元素并获取价格
                        element = sb.get_element(".last-zoF9r75I.js-symbol-last")
                        price = element.text
                        print(f"{symbol} 价格: {price}")
                        # 使用 wx.CallAfter 在主线程更新 UI，只传入价格
                        wx.CallAfter(self.update_label, label, price)
                        break  # 成功获取数据，跳出重试循环
                    except Exception as e:
                        retries += 1
                        print(f"尝试获取 {symbol} 数据失败，错误信息: {e}，重试次数: {retries}/{max_retries}")
                        if retries < max_retries:
                            print(f"等待 {retry_delay} 秒后重试...")
                            time.sleep(retry_delay)
                        else:
                            print(f"达到最大重试次数，本次 {symbol} 循环结束，等待下一次尝试。")

                # 无论是否成功，等待 1 秒后进行下一次循环
                time.sleep(1)

    def update_label(self, label, price):
        label.SetLabel(price)

if __name__ == "__main__":
    app = wx.App()
    frame = RealTimeDataFrame(None)
    app.MainLoop()