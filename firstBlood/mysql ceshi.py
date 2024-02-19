# import pymysql
import re
# connect = pymysql.connect(host='localhost', user='root', password='123456', db='test2', port=3306,
#                                   charset="utf8")
# print(connect)
# cursor = connect.cursor()
#
# connect.commit()
a='https://companyads.51job.com/companyads/2023/wx/wxxj/index.html'
b=re.compile('all/(.*).html')
print(re.findall(b,a))
if len(re.findall(b,a))!=0:
    job_id=re.findall(b,a)[0]
else:
    job_id=None
print(job_id)
