'''
使用requests下载火狐浏览器
'''
import requests
url='https://download-ssl.firefox.com.cn/releases-sha2/stub/official/zh-CN/Firefox-latest.exe'
res=requests.get(url)
url=url.split('/')
name=url[len(url)-1]
downFile=open(name,'wb')
for i in res.iter_content(100000):
    downFile.write(i)
downFile.close()
