from time import sleep
import requests
import json
import getToken as gt

token = gt.gettoken()
print("获取的token:", token)

# 公共参数
common_params = {
    "token": "bearer_73bc0024-c0d0-4aab-b91c-b5e20297f3c6",
    "url": "https://fat-bff-admin.hellobike.cn/general/bffGeneralReqLogin", 
    "planName": "分流计划核心用例测试001",
    "tenantCode": 11626,
    "tenantName": "分流平台-开放平台租户"
}

# 获取公共参数函数
def get_common_params():
    return common_params


# 分流计划创建
def create_distribution_plan():
    common_params = get_common_params()
    payload = {
    "bffAction": "plan.create",
    "tenantCode": common_params["tenantCode"],
    "tenantName": common_params["tenantName"],
    "distributeType": 1,
    "distributeRuleList": [
        {
            "channelId": 1,
            "channelName": "哈啰AI外呼",
            "percentage": 100,
            "taskTemplateId": "6487974923048321030",
            "taskTemplateName": "分流平台测试发送长短信"
        }
    ],
    "distributePlanName": common_params["planName"]
    }
    headers = {
        'Content-Type': 'application/json',
        'token': common_params["token"]
    }
    response = requests.post(common_params["url"], headers=headers, json=payload)
    if response.status_code == 200:
        print("分流计划创建成功:", response.json())
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
def update_distribution_plan(id):
    common_params = get_common_params()
    payload = {
    "bffAction": "plan.edit",
    "tenantCode": 11629,
    "tenantName": "testnoah",
    "distributeType": 1,
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



    
if __name__ == "__main__":
    是否测试修改 = 0 # 0表示不测试修改，1表示测试修改
    id = create_distribution_plan()
    print("分流计划ID:", id)
    sleep(5)  # 等待5秒钟，确保分流计划创建完成
    upload_roster(id)
    query_distribution_plan(id)
    
    
    
    if(是否测试修改):
        update_distribution_plan(id)
        sleep(5)  # 等待5秒钟，确保分流计划创建完成
        upload_roster(id)
    
    
    # update_distribution_plan()
    
    