import datetime
import pandas_datareader.data as web
from dateutil.relativedelta import relativedelta
import json

def dec_format(value):
    try:
        change = "{0:.2f}".format(value)
    except(TypeError):
        change = "N/A"
    return change

def comma_format(value):
    try:
        change = "{:,}".format(float(value))
    except(TypeError):
        change = "N/A"
    return change

end = datetime.datetime.now()
start = end - relativedelta(years=10)

gdp = web.DataReader('GDP', 'fred', start, end)
wilshire = web.DataReader('WILL5000PR','fred',start,end)

gdp_size = len(gdp)
wilshire_size = len(wilshire)

gdp_last = gdp['GDP'][gdp_size-1]
wilshire_last = wilshire['WILL5000PR'][wilshire_size-1]

buffet_indicator = (wilshire_last / gdp_last) * 100

if buffet_indicator < 50 :
    valuation = "Significantly Undervalued"
if buffet_indicator > 50 and buffet_indicator < 75 :
    valuation = "Modestly Undervalued"
if buffet_indicator > 75 and buffet_indicator < 90 :
    valuation = "Fair Valued"
if buffet_indicator > 90 and buffet_indicator < 115:
    valuation = "Modestly Overvalued"
if buffet_indicator > 115:
    valuation = "Significantly Overvalued"

data = [dec_format(buffet_indicator),valuation,comma_format(dec_format((wilshire_last))),comma_format(dec_format(gdp_last))]

with open('buffett_indicator.txt','w') as outfile:
    json.dump(data,outfile)
