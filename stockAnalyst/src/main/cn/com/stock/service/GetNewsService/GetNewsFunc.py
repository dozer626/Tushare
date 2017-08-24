# coding=utf-8
'''
author  :   lesq
date    :   2017-08-24
'''

import tushare as ts
import pandas as pd


# 需要定义一个基类里面放公共的方法，比如获取当前要查询的股票代码，并且支持多个



class GetNewsFunc(object):
    def __init__(self,dateS,dateE):
        # self.stockcodes = stockcodes
        self.dateS = dateS
        self.dateE = dateE
    def get_latest_news(self,topN):
        newslist = ts.get_latest_news(topN)
        latest_news = ()
        i = 0
        for record in newslist:
            print record.title[i]
        return latest_news
    def get_notices(self,code):
        notices = ts.get_notices(code,self.dateS)
        return notices


this = GetNewsFunc('2017-08-25','2017-08-24')
print this.get_latest_news(1)

# this = ts.get_notices('000002','2017-08-25')
# print this.title[2]