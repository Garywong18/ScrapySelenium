# -*- coding: utf-8 -*-

# Scrapy settings for ScrapySelenium project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ScrapySelenium'

SPIDER_MODULES = ['ScrapySelenium.spiders']
NEWSPIDER_MODULE = 'ScrapySelenium.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'ScrapySelenium.middlewares.ScrapyseleniumSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'ScrapySelenium.middlewares.SeleniumMiddlewares': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'ScrapySelenium.pipelines.ScrapyseleniumPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MAX_PAGE = 100
KEYWORDS = 'ipad'
COOKIES = 'cna=3dZ2FP071m8CAbSq12IcxR7y; miid=832751451142794490; tracknick=%5Cu5E7B%5Cu60F3%5Cu732B11; tg=0; thw=cn; enc=ajaj81fZaZibv0FQK5G8pe%2FLjLG2xqxnc%2FC6ju8uKopySiZtxs2A72VCd1e8W0GBkpl9yizZHoxIZs0WnrpizQ%3D%3D; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; hng=CN%7Czh-CN%7CCNY%7C156; t=ab16ace798f92aeaf0882ba83d9ca1f3; _cc_=VFC%2FuZ9ajQ%3D%3D; v=0; cookie2=1a8a16b6d83845632484abc32f6a8d3b; _tb_token_=e3aed7e85e3d1; JSESSIONID=C70F2635550DC8F8C6BDC91E382A4360; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; mt=ci%3D-1_0; isg=BKSkE43jpWB8YNeqRLm9n25bdaJWlcmvqQUZZ77FMG8yaUQz5k2YN9rALYFUsQD_; l=cBjk33Lnv4qeON1KBOCgCuI8Ls_OSIRAguPRwC0Mi_5QJ6T_LK_Okz0fJF96VjWdtYYB4JuaUMv9-etk9SeL58pRWkvP'