import json

import scrapy
import urllib.parse
import re
from ..items import FirstbloodItem
from myApp.admin import keyword
from copy import deepcopy
import time
x=0
count=0
class JobSpider(scrapy.Spider):
    name = 'first'
    allowed_domains = ['search.51job.com']
    job_name = input("请输入岗位：")
    keyword = urllib.parse.quote(job_name)
    # 岗位解析后的代 码
    # keyword = urllib.parse.quote(keyword)
    def start_requests(self):
        start_urls = ['http://search.51job.com/']

        # 页数
        # start_urls = f'https://search.51job.com/list/000000,000000,0000,00,9,99,{keyword},2,1.html?'
        # start_urls = ['https://we.51job.com/pc/search?jobArea=010000&keyword=python%E7%88%AC%E8%99%AB&searchType=2&sortType=0&metro=']
        # 生成url
        url_pre = f'https://we.51job.com/pc/search?keyword={keyword}&searchType=2&sortType=0&metro='
        start_urls = url_pre
        yield scrapy.Request(url=start_urls, callback=self.parse, dont_filter=True, meta={'page': '0'})
    def parse(self, response):
        item=FirstbloodItem()
        # print(response)
        # print(response.text)
        joblist = response.xpath('//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div')
        # item['company_id']=
    #     # print(joblist)
        global count
        count += 280
        global x
        x=x+1
        print(x)
        page_next = response.css('.number').extract()
        print(page_next)
        for pro in joblist:
            item['job_title'] = pro.xpath('./a/div/span[1]/text()').extract_first()
            item['job_salary']=pro.xpath('./a/p[1]/span[1]/text()').extract_first()
            item['job_time'] = pro.xpath('./a/div/span[2]/text()').extract_first()
            item['job_url'] = pro.xpath('./a/@href').extract_first()
            b = re.compile('\d+(?:\.\d+)?')
            item['job_id']=re.findall(b,item['job_url'])[1]
            # print(item['job_id'])
            item['job_place'] = pro.xpath('./a/p[1]/span[2]/span[1]/text()').extract_first()
            item['job_exp'] = pro.xpath('./a/p[1]/span[2]/span[3]/text()').extract_first()
            item['job_edu'] = pro.xpath('./a/p[1]/span[2]/span[5]/text()').extract_first()
            item['job_well'] = pro.xpath('./a/p[2]/span/i/text()').extract()
            item['company_name'] = pro.xpath('./div[2]/a/text()').extract_first()
            item['company_url']=pro.xpath('./div[2]/a/@href').extract_first()
            c=re.compile('all/(.*).html')
            if len(re.findall(c,item['company_url']))!=0:
                item['company_id']=re.findall(c,item['company_url'])[0]
            else:
                item['company_id']=None
            item['company_mag'] = pro.xpath('./div[2]/p[1]/text()').extract_first()
            item['company__type'] = pro.xpath('./div[2]/p[2]/text()').extract_first()
            # print(item)
            # print("爬取第{}条数据".format(id))
            yield item
            # yield item
        if len(page_next) > 1:
            if x<50:
                # 当数据>300可以让翻页暂停等待数据下载
                if count > 280:
                    time.sleep(0.5)
                # 使用selenium模拟点击下一页，该请求不会产生实质的下载动作
                yield scrapy.Request(url=response.url, callback=self.parse, meta={'page': '2','page_num' : x}, dont_filter=True)

    # def parse_details(self, response):
    #             # 数据每下载一条,count - 1
    #             global count
    #             count -=1
    #             item=response.meta['item']
    #             print(item)
    #             yield item