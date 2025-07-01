import hashlib
import time
import requests
import json
from collections import OrderedDict

def get_open_api_token(app_key, secret):
    """
    获取 Open API 的 token
    :param app_key: 应用的 app key
    :param secret: 应用的秘钥
    :return: 返回 token 字符串
    """
    url = "https://fat-hello-openapi.hellobike.com/login"
    phone_number = "15669059790"
    timestamp = str(int(time.time() * 1000))

    params = {
        "method": "hello.open.login",
        "appKey": app_key,
        "timestamp": timestamp,
        "phoneNumber": phone_number
    }
    sign = sign_top_request(params, secret)
    params["sign"] = sign

    headers = {}  # 假设 headers 为空，可按需修改
    response = requests.post(url, json=params, headers=headers)
    token_object = response.json()
    return token_object.get("data")

def sign_top_request(params, secret):
    """
    根据参数创建 sign
    :param params: 参数信息
    :param secret: 秘钥
    :return: sign 字符串
    """
    # 第一步：对参数键进行排序
    sorted_params = OrderedDict(sorted(params.items()))
    # 第二步：把所有参数名和参数值串在一起
    query = secret
    for key, value in sorted_params.items():
        if key.strip():
            if value is not None:
                query += key.strip()
                if isinstance(value, (list, dict)):
                    query += json.dumps(value)
                else:
                    query += str(value)
    query += secret
    return get_md5_str(query)

def get_md5_str(s):
    """
    MD5 加密，返回最终的 sign
    :param s: 待加密的字符串
    :return: 加密后的小写 16 进制字符串
    """
    md5 = hashlib.md5(s.encode('utf-8'))
    return md5.hexdigest()
def gettoken():
    """
    获取 token 的简易接口
    :return: 返回 token 字符串
    """
    app_key = "caoweicode-WWmJQ8Tb"
    secret = "801afd8e48764d6f9336cc8a7e277db3"
    token = "Bearer_" + get_open_api_token(app_key, secret)
    return token
    
if __name__ == "__main__":
    app_key = "caoweicode-WWmJQ8Tb"
    secret = "b3c7f0d2-4e8a-4b1c-9f5c-6d8e0f1a2b3c"
    token = get_open_api_token(app_key, secret)
    bearer_token = "Bearer_" + token
    print("Bearer token:", bearer_token)