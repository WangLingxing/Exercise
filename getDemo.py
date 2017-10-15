#-*-coding:utf-8-*-
import requests


r = requests.get("https://www.baidu.com/")

print r.url
print r.encoding
print r.content    #返回内容（自动解码gzip)
print r.headers
print r.cookies
