import json

# 明文参数
plaintext_params = {
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
        "rosterType": 2,
        "appKey": "caoweicode-WWmJQ8Tb",
        "taskId": id
    }
 }

# 获取明文参数
def get_plaintext_params():
    return plaintext_params

# MD5参数
MD5_params = {
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
 }


# 获取MD5参数
def get_md5_params():
    return MD5_params
if __name__ == "__main__":
    print("明文参数:", get_plaintext_params())
    print("MD5参数:", get_md5_params())