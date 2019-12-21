#标签以及重要性
import MySQLdb
from snownlp import SnowNLP
# -*- coding: utf-8 -*-
import pandas as pd
import pymysql
import numpy as np
def dic2sql(pos,neo,neu,sql):
    sf = ''
    tup = (pos, neo, neu)
    sf += (str(tup) + ',')
    sf = sf.rstrip(',')
    sql2 = sql % sf
    return sql2
from wordcloud import WordCloud, STOPWORDS
dbconn = pymysql.connect(
    host="localhost",
    database="user",
    user="root",
    password="root",
    port=3306,
    charset='utf8'
)

# sql语句

# 利用pandas 模块导入mysql数据
cursor_fetch=dbconn.cursor()

sqlcmd2='select  id  from  comment '
b=pd.read_sql(sqlcmd2,dbconn)
# print(b)
id=np.unique(b)
sentiments_out = []

dic = {}
for i in range(len(id)):
    sqlcmd = "select text from comment where id=%s"
    cursor_fetch.execute(sqlcmd, id[i])
    results = cursor_fetch.fetchall()
    one=id[i]
    pos = 0
    neu = 0
    neg = 0

    try:
        for n in range(len(results)):
            str2 = results[n][0]
            s = SnowNLP(str2)
            sentiments_out.append(s.sentiments)
            # print(s.sentiments)
            if s.sentiments > 0.8:
                pos = pos + 1
            elif s.sentiments > 0.4 and s.sentiments < 0.6:
                neu = neu + 1
            elif s.sentiments < 0.3:
                neg = neg + 1
            else:
                pass
        print("输出")
        print('积极评论数', pos, '中级评论数', neu, '消极评论数', neg)
        x=i
        sql = "insert into events(passive_remark,neutral_remark,negative_remark) VALUES %s;"
        ret = dic2sql(pos, neu, neg, sql)
        print(ret)
        # print('积极评论数',pos,'中级评论数',neu,'消极评论数',neg)
        # sql = "insert into remark(pos,neu,neg,user_id) VALUES %s;"
        # ret = dic2sql(pos, neu, neg,one,sql)
        # print(ret)


        # 连接MySQL，并提交数据
        cxn = MySQLdb.connect(host="localhost",
                              database="user",
                              user="root",
                              password="root",
                              port=3306,
                              charset='utf8')
        cur = cxn.cursor()
        cur.execute(ret,i)
        cxn.commit()
    except ZeroDivisionError:  # 'ZeroDivisionError'除数等于0的报错方式
        print("You can't divide by zero!")



