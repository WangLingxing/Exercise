# -*-coding:utf-8-*-
import requests

url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-1202247993797-yunda.html"

headers = {"Content-Type":"text/html; Language=UTF-8"}

s = requests.session()
r = s.post(url, headers = headers, verify = False)

result = r.json()
print result
data = result["data"]

print data
print data[0]

get_result = data[0]['context']
print get_result

if u"签收" in get_result:
	print "收到快递"
else:
	print "未签收"
