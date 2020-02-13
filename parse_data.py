import pandas as pd
import urllib.request
import json

app_name="和平精英"
app_name=urllib.request.quote(app_name)

url="http://itunes.apple.com/search?term="+app_name+"&country=cn&entity=software&limit=1"
req=urllib.request.Request(url)
resp=urllib.request.urlopen(req)
result=resp.read().decode('utf-8')

json_ld = json.loads(result)['results'][0]
version=json_ld["version"]
releaseDate=json_ld["releaseDate"]
categories=json_ld["genres"]
print(releaseDate)
# data=pd.read_json('AppStore/appstore.json',encoding=None)
# print(data.loc[0,])