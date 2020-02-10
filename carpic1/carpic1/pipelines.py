# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import ssl

from urllib import request

class Carpic1Pipeline(object):
    def __init__(self):

        ssl._create_default_https_context = ssl._create_unverified_context
        #os.path.join(os.path.dirname(os.path.dirname(__file__)),'images')
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        else:
            print("已经存在文件夹")

    def process_item(self, item, spider):
        catgory_title = item['catgory_title']
        urls_list = item['urls_list']
        #创建一个当前分类的文件夹
        title_path = os.path.join(self.path,catgory_title)
        if not os.path.exists(title_path):
            os.mkdir(title_path)

        #文件夹创建完毕后，就将每一个图片放入到对应的文件夹下
        for url in urls_list:
            print(url)
            image_name = url.split("_")[-1]
            request.urlretrieve(url,os.path.join(title_path,image_name))
        return item
