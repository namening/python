#7.18.1强密码匹配
import re
#匹配8个字符以上
password=re.compile(r'\w{8,}')
text=password.findall('adkokkl\nsdfsdfsfsdfd\n\asdflkS2s\nadlkGooslf\nadadflsdf\nsadfasdf8adf\nAadsflkj\nasdflkjioasdfAAA9\nADFJAaKF7\n')
text='\n'.join(text)
#至少一个数字
password=re.compile(r'.*\d+.*')
text=password.findall(text)
text='\n'.join(text)
#至少一个小写字母
password=re.compile(r'.*[a-z]+.*')
text=password.findall(text)
text='\n'.join(text)
#至少一个大写字母
password=re.compile(r'.*[A-Z]+.*')
text=password.findall(text)
print('the following is the strong password:')
for i in text:
    print(i)
