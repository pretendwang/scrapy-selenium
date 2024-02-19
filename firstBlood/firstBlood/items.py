# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstbloodItem(scrapy.Item):
    job_id = scrapy.Field()
    company_id= scrapy.Field()
    company_url = scrapy.Field()
    job_title = scrapy.Field()  # 公司名称
    job_salary = scrapy.Field()  # 公司规模
    job_time = scrapy.Field()  # 公司地址
    job_url = scrapy.Field()  # 职位名称
    job_place = scrapy.Field()  # 薪酬
    job_exp = scrapy.Field()  # 职位描述、详情要求
    job_edu = scrapy.Field()  # 工作经验
    job_well = scrapy.Field()  # 学历要求
    company_name = scrapy.Field()  # 发布页面
    company_mag = scrapy.Field()  # 发布页面
    company__type = scrapy.Field()  # 发布页面
