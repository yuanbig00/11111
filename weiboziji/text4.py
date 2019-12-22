import MySQLdb
from snownlp import SnowNLP
# -*- coding: utf-8 -*-
#实现用户和评论，头像的表格ok
import pandas as pd
import pymysql
import numpy as np
dbconn = pymysql.connect(
    host="localhost",
    database="user",
    user="root",
    password="root",
    port=3306,
    charset='utf8'
)
cursor_fetch=dbconn.cursor()
sqlcmd2='select  id  from  comment '
b=pd.read_sql(sqlcmd2,dbconn)
# print(b)
id=np.unique(b)
# sqlcmd4='select  id  from  user '
# c=pd.read_sql(sqlcmd4,dbconn)
# user_id=np.unique(c)
# com_id= [x for x in id if x in user_id]
# print(id)
# print(user_id)
# print("is",com_id)

def dic2sql(id,name1,comment1,pic1,name2,comment2,pic2,name3,comment3,pic3,name4,comment4,pic4,name5,comment5,pic5,name6,comment6,pic6,sql):
    sf = ''
    tup = (id,name1,comment1,pic1,name2,comment2,pic2,name3,comment3,pic3,name4,comment4,pic4,name5,comment5,pic5,name6,comment6,pic6)
    sf += (str(tup) + ',')
    sf = sf.rstrip(',')
    sql2 = sql % sf
    return sql2
for i in range(len(id)):
    sqlcmd = "select screen_name,text,profile_image_url from comment where id=%s"
    cursor_fetch.execute(sqlcmd, id[i])
    results = cursor_fetch.fetchall()
    one=id[i]
    namelist=[]
    commentlist=[]
    piclist=[]
    try:
        if len(results)>6:
            for n in range(6):
                name = results[n][0]
                comment = results[n][1]
                pic = results[n][2]
                namelist.append(name)
                commentlist.append(comment)
                piclist.append(pic)
            # print(namelist)
            # print(type(commentlist[1]))
            sql = "insert into person_remarks(id,person1_name,person1_remark,person1_pic,person2_name,person2_remark,person2_pic,person3_name,person3_remark,person3_pic,person4_name,person4_remark,person4_pic,person5_name,person5_remark,person5_pic,person6_name,person6_remark,person6_pic) VALUES %s;"
            ret = dic2sql(one,namelist[0], commentlist[0],piclist[0] ,namelist[1], commentlist[1],piclist[1],
                          namelist[2], commentlist[2],piclist[2], namelist[3], commentlist[3],piclist[3],
                          namelist[4], commentlist[4],piclist[4], namelist[5], commentlist[5],piclist[5], sql )
            print(ret)
            # 连接MySQL，并提交数据
            cxn = MySQLdb.connect(host="localhost",
                              database="user",
                              user="root",
                              password="root",
                              port=3306,
                              charset='utf8')
            cur = cxn.cursor()
            cur.execute(ret)
            cxn.commit()
    except ZeroDivisionError:
                print("You can't divide by zero!")

 