# -*- coding: utf-8 -*-


# weibo.py
#
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

from weiboziji.items import   SearchItem, CommentItem
import re
import json
import re

import scrapy
from scrapy import Request
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings

from weiboziji.spiders.util import time_fix, text_content, gender_content,trans_format,title_conent
import time
user_id=0

class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['m.weibo.cn']
    start_urls = ['http://m.weibo.cn/']
    #100103type=1&q=火灾
    #100103type=1&q=地震
    #100103type%3D1%26q%3D%E5%9C%B0%E9%9C%87
    #https://m.weibo.cn/comments/hotflow?id=4447610590672451&mid=4447610590672451&max_id_type=0
    # url='https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%E5%9C%B0%E9%9C%87&page_type=searchall&page=2'
    search_url='https://m.weibo.cn/api/container/getIndex?containerid={containerid}&page_type=searchall&page={page}'
    comment_url='https://m.weibo.cn/comments/hotflow?id={id}&mid={id}&max_id_type=0'
    key_containerid='100103type=1&q=地震'
    start_page=1


      # 初始请求的事件
    def start_requests(self):
        for i in range(1,100):
            start_page=i
            yield Request(self.search_url.format(containerid=self.key_containerid, page=i),
                          callback=self.searchparse)

    def searchparse(self, response):
        results = json.loads(response.text)
        # print(results)
        for n in range(9):
            a = results["data"]["cards"][3]["mblog"]["created_at"]
            print("测试数据a:" + a)
            created_at1 = results["data"]["cards"][n]["mblog"]["created_at"]
            created_at =time_fix(created_at1)
            id = results["data"]["cards"][n]["mblog"]["id"]
            source = results["data"]["cards"][n]["mblog"]["source"]
            text1 = results["data"]["cards"][n]["mblog"]["text"]
            text = text_content(text1)
            comments_count = results["data"]["cards"][n]["mblog"]["comments_count"]
            gender1 = results["data"]["cards"][n]["mblog"]["user"]["gender"]
            gender = gender_content(gender1)
            screen_name = results["data"]["cards"][n]["mblog"]["user"]["screen_name"]
            profile_image_url = results["data"]["cards"][n]["mblog"]["user"]["profile_image_url"]
            transmit=results["data"]["cards"][n]["mblog"]["reposts_count"]
            follow=results["data"]["cards"][n]["mblog"]["attitudes_count"]

            title=title_conent(text)
            global user_id
            user_id= id
            # time.sleep(2)
            print("文章内容输出")
            print(created_at)
            print(id)
            print(source)
            print(text)
            print(gender)
            print(profile_image_url)
            print(comments_count)
            print(screen_name)
            print(title)
            print(transmit)
            print(follow)
            searchitem = SearchItem()
            searchitem['created_at'] = created_at
            searchitem['id'] = id
            searchitem['source'] = source
            searchitem['text'] = text
            searchitem['comments_count'] = comments_count
            searchitem['gender'] = gender
            searchitem['screen_name'] = screen_name
            searchitem['profile_image_url'] = profile_image_url
            searchitem['title']=title
            searchitem['transmit']=transmit
            searchitem['follow']=follow


            print("跳转到达的id:" + id)
            yield searchitem
            if comments_count >= 1:
                print("跳转到评论页面")
                yield Request(self.comment_url.format(id=id, mid=id),
                              callback=self.commentparse)
        yield Request(self.search_url.format(containerid=self.key_containerid, page=self.start_page),
                      callback=self.searchparse)

    def commentparse(self, response):
        results = json.loads(response.text)
        # print(results)
        for i in range(19):
            print("评论输出")

            comment_created_at1 = results["data"]["data"][i]["created_at"]
            time_string = comment_created_at1[4:10] + ' ' + comment_created_at1[26:30] + ' ' + comment_created_at1[11:19]
            comment_created_at = trans_format(time_string, '%b %d %Y %H:%M:%S', '%Y-%m-%d %H:%M:%S')
            comment_like_count = results["data"]["data"][i]['like_count']
            comment_id=user_id
            # comment_id= results["data"]["data"][2]['id']
            comment_text1 = results["data"]["data"][i]['text']
            comment_text=text_content(comment_text1)
            comment_gender1 = results["data"]["data"][i]['user']["gender"]
            comment_gender=gender_content(comment_gender1)
            # comment_id = results["data"]["data"][i]["user"]["id"]
            comment_profile_image_url = results["data"]["data"][i]["user"]["profile_image_url"]
            comment_screen_name = results["data"]["data"][i]["user"]["screen_name"]
            # time.sleep(2)
            print('评论数据显示')
            print(comment_created_at)
            print(comment_id)
            print(comment_like_count)
            print(comment_text)
            print(comment_gender)
            print(comment_profile_image_url)
            print(comment_screen_name)
            commentitem = CommentItem()
            commentitem['created_at'] = comment_created_at
            commentitem['like_count'] = comment_like_count
            commentitem['gender'] =comment_gender
            commentitem['text'] = comment_text
            commentitem['id'] = comment_id
            commentitem['profile_image_url'] = comment_profile_image_url
            commentitem['screen_name'] = comment_screen_name
            yield commentitem

        yield Request(self.search_url.format(containerid=self.key_containerid, page=self.start_page),
                      callback=self.searchparse)





