import wx
from seleniumbase import SB
import time
import threading
url = "https://cn.tradingview.com/symbols/BTCUSD/"
# https://cn.tradingview.com/symbols/XAUUSD/

class RealTimeDataFrame(wx.Frame):
    def __init__(self, parent, title="小提示"):
        # 设置 wx.STAY_ON_TOP 样式，让窗口固定在前台
        super().__init__(parent, title=title, size=(100, 50), style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP)

        # 创建面板
        panel = wx.Panel(self)

        # 创建垂直布局的 sizer
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 创建静态文本控件，用于显示黄金价格

        self.label = wx.StaticText(panel, label="0", style=wx.ALIGN_CENTER)

        # 设置字体（可选）
        font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.label.SetFont(font)

        # 添加到布局管理器
        vbox.Add(self.label, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        panel.SetSizer(vbox)

        # 启动获取黄金价格的线程
        self.price_thread = threading.Thread(target=self.get_gold_price)
        self.price_thread.daemon = True
        self.price_thread.start()

        # 显示窗口
        self.Show()

    def get_gold_price(self):
        with SB(test=True, uc=True, headless=True) as sb:
            try:
                while True:
                    # 打开网页

                    sb.open(url)
                    # 等待指定元素加载完成，最多等待 10 秒
                    sb.wait_for_element(".last-zoF9r75I.js-symbol-last", timeout=10)
                    # 定位元素并获取黄金价格
                    element = sb.get_element(".last-zoF9r75I.js-symbol-last")
                    price = element.text
                    # 使用 wx.CallAfter 在主线程更新 UI
                    wx.CallAfter(self.update_label, price)

                    # 等待 5 秒
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\n程序已退出。")

    def update_label(self, price):
        self.label.SetLabel(f"{price}")

if __name__ == "__main__":
    app = wx.App()
    frame = RealTimeDataFrame(None)
    app.MainLoop()