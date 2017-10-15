#!/usr/bin/env python
#-*-coding:utf-8-*-

import requests
import time

h = {"Content-Type":"application/x-www-form-urlencoded"}
payload = {"loginName":"15267165820","password":"souche2015"}

s = requests.session()
r = s.post("http://dfc.sqaproxy.souche.com/rest/account/login",params = payload, headers = h)
j = r.json()
t = j['data']['token']
print t
time.sleep = 2
params = {"token":t, "province":"00974","city":"00975","region":"330110","platform":"58", "account":"test01","password":"test"}
response = s.post("http://shop.sqaproxy.souche.com/pc/synchronous/platformaccountsaction/saveBindAccounts.json",headers = h, params = params)
status = response.status_code
print status
time.sleep = 2
result = response.json()
data = result['data']
print result
print data
print data['id']

logout = s.post("http://app.prepub.souche.com/rest/account/logout",params = payload, headers = h)

