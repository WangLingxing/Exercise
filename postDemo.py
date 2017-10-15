#-*-coding:utf-8-*-
import requests

payload = {"wlx":"Hello World","python":"2.7.10"}

r = requests.post("http://httpbin.org/post",data=payload)

print r.text

