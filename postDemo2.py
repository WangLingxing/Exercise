#-*-coding:utf-8-*-

import requests
import json

payload = {"wlx":"Hello World","python":"2.7.10"}

#转换为json
data_json = json.dumps(payload)
r = requests.post("http://httpbin.org/post",data = data_json)
print r.text