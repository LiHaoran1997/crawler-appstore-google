import os
import requests
import json


def resolveJson(path):
    file = open(path,'r')
    fileJson = json.load(file)
    appid = fileJson[0]['app_id']
    return appid


appid=resolveJson('jsondata/appstore.json')
print(appid)
url='https://itunes.apple.com/lookup?id='+str(appid)
r = requests.get(url)
data=json.loads(r.text)
print(data)
language=data['results'][0]['languageCodesISO2A']
developer_contact=data['results'][0]['sellerUrl']
category=data['results'][0]['genres']
version=data['results'][0]['version']
print(data)
