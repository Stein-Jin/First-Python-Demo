import requests
import json
import pandas as pd

adcode = '310101'
APIkey = "98a805506f788f97f37a9cfae49d8216"
areaname_dict = {"310101": "黄浦区", "310106": "静安区", "310110": "杨浦区", "310109": "虹口区"}
type = "all"


def get_df(adcode, APIkey, areaname_dict):
    url = 'https://restapi.amap.com/v3/weather/weatherInfo'  # API地址
    payload = {'city': adcode, 'key': APIkey}  # 传入API参数

    r = requests.get(url, params=payload)  # GET请求API结果

    content_json = json.loads(r.content)  # 转换成json格式
    df = pd.DataFrame(content_json['lives'])
    df['areaname'] = areaname_dict(adcode)
    return df

def get_dfs(areaname_dict,APIkey):
    dfs = []
    for adcode in areaname_dict:
        temp_df = get_df(adcode,APIkey,areaname_dict)
        dfs_times.append(temp_df)
    area_df = pd.concat(dfs_dict)
    dfs.append(area_df)
    return dfs

dfs = get_dfs(areaname_dict,APIkey)