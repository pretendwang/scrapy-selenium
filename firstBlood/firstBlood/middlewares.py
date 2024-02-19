# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random
from selenium import webdriver
from selenium.common import TimeoutException

from .settings import USER_AGENT_LIST
from .settings import PROXY_LIST
import time,random
from scrapy.http import HtmlResponse
from selenium.webdriver.common.by import By

class RandomUserAgent(object):
    def process_request(self, request, spider):
        ua = random.choice(USER_AGENT_LIST)
        request.headers['User-Agent'] = ua
        print(request.headers['User-Agent'])


# class RandomProxy(object):
#     def process_request(self, request, spider):
#         proxy = random.choice(PROXY_LIST)
#         request.meta['proxy'] = 'https://'+proxy['ip_port']
#         print(request.meta)

#结合
class JobdownloadMiddleware:
    def __init__(self):
        # 创建一个driver对象
        chorme_path = r'E:/Python/chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=chorme_path)

    def process_request(self, request, spider):
        # 在这个方法中通过driver访问第一个链接
        self.driver.get(request.url)
        time.sleep(3)
        # 获取page_source,再把源代码传递给爬虫parse方法的reponse对象
        data = self.driver.page_source
        # print(data)
        # global x
        # x=int(self.driver.find_element(By.CLASS_NAME, 'number.active').text)
        print(request.meta['page'])
        if int(request.meta['page']) == 2:
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
            x=request.meta['page_num']
            print(x)
            for i in range(0,x):
                button = self.driver.find_element(By.CLASS_NAME, 'btn-next')
                button.click()
                time.sleep(4)
            # x = int(self.driver.find_element(By.CLASS_NAME, 'number.active').text)
            print(x)
            data = self.driver.page_source
        else:
            if int(request.meta['page']) == 0:
                try:
                    print('url is :::', request.url)
                    self.driver.get(request.url)
                except TimeoutException as e:
                    print('超时')
                time.sleep(5)
        print(self.driver.current_url)
        # print(data)
        return HtmlResponse(url=request.url,body=data,request=request,encoding='utf-8')
