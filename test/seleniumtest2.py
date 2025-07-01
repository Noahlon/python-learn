from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from time import sleep
from selenium.webdriver.chrome.options import Options


# 执行 JavaScript 代码将 window.navigator.webdriver 设置为 undefined
def set_webdriver_undefined(browser):
    browser.execute_script("Object.defineProperty(window.navigator, 'webdriver', {get: () => undefined})")
    #获取 Window.navigator.webdriver 的值
    webdriver_value = browser.execute_script("return window.navigator.webdriver")
    if webdriver_value is None:
        print("Window.navigator.webdriver is set to undefined successfully.")
    else:
        print(f"Failed to set Window.navigator.webdriver: {webdriver_value}")

def init_browser():
    # 创建 Chrome 浏览器对象
    browser = webdriver.Chrome()
    # “Chrome正受到自动测试软件的控制”隐藏掉
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--disable-blink-features=AutomationControlled")

    # 设置无头模式（可选）
    # options.add_argument("--headless")  
    browser = webdriver.Chrome(options=options)
    return browser



# 创建Chrome浏览器对象
browser = init_browser()

# test execute script
browser.execute_script("alert('Hello, this is a test alert!')")

# Handle the alert
sleep(2)  # 等待2秒钟以便查看alert
alert = Alert(browser)
alert.accept()

set_webdriver_undefined(browser)


browser.get('https://www.baidu.com/')
# 通过元素ID获取元素
kw_input = browser.find_element(By.ID, 'kw')
# 模拟用户输入行为
kw_input.send_keys('Python')
# 通过CSS选择器获取元素
su_button = browser.find_element(By.CSS_SELECTOR, '#su')
# 模拟用户点击行为
su_button.click()
set_webdriver_undefined(browser)
# 退出
sleep(5)  # 等待5秒钟以便查看结果
browser.quit()
