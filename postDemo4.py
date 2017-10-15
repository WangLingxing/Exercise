#-*-coding:utf-8-*-

import requests

h = {"Content-Type":"application/x-www-form-urlencoded"}
payload = {"loginName":"15267165820","password":"souche2015"}

s = requests.session()
r = s.post("http://dfc.souche.com/rest/account/login",params = payload, headers = h)

print r.json()