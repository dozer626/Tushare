# coding=utf-8
import tushare as ts


# 需要定义一个基类里面放公共的方法，比如获取当前要查询的股票代码，并且支持多个



class GetNewsFunc(object):
    def __init__(self,dateS,dateE):
        # self.stockcodes = stockcodes
        self.dateS = dateS
        self.dateE = dateE
    def get_latest_news(self,topN):
        latest_news = ts.get_latest_news(topN)
        return latest_news
    def get_notices(self,code):
        notices = ts.get_notices(code,self.dateS)
        return notices


this = GetNewsFunc('2017-08-25','2017-08-24')
print this.get_notices('000002')

# print ts.get_notices('000002','2017-08-11')