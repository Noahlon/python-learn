import requests
import json
import threading
import time
import random


url = "https://fat-rabbit.hellobike.cn/api/rpc/method/invoke"
模版id = "7324573985469570622"
# 生成 rosterList 的示例数据
# 生成随机电话号码
def generate_phone_number():
    
    return f"{random.randint(130, 139,151,158,159,170,171,172,173,174,175,176,177,178,179)}{random.randint(10000000, 99999999)}"
# 生成假手机号
def generate_fake_phone_number():
    return f"130{random.randint(10000000, 99999999)}"
# 生成随机姓名
def generate_name():
    import random
    names = ["龙", "张三", "李四", "王五", "赵六"]
    return random.choice(names)


# 生成32位随机数据标识符
def generate_data_identifier():
    import random
    return str(random.randint(1000000000000, 9999999999999))




# 生成 rosterList 列表
def generate_roster_list(num_entries):
    roster_list = []
    for _ in range(num_entries):
        entry = {
            "phone": generate_phone_number(),
            "variableInfos": {
                "k1": "v1",
                "k2": "v2"
            },
            "name": generate_name(),
            "dataIdentifier": generate_data_identifier()
        }
        roster_list.append(entry)
    return roster_list

# 请求的 payload 中包含 loginUser、appId、iface、method、soaHeaders 和 param 字段


def uploadList(nums):
    # 生成 rosterList 列表，假设我们需要 2 个条目
    num_entries = nums
    roster_list = generate_roster_list(num_entries)

    payload = json.dumps({
    "loginUser": {
        "guid": "7e174c6e3130487abd93a6b30576b5bc",
        "realName": "刘乾龙",
        "email": "liuqianlongwb728@hellobike.com"
    },
    "appId": "AppHelloBussinessPortalService",
    "iface": "com.hellobike.business.portal.api.serivce.distribute.DistService",
    "method": "importRoster",
    "soaHeaders": {},
    "param": {
        "rosterList": roster_list,
        "appKey": "caoweicode-WWmJQ8Tb",
        "taskId": 模版id
    }
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)



    print(response.text)

# 多线程启动
def uploadListThread(count):
   
    threads = []
    for i in range(int(count)):
        for _ in range(10):  # 创建10个线程
            thread = threading.Thread(target=uploadList, args=(300,))  # 每个线程传入需要的条目数，例如 300
            threads.append(thread)
            thread.start()
        # 等待所有线程完成
        for thread in threads:
            thread.join()
        print(f"已完成 {i * 3000 } 条数据上传")
        
              

# 压力测试10分钟
def stress_test():
    start_time = time.time()
    duration = 10 # 10分钟
    while time.time() - start_time < duration:
        uploadListThread(4800)  # 每次上传300条数据
        time.sleep(1)  # 每秒上传一次
        
        
        
if __name__ == "__main__":
 
    # uploadListThread(30)  # 3000为单位
    uploadList(300)  
    # 等待上传完成
    



    
   
    

