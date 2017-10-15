#-*-coding:utf-8-*-

import requests

h = {"Content-Type":"application/x-www-form-urlencoded"}
payload = {"loginName":"15267165820","password":"souche2015"}

s = requests.session()
r = s.post("http://dfc.souche.com/rest/account/login",params = payload, headers = h)

params = {"carId":"16c23473e66c45df8f629a4b25504b00","token":"1MmPb_ts61QQOLbk"}
s1 = requests.session()
r1 = s.post("http://erp-test.sqaproxy.souche.com/pc/car/carstockaction/operate.json",params = params, headers = h)
json1 = r1.json()
print json1

