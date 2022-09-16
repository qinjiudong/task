# coding:utf8
import requests

url = 'http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp'
response = requests.get(url).json()
t = response['data']['t']

print(t)
print(123456)