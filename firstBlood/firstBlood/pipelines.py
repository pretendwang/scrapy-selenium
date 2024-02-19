# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
# 打印logging日志
import logging

logger = logging.getLogger(__name__)


# 日志输出打印
class Job51Pipeline:
    def process_item(self, item, spider):

        # 连接MySQL数据库
        connect = pymysql.connect(host='localhost', user='root', password='123456', db='test2', port=3306,
                                  charset="utf8")
        print(connect)
        cursor = connect.cursor()
        job_id=item["job_id"]
        job_title=item["job_title"]
        job_salary=item["job_salary"]
        job_time=item["job_time"]
        job_url=item["job_url"]
        job_place=item["job_place"]
        job_exp=item["job_exp"]
        job_edu=item["job_edu"]
        job_well=str(item["job_well"])
        company_id=item["company_id"]
        company_name=item["company_name"]
        company_url=item["company_url"]
        company__type=item["company__type"]
        company_mag=item["company_mag"]
        item_list=[]
        item_list.append((
            job_id,job_title, job_salary, job_url, job_time, job_place, job_exp, job_edu, job_well,company_id, company_name,company_url,company__type, company_mag))
        # 往数据库里面写入数据
        try:

            sql = "insert into scrapy_job values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.executemany(sql, tuple(item_list))
            connect.commit()
        except Exception as error:
            # 出现错误时打印错误日志
            logging.warning(error)

        # 关闭数据库

        cursor.close()
        connect.close()

        return item
