# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field


from scrapy import Item, Field




class SearchItem(scrapy.Item):
    created_at=Field()
    id=Field()
    source=Field()
    text=Field()
    comments_count=Field()
    gender=Field()
    screen_name=Field()
    profile_image_url=Field()
    # 添加
    title = Field()
    transmit=Field()
    follow=Field()

class CommentItem(scrapy.Item):
    created_at=Field()
    like_count=Field()
    text=Field()
    gender=Field()
    id=Field()
    profile_image_url=Field()
    screen_name=Field()
    title=Field()


