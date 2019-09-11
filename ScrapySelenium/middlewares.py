# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
import time
from ScrapySelenium import settings

class SeleniumMiddlewares():
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser,10)
        # 将cookies转化为字典形式
        self.cookie = {i.split('=')[0]:i.split('=')[1] for i in settings.COOKIES.split(';')}

    def process_request(self,request,spider):
        # 获取当前页
        page = request.meta.get('page')
        try:
            self.browser.get(request.url)
            self.browser.delete_all_cookies()
            for name,value in self.cookie.items():
                cookie = {
                    'domain':'.taobao.com',
                    'name':name.strip(),
                    'value':value,
                }
                self.browser.add_cookie(cookie)
            # 携带cookie再次请求
            self.browser.get(request.url)
            if page > 1:
                input = self.wait.until(
                    EC.presence_of_element_located((By.XPATH,"//div[@id='mainsrp-pager']//div[@class='form']//input"))
                )
                submit = self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager div.form > span.btn.J_Submit')))
                input.clear()
                input.send_keys(page)
                submit.click()
                # 等待翻转页码成功（当前页码高亮）
                self.wait.until(
                    EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager li.item.active > span'),str(page)))
                # 等待出现商品列表
                self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,'.m-itemlist .items .item'))
                )
            # 返回page_source
            return HtmlResponse(
                url=request.url,
                body=self.browser.page_source,
                request=request,
                encoding='utf-8',
                status=200
            )
        except TimeoutException:
            return HtmlResponse(
                url=request.url,
                status=500,
                request=request
            )