#!/usr/bin/python3
import pymysql.cursors
import datetime
import time

con = pymysql.connect( host='localhost',
db='test', user='admin96',password='kurosaki96',charset='utf8',
cursorclass=pymysql.cursors.DictCursor)

with con.cursor() as cursor:
  sql = "select * from test.sample"
  cursor.execute(sql)

  result= cursor.fetchall()
  for r in result:
    print(r)

con.close()

