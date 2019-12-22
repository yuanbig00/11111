import MySQLdb
from snownlp import SnowNLP
# -*- coding: utf-8 -*-
import pandas as pd
import pymysql
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import jieba
from nltk.corpus import stopwords
import json
# 词频实现
dbconn = pymysql.connect(
    host="localhost",
    database="user",
    user="root",
    password="root",
    port=3306,
    charset='utf8'
)
def dic2sql(dic, sql,one):
    sf = ''
    for key in dic:
        tup = (key, dic[key],one)
        sf += (str(tup) + ',' )
    sf = sf.rstrip(',')
    sql2 = sql % sf
    return sql2

 

cursor_fetch=dbconn.cursor()
sqlcmd2='select  id  from  comment '
b=pd.read_sql(sqlcmd2,dbconn)
id=np.unique(b)
sentiments_out = []
for i in range(len(id)):
    sqlcmd = "select text from comment where id=%s"
    cursor_fetch.execute(sqlcmd, id[i])
    results = cursor_fetch.fetchall()
    one=id[i]
    dic = {}
    # print(results[0])
    # a=list(results)
    # print(len(results))
    try:
        for n in range(len(results)):
            str2 = results[n][0]
            # print(str2)
            s = SnowNLP(str2)
            h = s.keywords()
            for k in range(len(h)):
                word = h[k]
                if word not in dic:
                    dic[word] = 1
                else:
                    dic[word] = dic[word] + 1
        # print(dic)
        if dic:
            print(dic)
            sql = "insert into jsondata(data) values('%s')"
            try:
                # 执行sql
                db= pymysql.connect(host='localhost', user='root', password='root', db='user', port=3306)
                cur = db.cursor()
                c = json.dumps(dic, ensure_ascii=False)
                cur.execute(sql % c)
                db.commit()
                print("插入数据成功")
            except Exception as e:
                print(e)
                db.rollback()
                print("插入数据失败")

 

    except ZeroDivisionError:  # 'ZeroDivisionError'除数等于0的报错方式
        print("You can't divide by zero!")










