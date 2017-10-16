import re
line='''我的电子邮件tom@gmail.com. 
将什么发送到jerry123@163.com或者3123432@qq.com.
若遇特殊情况打电话给182123445678.'''
a=re.search(r'[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+',line,re.A)
print('邮箱1：',a)
c=re.search(r'[\w-]+(\.[\w-]+)*@?163.com',line,re.A)
print('邮箱2：',c)
d=re.search(r'[\w-]+(\.[\w-]+)*@?qq.com',line,re.A)
print('邮箱3：',d)
b=re.search(r'(\d+){12}',line)
print('电话号码：',b)
