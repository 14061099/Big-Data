from DBMS import DBMS
import re
from datetime import datetime

from pandas import Series as se
from pandas import DataFrame as df

parList = ['amount','datetime','end','max','min','money','start']

class Query(object):
    def __init__(self,host,ip):
        self.dbms = DBMS(host,ip)


#start_date and end_date are string format like '2016.2.15.10.45'
#fields is one of []
    def get_price(self,stock_name,col_name,start_date=None,end_date=None,fields=[]):
        s_datetime = start_date
        e_datetime = end_date


        if s_datetime>e_datetime:
            raise Exception("start time should not be later than end time")



        col = self.dbms.get_col(stock_name,col_name)
        result = col.find({
            'datetime' : {'$gte': s_datetime,'$lte':e_datetime}
        })
        d = []
        index =[]
        for m in result:
            del m['_id']
	    pa = re.compile(r"(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+)")
	    match = pa.match(str(m['datetime']))
	    number = ""
	    for num in match.groups():
		number = number+ num
            index.append(number)
            if not fields:
                d.append(m)
            else:
                for n in parList :
                    if n not in fields:
                        del m[n]
                d.append(m)

        Df = df(d,index=index)

        return Df


query = Query('219.224.169.45', 12345)
def get_data(stock_name,start_date,end_date,fields=[]):
    a = query.get_price('Data1516',stock_name,start_date,end_date,fields)
    return a
