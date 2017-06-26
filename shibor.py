# -*- coding: utf-8 -*-
"""
Created on Tue May 23 10:02:20 2017
@email:hanlinsan@163.com
@author: hanlinsan

"""

import os
import requests
from bs4 import BeautifulSoup
from datetime import date

currentDate = date.today()

shiborUrls = ['http://www.shibor.org/shibor/web/html/shibor.html',]
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}

r = requests.get(shiborUrls[0], headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
tableShibor = soup.select('.shiborquxian')[0]

trs = tableShibor.find_all('tr')[0:8]

shiborDatas = [str(currentDate)]

for tr in trs:
    _,_,shibor,*ign = tr.find_all('td')
    shiborDatas.append(shibor.string)  
    

line = ','.join(shiborDatas) + '\n'

shiborsFile = r".\shibors.csv"

if not os.path.exists(shiborsFile) :
    with open(shiborsFile, 'xt') as f :
        f.write(line)
else:
    with open(shiborsFile,'at') as f :
        f.write(line)
