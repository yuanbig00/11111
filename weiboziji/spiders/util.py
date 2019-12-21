#!/usr/bin/env python
# encoding: utf-8
import re
import datetime
import time
#时间规范化
from snownlp import SnowNLP
def time_fix(time_string):
    now_time = datetime.datetime.now()
    today = datetime.date.today()  # 今天
    if '刚刚' in time_string:
        created_at = now_time
        return created_at.strftime('%Y-%m-%d %H:%M')
    if '分钟前' in time_string:
        minutes = re.search(r'^(\d+)分钟', time_string).group(1)
        created_at = now_time - datetime.timedelta(minutes=int(minutes))
        return created_at.strftime('%Y-%m-%d %H:%M')
    if '小时前' in time_string:
        minutes = re.search(r'^(\d+)小时', time_string).group(1)
        created_at = now_time - datetime.timedelta(hours=int(minutes))
        return created_at.strftime('%Y-%m-%d %H:%M')
    if '昨天' in time_string:
        yesterday = today - datetime.timedelta(days=1)
        return time_string.replace('昨天',  datetime.date.strftime(yesterday, '%Y-%m-%d'))

    if '今天' in time_string:
        return time_string.replace('今天', now_time.strftime('%Y-%m-%d'))

    if '月' in time_string:
        time_string = time_string.replace('月', '-').replace('日', '')
        time_string = str(now_time.year) + '-' + time_string
        return time_string

    if '\d{1,2}-\d{1,2}' in time_string:
        time_string.Format("yyyy-MM-dd hh:mm:ss")
        time_string=time_string.replace('\d{1,2}-\d{1,2}','2019-\d{1,2}-\d{1,2}')
    if '(Mon|Tues|Wed|Thur|Fri|Sat|Sun)\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec)\s+\d\d\s+\d\d:\d\d:\d\d\s+CST\s+\d\d\d\d' in time_string:
        time_string=time_string.Format("yyyy-MM-dd hh:mm:ss")
        print('ok')
    else:
        print('error')

    return time_string

#格林时间格式的转换
def trans_format(time_string, from_format, to_format='%Y.%m.%d %H:%M:%S'):
    time_struct = time.strptime(time_string, from_format)
    times = time.strftime(to_format, time_struct)
    return times

 # pubtime = 'Sun Sep 30 17:12:21 +0800 2018'
  # 4-9是把前面的星期抹去，26-30是把年提前，11-19是把具体时间接上


# time_string = 'Feb 01 2017 23:00:12'  # 中国标准时间更长，更全面，手动就是纯粹的截取字符串
# times = trans_format(time_string, '%b %d %Y %H:%M:%S', '%Y-%m-%d %H:%M:%S')


#性别转化
def gender_content(gender_string):
    if 'm' in gender_string:
        gender_string=gender_string.replace('m','男')
    if 'f' in gender_string:
        gender_string=gender_string.replace('f','女')
    return gender_string
# 去除文章中的a标签和image标签和br标签和空格
def text_content(text_string):
    if '<a (.*?)>' in text_string:
        text_string=text_string.replace('<a (.*?)>','')
    if '<a href=(.*?)>|</a>' in text_string:
        text_string=text_string.replace('<a href=(.*?)>|</a>','')
    if '<img alt="|" src="(.*?)/>' in text_string:
        text_string=text_string.replace('<img alt="|" src="(.*?)/>','')
    if '<br>' in text_string:
        text_string=text_string.replace('<br>','')
    if '<span (.*?)>' in text_string:
        text_string=text_string.replace('<span (.*?)>','')
    if '\s+' in text_string:
        text_string=text_string.replaceAll('\s+','')
    return text_string

#在文章中找标题
def title_conent(text_string):
    s = SnowNLP(text_string)
    # text_string=s.summary(limit=6)
    text_string=s.keywords(limit=4)
    list2 = [str(i) for i in text_string]
    list3 = ''.join(list2)
    # list3.strip()#去除首位的空格
    # list3.replace(" ", "")

    return list3




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





# str1=('科技客户端发开始交互发的是姐夫和萨克符合')
# s=SnowNLP(str1)
# h=s.keywords()
# m=SnowNLP(h)
# k=m.idf
# print(h)
# print(k)

























keyword_re = re.compile('<span class="kt">|</span>|原图|<!-- 是否进行翻译 -->|')
emoji_re = re.compile('<img alt="|" src="//h5\.sinaimg(.*?)/>')
white_space_re = re.compile('<br />')
div_re = re.compile('</div>|<div>')
image_re = re.compile('<img(.*?)/>')
url_re = re.compile('<a href=(.*?)>|</a>')







def extract_weibo_content(weibo_html):
    s = weibo_html
    if '转发理由' in s:
        s = s.split('转发理由:', maxsplit=1)[1]
    if 'class="ctt">' in s:
        s = s.split('class="ctt">', maxsplit=1)[1]
    s = s.split('赞', maxsplit=1)[0]
    s = keyword_re.sub('', s)
    s = emoji_re.sub('', s)
    s = url_re.sub('', s)
    s = div_re.sub('', s)
    s = image_re.sub('', s)
    if '<span class="ct">' in s:
        s = s.split('<span class="ct">')[0]
    s = white_space_re.sub(' ', s)
    s = s.replace('\xa0', '')
    s = s.strip(':')
    s = s.strip()
    return s


def extract_comment_content(comment_html):
    s = comment_html
    if 'class="ctt">' in s:
        s = s.split('class="ctt">', maxsplit=1)[1]
    s = s.split('举报', maxsplit=1)[0]
    s = emoji_re.sub('', s)
    s = keyword_re.sub('', s)
    s = url_re.sub('', s)
    s = div_re.sub('', s)
    s = image_re.sub('', s)
    s = white_space_re.sub(' ', s)
    s = s.replace('\xa0', '')
    s = s.strip(':')
    s = s.strip()
    return s