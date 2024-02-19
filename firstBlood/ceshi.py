from selenium import webdriver
import time
from selenium.webdriver.common.by import By

chorme_path = r'E:/Python/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chorme_path)
driver.get('https://we.51job.com/pc/search?keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&searchType=2&sortType=0&metro=')
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(3)
def ceshi():
    x1=driver.find_element(By.CLASS_NAME,'number.active').text
    for i in range(0,3):
        button = driver.find_element(By.CLASS_NAME,'btn-next')
        button.click()
        time.sleep(3)
    # button = driver.find_element(By.CLASS_NAME,'btn-next')
    # button.click()
    # time.sleep(3)
    x=driver.find_element(By.CLASS_NAME,'number.active').text
    print(x1,x)
    time.sleep(30)
    # print(len(['<li class="number active">1</li>']))
def ceshi2():
    print('520')
