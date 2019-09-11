# ScrapySelenium
## scrapy结合selenium对淘宝进行抓取
### 抓取逻辑
> 由scrapy先发起初始请求，并且记录页数。请求由调度器传给下载器的过程中，通过设置下载中间件，将请求交由selenium来进行处理，包括登陆和获取网页源码。最后返回response给spider进行解析。
注意：由于下载中间件返回了response，所以会跳过下载中间件将request传递给下载器这个步骤，直接将response传递给了spider
### 登陆
> 通过调度器发送过来的request得到url，selenium先发送一次请求，然后清空cookies。接下来添加登陆过后的cookies，然后再次请求就可以实现自动登陆。
### 登陆时遇到的坑
- 使用selenium的`add_cookie()`进行登陆模拟的时候，一定要先`browser.get(url)`请求一次，不然无法添加cookie。
- 添加`cookie = {'adomin':'.taobao.com','name':name.strip(),'value':value}`其中`adomin`是·`.taobao.com`如果写成`taobao.com`抓取为空
- 由于是直接用推导式构造的cookie字典`{i.split('=')[0]:i.split('=')[1] for i in settings.COOKIES.split(';')}`所以`name`会存在空格，如果不消除
空格的话，会报不能设置cookie的错误`WebDriverException: Message: unable to set cookie`
