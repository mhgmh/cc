# -*- coding: utf-8 -*-
import scrapy
import json
import re
from ..items import CcItem


class CcspiSpider(scrapy.Spider):
    name = 'ccspi'
    allowed_domains = ['toutiao.com']
    start_urls = ['http://toutiao.com/']

    def parse(self, response):
        item_url = "http://www.baidu.com"
        f = open('keyword.txt',encoding='utf-8').read().split('\n')
        for key in f:
            url = "https://www.toutiao.com/search/?keyword="+key
            yield scrapy.Request(url,callback=self.Read_key,meta={'key':key})






    def Read_key(self,response):
        key = response.meta['key']
        for i in range(0,8):
            url = "https://www.toutiao.com/search_content/?offset="+str(i*20)+"&format=json&keyword={}&autoload=true&count=20&cur_tab=1&from=search_tab".format(key)
            headers = {
                'cookie':'tt_webid=6554563661830604302; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=16352d801092ac-0eb0a388034e86-33657f07-1fa400-16352d8010afee; tt_webid=6554563661830604302; uuid="w:a904362acac346dbb2b84c78fd6a868f"; sso_login_status=0; __tasessionId=jzofko4e61526271796330; CNZZDATA1259612802=102088705-1526101527-%7C1526270226',
                'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
                'x-requested-with':'XMLHttpRequest',
            }
            yield scrapy.Request(url,callback=self.Read_url,headers=headers,meta={'keys':key})


    def Read_url(self,response):
        print(response.url)
        f = json.loads(response.text)
        it = CcItem()
        content = f['data']
        data = []
        for li in content:
            try:
                print(li['id'],li['title'])
                url = "https://www.toutiao.com/a{}/".format(li['id'])
                it['key'] = response.meta['keys']
                data.append((li['title'],url))
                it['name'] = data
            except KeyError:
                print("暂无id")
        yield it




