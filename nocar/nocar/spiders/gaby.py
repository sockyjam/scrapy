# -*- coding: utf-8 -*-
import scrapy
from nocar.items import NocarItem

class GabySpider(scrapy.Spider):
    name = 'gaby'
    allowed_domains = ['wallpaper.desktx.com']
    start_urls = ['http://wallpaper.desktx.com/scenery/',
    'http://wallpaper.desktx.com/animals/',
    'http://wallpaper.desktx.com/animals/index_2.html',
    'http://wallpaper.desktx.com/animals/index_3.html',
    'http://wallpaper.desktx.com/animals/index_4.html',
    'http://wallpaper.desktx.com/construction/',
    'http://wallpaper.desktx.com/sports/',
    'http://wallpaper.desktx.com/sports/index_2.html',
    'http://wallpaper.desktx.com/sports/index_3.html',
    'http://wallpaper.desktx.com/sports/index_4.html',
    'http://wallpaper.desktx.com/meishi/',
    'http://wallpaper.desktx.com/meishi/index_2.html',
    'http://wallpaper.desktx.com/meishi/index_3.html',
    'http://wallpaper.desktx.com/meishi/index_4.html',
    'http://wallpaper.desktx.com/People/females/',
    'http://wallpaper.desktx.com/People/females/index_2.html',
    'http://wallpaper.desktx.com/People/males/',
    'http://wallpaper.desktx.com/People/males/index_2.html',
    'http://wallpaper.desktx.com/plant/',
    'http://wallpaper.desktx.com/space/',
    'http://wallpaper.desktx.com/space/index_2.html',
    'http://wallpaper.desktx.com/space/index_3.html',
    'http://wallpaper.desktx.com/space/index_4.html',
    ]

    def parse(self, response):
        item = NocarItem()

        imgdivs = response.xpath("//div[@class='img_list']")
        # aa = response.xpath("//ul[@id='picList1']")
        # lis = imgdiv.xpath("./a")
        # print("------", imgdivs, len(imgdivs))
        urls_list = []
        for pic in imgdivs:
            urls = pic.xpath(".//div[@class='pic_zs']/a/img/@src").getall()
            # print("======", lis)
            urls_list = urls

        item['urls_list'] = urls_list


        # for urlbox in urlboxes:
        #     item = NocarItem()

            #拿到所有的分类中文名
            # catgory_title = urlbox.xpath(".//div[@class='uibox-title']/a/text()").get()

            # item['catgory_title'] = catgory_title
            # #再获取每个分类下面的所有图片链接
            # image_urls = urlbox.xpath(".//ul/li/a/img/@src").getall()
            # urls_list = []
            # for url in image_urls:
            #     #url = "https:" + url
            #     url = response.urljoin(url)
            #     urls_list.append(url)
            # item['urls_list'] = urls_list
        yield item

