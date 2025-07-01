import random
import json
import threading

import requests



# 创建数据
def create_test_data(count):
    # 生成随机手机号
    def generate_phone_number():
        return f"11{str(random.randint(100000000, 999999999))}"
    # 生成随机姓名
    def generate_name():
        names = ["张三", "李四", "王五", "赵六", "赵一"]
        return random.choice(names)
    # 生成随机数据标识
    def generate_data_identifier():
        return str(random.randint(1000000000000000, 9000000000000000))
    reslist = []
    for _ in range(count):
        reslist.append({
            "phone": generate_phone_number(),
            "dataIdentifier": generate_data_identifier(),
            "name": generate_name(),
             "variableInfos": {
                "k1": "v1",
                "k2": "v2"
            },
        })
    return reslist

# 上传名单
def upload_roster(id,count):
    url = "https://fat-rabbit.hellobike.cn/api/rpc/method/invoke"
    data = create_test_data(count)

    payload = json.dumps({
    "loginUser": {
        "guid": "7e174c6e3130487abd93a6b30576b5bc",
        "realName": "刘乾龙",
        "email": "liuqianlongwb728@hellobike.com"
    },
    "appId": "AppHelloBussinessPortalService",
    "iface": "com.hellobike.business.portal.api.serivce.distribute.DistService",
    "method": "importRosterByTemplate",
    "soaHeaders": {},
    "param": {
        "rosterList": data,
        "appKey": "caoweicode-WWmJQ8Tb",
        "templateId": id
    }
    })
    headers = {
    'Content-Type': 'application/json'
    }
  
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        # json 格式打印
        print("名单上传成功:")
        print(json.dumps(response.json(), ensure_ascii=False, indent=2))
              
    else:
        # json 格式打印
        print("名单上传失败:")
        print(json.dumps(response.json(), ensure_ascii=False, indent=2))

    # 检查 JSON返回结果
    
# 多线程上传
def uploadListThread(id,count):
   
    threads = []
    for i in range(int(count)):
        for _ in range(10):  # 创建10个线程
            thread = threading.Thread(target=upload_roster, args=(id,300,))  # 每个线程传入需要的条目数，例如 300
            threads.append(thread)
            thread.start()
        # 等待所有线程完成
        for thread in threads:
            thread.join()
        print(f"已完成 {i * 3000 } 条数据上传")

# 测试准备
def test_data_generation():
    # 生成100条测试数据
    data = create_test_data(100)
    # json 格式打印
    print(json.dumps(data, ensure_ascii=False, indent=2))
    

if __name__ == "__main__":
    planTemplateId = "7324343792401711909"  # 模版id
    nums = 300  # 上传名单数量
    # upload_roster(planTemplateId, nums)  # 上传名单
    # 批量上传
    # uploadListThread(planTemplateId, 1000)  # 多线程上传名单
