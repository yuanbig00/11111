# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
from logging import log
import re

import MySQLdb
import pymysql
import redis
import pandas as pd
from bs4 import BeautifulSoup
from weiboziji.spiders.util import  title_conent

from weiboziji.items import SearchItem

class MySQL3TopicPipeline:
  def open_spider(self, spider):
      db = spider.settings.get('MYSQL_DB_NAME', 'user')
      host = spider.settings.get('MYSQL_HOST', 'localhost')
      port = spider.settings.get('MYSQL_PORT', 3306)
      user = spider.settings.get('MYSQL_USER', 'root')
      passwd = spider.settings.get('MYSQL_PASSWORD', 'root')
      self.db_conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
      self.db_cur = self.db_conn.cursor()




  def insert_db(self, item):

      #输入
      values2=(item['created_at'], item['like_count'],item['text'],item['gender'],item['id'],item['profile_image_url'],item['screen_name'] )
      sql2 = 'INSERT INTO comment(created_at,like_count,text,gender,id,profile_image_url,screen_name)VALUES (%s,%s,%s,%s,%s,%s,%s)'
      self.db_cur.execute(sql2, values2)

  def close_spider(self, spider):
       self.db_conn.commit()
       self.db_cur.close()
       self.db_conn.close()



#去除url
  def removeurl(self,urlline):
      results = re.compile(r'http://[a-zA-Z0-9.?/&=:]*', re.S)
      dd = results.sub("", urlline)
      return dd
  #去除@
  def removepeople(self,peopleline):
      pattern = peopleline.split("//@")
      outputline = ""
      for name in pattern:
          name = name.split(":")[-1]
          outputline += name
      return outputline
  #去除标点符号
  def puncfilter(self,line):
      r1 = u'[’!"#$%&\'()*+,-./:;<=>?@；；：．｜～\≧▽—°×▲●巜「」／↓→<=>?@⁄•ω★·、…★、​…【】《》『』（）？“”‘’！[\\]^_`{|}~]+'
      return re.sub(r1, '', line)
  #预处理,改过
  #预处理,改过
  def process_item(self, item, spider):
      now_time = datetime.datetime.now()
      today = datetime.date.today()  # 今天
      rating = item.get('created_at')
      content=item.get('text')
      soup = BeautifulSoup(content, "html.parser")
      contentPretty = ""
      for string in soup.stripped_strings:
          contentPretty += string

      contentPretty = self.removepeople(contentPretty)
      contentPretty = self.removeurl(contentPretty)
      contentPretty = self.puncfilter(contentPretty)

      item['text']=contentPretty
      self.insert_db(item)
      print("结果2是", item)
      return item


class MySQL2TopicPipeline:
  def open_spider(self, spider):
      db = spider.settings.get('MYSQL_DB_NAME', 'user')
      host = spider.settings.get('MYSQL_HOST', 'localhost')
      port = spider.settings.get('MYSQL_PORT', 3306)
      user = spider.settings.get('MYSQL_USER', 'root')
      passwd = spider.settings.get('MYSQL_PASSWORD', 'root')
      self.db_conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
      self.db_cur = self.db_conn.cursor()

  def close_spider(self, spider):
       self.db_conn.commit()
       self.db_cur.close()
       self.db_conn.close()

  def insert_db(self, item):
      values = (item['created_at'], item['id'],item['source'],item['text'],item['comments_count'],item['gender'],item['screen_name'],item['profile_image_url'],item['title'],item['transmit'],item['follow'])
      sql = 'INSERT INTO user(created_at,id,source,text,comments_count,gender,screen_name,profile_image_url,title,transmit,follow)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
      self.db_cur.execute(sql, values)
      #输入
      # values2=(item['created_at'], item['like_count'],item['text'],item['gender'],item['id'],item['profile_image_url'],item['screen_name'] )
      # sql2 = 'INSERT INTO comment(created_at,like_count,text,gender,id,profile_image_url,screen_name )VALUES (%s,%s,%s,%s,%s,%s,%s)'
      # self.db_cur.execute(sql2, values2)


  def removeurl(self, urlline):
      results = re.compile(r'http://[a-zA-Z0-9.?/&=:]*', re.S)
      dd = results.sub("", urlline)
      return dd
      # 去除@

  def removepeople(self, peopleline):
      pattern = peopleline.split("//@")
      outputline = ""
      for name in pattern:
          name = name.split(":")[-1]
          outputline += name
      return outputline
      # 去除标点符号

  def puncfilter(self, line):
      r1 = u'[’!"#$%&\'()*+,-./:;<=>?@；；：．｜～\≧▽—°×▲●巜「」／↓→<=>?@⁄•ω★·、…★、​…【】《》『』（）？“”‘’！[\\]^_`{|}~]+'
      return re.sub(r1, '', line)
      # 预处理

  def process_item(self, item, spider):
      now_time = datetime.datetime.now()
      today = datetime.date.today()  # 今天
      rating = item.get('created_at')
      content = item.get('text')
      soup = BeautifulSoup(content, "html.parser")
      contentPretty = ""
      for string in soup.stripped_strings:
          contentPretty += string

      contentPretty = self.removepeople(contentPretty)
      contentPretty = self.removeurl(contentPretty)
      contentPretty = self.puncfilter(contentPretty)
      title = title_conent(contentPretty)
      item['title'] = title
      item['text'] = contentPretty
      self.insert_db(item)
      print("结果2是", item)


class RemoveReDoPipline(object):
    def __init__(self, host):

        self.conn = MySQLdb.connect(host, 'root', 'root', charset="utf8", use_unicode=True)
        self.redis_db = redis.Redis(host='127.0.0.1', port=6379, db=0)
        sql = "SELECT id FROM  user"
        # 获取全部的id,这是区分是不是同一条微博的标识
        df = pd.read_sql(sql, self.conn)
        # 全部放入Redis中
        for mid in df['d'].get_values():
            self.redis_db.sadd("id", id)

    # 获取setting文件配置
    @classmethod
    def from_settings(cls, setting):
        host = setting["MYSQL_HOST"]
        return cls(host)

    def process_item(self, item, spider):
        # 只对微博的Item过滤，微博评论不需要过滤直接return：
        if isinstance(item, SearchItem):
            if self.redis_db.sadd("id", item["id"]):
                return item
            else:
                print("重复内容：", item['text'])
                raise SearchItem ("same title in %s" % item['text'])
        else:
            return item

