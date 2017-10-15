#-*-coding:utf-8-*-

import requests

h = {"Content-Type":"application/x-www-form-urlencoded"}
payload = {"loginName":"15267165820","password":"souche2015"}

r = requests.post("http://dfc.souche.com/rest/account/login",params = payload, headers = h)
j = r.json()

print r.status_code
print j['success']
print r.text




