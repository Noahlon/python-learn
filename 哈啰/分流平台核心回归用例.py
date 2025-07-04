from time import sleep
import requests
import json


# 公共参数
common_params = {
    "token": "bearer_e8975124-4368-4ea4-a477-72110848e681",
    "url": "https://fat-bff-admin.hellobike.cn/general/bffGeneralReqLogin", 
    "planName": "测试重试上传名单功能离线下发",
    "tenantCode": 11626,
    "tenantName": "分流平台-开放平台租户",
    "appKey": "caoweicode-WWmJQ8Tb"
    
}

# 获取公共参数函数
def get_common_params():
    return common_params


# 分流计划创建
def create_distribution_plan(distributeType=1):
    common_params = get_common_params()
    payload = {
    "bffAction": "plan.create",
    "tenantCode": common_params["tenantCode"],
    "tenantName": common_params["tenantName"],
    "distributeType": distributeType,
    "distributeRuleList": [
        {
            "channelId": 1,
            "channelName": "哈啰AI外呼",
            "percentage": 100,
            "taskTemplateId": "6487974923048321030",
            "taskTemplateName": "分流平台测试发送长短信"
        }
    ],
    "distributePlanName": "TEST-" + common_params["planName"]
    }
    headers = {
        'Content-Type': 'application/json',
        'token': common_params["token"]
    }
    response = requests.post(common_params["url"], headers=headers, json=payload)
    if response.status_code == 200:
        print("分流计划创建成功:",common_params["planName"], response.json())
        # 返回id
        return response.json()["data"]
    else:
        print("分流计划创建失败:", response.status_code, response.json())
        return None



# 分流计划查询
def query_distribution_plan(id):
    common_params = get_common_params()
    payload ={
    "bffAction": "plan.pageQuery",
    "pageNum": 1,
    "pageSize": 100,
    "planId": id
    }
    headers = {
        'Content-Type': 'application/json',
        'token': common_params["token"]
    }
    response = requests.post(common_params["url"], headers=headers, json=payload)
    if response.status_code == 200:
        print("分流计划查询成功:", response.json())
    else:
        print("分流计划查询失败:", response.status_code, response.json())



# 修改分流计划
def update_distribution_plan(distributeType):
    common_params = get_common_params()
    payload = {
    "bffAction": "plan.edit",
    "tenantCode": 11629,
    "tenantName": "testnoah",
    "distributeType": distributeType,
    "distributeRuleList": [
        {
            "channelId": 1,
            "channelName": "哈啰AI外呼",
            "percentage": 100,
            "taskTemplateId": "6452260517322424560",
            "taskTemplateName": "线路小类中性测试"
        }
    ],
    "distributePlanName": "分流计划增加",
    "distributePlanId": 1000000000000000000
    }
    headers = {
        'Content-Type': 'application/json',
        'token': common_params["token"]
    }
    response = requests.post(common_params["url"], headers=headers, json=payload)
    if response.status_code == 200:
        print("分流计划修改成功:", response.json())
    else:
        print("分流计划修改失败:", response.status_code, response.json())
        return response.json()

# 上传名单
def upload_roster(id):
    url = "https://fat-rabbit.hellobike.cn/api/rpc/method/invoke"

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
        "rosterList": [
        {
            "phone": "13072665126",
            "variableInfos": {
            "k1": "v1",
            "k2": "v2"
            },
            "name": "刘乾龙",
            "dataIdentifier": "1323434343434"
        },
        {
            "phone": "15039506512",
            "variableInfos": {
            "k1": "v1",
            "k2": "v2"
            },
            "name": "张三",
            "dataIdentifier": "1323434343435"
        }
        ],
        "appKey": "caoweicode-WWmJQ8Tb",
        "taskId": id
    }
    })
    headers = {
    'Content-Type': 'application/json'
    }
  
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        print("名单上传成功:", response.json())
    else:
        print("名单上传失败:", response.status_code, response.json())

# 上传名单md5
def upload_roster_md5(id):
    url = "https://fat-rabbit.hellobike.cn/api/rpc/method/invoke"
    params = get_common_params()

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
        "rosterList": [
        {
            "phone": "fd2c581add1dad025a3013c4b087bfa9",
            "variableInfos": {
            "k1": "v1",
            "k2": "v2"
            },
            "name": "刘乾龙",
            "dataIdentifier": "1323434343434"
        },
        {
            "phone": "9dcfb3fa4d4fcac026e19504bfab1806",
            "variableInfos": {
            "k1": "v1",
            "k2": "v2"
            },
            "name": "张三",
            "dataIdentifier": "1323434343435"
        }
        ],
        "rosterType": 2,
        "appKey": params["appKey"],
        "taskId": id
    }
    })
    headers = {
    'Content-Type': 'application/json'
    }
  
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        print("名单上传成功:", response.json())
    else:
        print("名单上传失败:", response.status_code, response.json())

# 离线分流
def offline_distribution():
    # 设置分流名称
    common_params["planName"] = "离线分流测试"
    id = create_distribution_plan(2)
    print("分流计划ID:", id)
    sleep(5)  # 等待5秒钟，确保分流计划创建完成
    upload_roster(id)
    query_distribution_plan(id)

# 实时分流
def real_time_distribution():
    # 设置分流名称
    common_params["planName"] = "实时分流测试"
    id = create_distribution_plan(1)
    print("分流计划ID:", id)
    sleep(5)  # 等待5秒钟，确保分流计划创建完成
    upload_roster(id)
    query_distribution_plan(id)

# 实时分流-md5
def real_time_distribution_md5():
    # 设置分流名称
    common_params["planName"] = "实时分流测试-md5"
    id = create_distribution_plan(1)
    print("分流计划ID:", id)
    sleep(5)  # 等待5秒钟，确保分流计划创建完成
    upload_roster_md5(id)
    query_distribution_plan(id)



# 离线分流-md5
def offline_distribution_md5():
    # 设置分流名称
    common_params["planName"] = "离线分流测试-md5"
    id = create_distribution_plan(2)
    
    sleep(5)  # 等待5秒钟，确保分流计划创建完成
    upload_roster_md5(id)
    query_distribution_plan(id)

# 创建分流模版
def create_distribution_template():
    common_params = get_common_params()
    common_params = get_common_params()
    payload = {
    "bffAction": "plan.template.create",
    "tenantCode": 11626,
    "tenantName": "分流平台-开放平台租户",
    "distributeType": 1,
    "distributeRuleList": [
        {
            "channelId": 1,
            "channelName": "哈啰AI外呼",
            "percentage": 100,
            "taskTemplateId": "6506453281338818692",
            "taskTemplateName": "假呼叫测试副本副本",
            "taskNameDefModel": 3,
            "custTaskNamePart": "分流模版测试"
        }
    ],
    "autoSubpackage": 1,
    "subpackageThreshold": 55,
    "templateName": "TEST-创建分流模版测试"
    }
    headers = {
        'Content-Type': 'application/json',
        'token': common_params["token"] # 使用公共参数中的token
    }
    response = requests.post(common_params["url"], headers=headers, json=payload)
    if response.status_code == 200: 
        print("模版创建成功:", response.json())
    else:
        print("模版创建失败:", response.status_code, response.json())

if __name__ == "__main__":
    
    
    # 创建分流模版
    create_distribution_template()  # 创建分流模版
    
    是否测试主流程 = True
    if 是否测试主流程:
        offline_distribution()  # 离线分流
        real_time_distribution()  # 实时分流
        real_time_distribution_md5()  # 实时分流-md5
        offline_distribution_md5()  # 离线分流-md5
        


    
    

    
    
    