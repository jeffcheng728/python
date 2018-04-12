#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from rblwatch import RBLSearch
import smtplib
import time
import sys
import csv
import pandas as pd

# 取得執行時的時跟分，格式如 1815
now = str(time.localtime().tm_hour)+str(time.localtime().tm_min)

# 要檢查的 IP
argv_nu = len(sys.argv)

# 判斷是否有帶參數，有則第1個參數當 checkIP

if argv_nu == 1:
  checkIP = ("140.109.20.25","60.238.117.117")
else:
  checkIP = [sys.argv[1]]

# 初始化 line
line = ''

# 預設不寄發 eMail
sendMail = 0

for IP in checkIP:
  searcher = RBLSearch(IP)
  # Use the result data for something else
  result_data = searcher.listed
  title='******** Checking IP_' + IP + ' ********'
  print(title)
  line = line + title + "\r\n"
  for keys,values in result_data.items():
    if keys == 'SEARCH_HOST':
        continue
    if values['LISTED']:
        print(keys,values['LISTED'])
    line = line + keys + "," + str(values['LISTED']) + "\r\n"
    sendMail = 1
    line = line + '\r\n'

#f = open("spam.csv",'w',encoding='utf-8')
#spam =f.write((line))
#f.close()
print (line)