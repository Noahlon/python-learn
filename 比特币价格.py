import time
import requests

def get_bitcoin_price_with_retry(retries=3, delay=5):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "TRUMP",
        "vs_currencies": "usd"
    }
    for attempt in range(retries):
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            price = data.get("TRUMP", {}).get("usd")
            if price:
                print(f"币价格: ${price}")  
                return
            else:
                print("无法获取比特币价格")
                return
        elif response.status_code == 429:
            print("请求过多，等待后重试...")
            time.sleep(delay)
        else:
            print(f"请求失败，状态码: {response.status_code}")
            return
    print("多次重试后仍然失败")

def get_crypto_price(crypto_id, currency="usd"):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": crypto_id,  # 加密货币的 ID
        "vs_currencies": currency  # 目标货币
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            price = data.get(crypto_id, {}).get(currency)
            if price:
                print(f"当前 {crypto_id} 的价格: {price} {currency.upper()}")
            else:
                print(f"无法获取 {crypto_id} 的价格")
        elif response.status_code == 429:
            print("请求过多，请稍后再试")
        else:
            print(f"请求失败，状态码: {response.status_code}")
    except Exception as e:
        print(f"发生错误: {e}")

# 调用函数
get_crypto_price("trumpcoin")  # 替换为实际的加密货币 ID
# 调用函数
get_bitcoin_price_with_retry()