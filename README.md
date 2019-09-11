# ScrapySelenium
## scrapy结合selenium对淘宝进行抓取
### 抓取逻辑
> 由scrapy先发起初始请求，并且记录页数。请求由调度器传给下载器的过程中，通过设置下载中间件，将请求交由selenium来进行处理，包括登陆和获取网页源码。最后返回response给
  item进行解析
