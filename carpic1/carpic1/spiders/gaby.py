# -*- coding: utf-8 -*-
import scrapy
from carpic1.items import Carpic1Item

class GabySpider(scrapy.Spider):
    name = 'gaby'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html#pvareaid=3454438']

    def parse(self, response):
        urlboxes = response.xpath("//div[@class='uibox']")[1:]
        for urlbox in urlboxes:
            item =Carpic1Item()
            #拿到所有的分类中文名
            catgory_title = urlbox.xpath(".//div[@class='uibox-title']/a/text()").get()
            if
            item['catgory_title'] = catgory_title
            #再获取每个分类下面的所有图片链接
            image_urls = urlbox.xpath(".//ul/li/a/img/@src").getall()
            urls_list = []
            for url in image_urls:
                #url = "https:" + url
                url = response.urljoin(url)
                urls_list.append(url)
            item['urls_list'] = urls_list
            yield item
