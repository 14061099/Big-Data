# coding=utf-8
from datetime import datetime, timedelta
from pandas import Series, DataFrame
from OrderOp import Order


class Config(object):#常量，其中变量不允许在回测运行后修改
    @staticmethod
    def starting_cash():
        return 10000
    @staticmethod
    def stock_pool():
        return ['g1','g2','g3','g4','g5']
    @staticmethod
    def open():
        return 100
    @staticmethod
    def close():
        return 200
    @staticmethod
    def low():
        return 80
    @staticmethod
    def high():
        return 250
    @staticmethod
    def volume():
        return 5000
    @staticmethod
    def money():
        return 1000000
    @staticmethod
    def avg():
        return 123
    @staticmethod
    def preclose():
        return 101


class Context(object):#全局变量
    __slots__ = ('_portfolio','_current_dt','_previous_dt','_universe','_start_date','_end_date','_style','_frequency')
    def __init__(self):
        self._portfolio = Portfolio() #  账户
        self._universe = Config.stock_pool() # 股票池
        self._current_dt = datetime(2016, 11, 1, 0, 0) # 当前时间
        self._previous_dt = None
        self._previous_dt = None # 前一个时间
        self._start_date = self._current_dt # 回测起时
        self._end_date = self.start_date + timedelta(days=30) # 回测终时
        self._style = 'huice' # ？？？
        self._frequency = 'minute' # 时间细度
    @property
    def portfolio(self):
        return self._portfolio
    @property
    def universe(self):
        return self._universe
    @property
    def current_dt(self):
        return self._current_dt
    @property
    def previous_dt(self):
        return self._previous_dt
    @property
    def start_date(self):
        return self._start_date
    @property
    def end_date(self):
        return self._end_date
    @property
    def style(self):
        return self._style
    @property
    def frequency(self):
        return self._frequency
    def Changetime(self,t):
        if isinstance(t,datetime):
            self._previous_dt = self._current_dt
            self._current_dt = t
            return True
        else:
            return False


class Portfolio(object):# 个体
    __slots__ = ('_starting_cash','_cash','_available_cash','_locked_cash','_positions','_total_value','_positions_value')
    def __init__(self):
        self._starting_cash = Config.starting_cash()
        self._cash = self._starting_cash
        self._available_cash = self._cash
        self._locked_cash = 0
        p = []
        for i in range(0,5):
            p.append(Position('g'+unicode(i)))
        self._positions = Series(p,index=Config.stock_pool())
        self._total_value = self._cash
        self._positions_value = 0
    @property
    def starting_cash(self):
        return self.starting_cash
    @property
    def cash(self):
        return self._cash
    @property
    def available_cash(self):
        return self._available_cash
    @property
    def locked_cash(self):
        return self._locked_cash
    @property
    def positions(self):
        return self._positions
    @property
    def total_value(self):
        return self._total_value
    @property
    def positions_value(self):
        return self._positions_value


class Position(object):# 仓位
    __slots__ = ('_security','_price','_avg_cost','_total_amount','_available_amount','_locked_amount')
    def __init__(self,stock_name):
        self._security = stock_name
        self._price = 0
        self._avg_cost = 0
        self._total_amount = 0
        self._available_amount = 0
        self._locked_amount = 0
    @property
    def security(self):
        return self._security
    @property
    def price(self):
        return self._price
    @property
    def avg_cost(self):
        return self._avg_cost
    @property
    def total_amount(self):
        return self._total_amount
    @property
    def available_amount(self):
        return self._available_amount
    @property
    def locked_amount(self):
        return self.locked_amount
    def Change(self,order):  # 订单对仓位的改变,成功返回0
        if isinstance(order, Order):
            if order.stock_name!=self._security:
                print('Position received an invalid parameter:an order with no connection(%s,%s)' % (self._security,order.stock_name))
                return -1
            elif (order.is_buy==True):
                #i need to know the buy-in price to update data (price,avg_cost)
                self._total_amount += order.amount
                self._locked_amount += order.amount
                return 0
            else:
                if self._available_amount<order.amount:
                    print('Position received an invalid parameter:an order with over-much amount(%d,%d)'% (self._available_amount,order.amount))
                    return -1
                else:
                    self._available_amount -= order.amount
                    self._total_amount-= order.amount
                    return 0
        else:
            print 'Position received a non-Order parameter'
            return -1
    def Update(self):#一天结束对仓位数据的检查和刷新，正常返回0
        #check
        if(self._price<0 or self._avg_cost<0 or self._total_amount<0 or self._available_amount<0 or self._locked_amount<0):
            print('Position occur an error: data < 0')
            return -1
        if(self._total_amount!=self._available_amount+self._locked_amount):
            print('Position occur an error: data mess')
            return -1
        #flush
        self._available_amount = self._total_amount
        self._locked_amount = 0
        return 0

class SecurityUnitData(object):#之后用pandas替代
    __slots__ = ('_security','_open','_close','_low','_high','_volume','_money','_high_limit','_low_limit','_avg','_pre_close','_paused')
    def __init__(self,stock_name):
        self._security = stock_name
        self._open = Config.open()
        self._close = Config.close()
        self._low = Config.low()
        self._high = Config.high()
        self._volume = Config.volume()
        self._money = Config.money()
        self._high_limit = 0
        self._low_limit = 0
        self._avg = Config.avg()
        self._pre_close = Config.preclose()
        self._paused = False
    @property
    def security(self):
        return self._security
    @property
    def open(self):
        return self._open
    @property
    def close(self):
        return self._close
    @property
    def low(self):
        return self._low
    @property
    def high(self):
        return self._high
    @property
    def volume(self):
        return self._volume
    @property
    def money(self):
        return self._money
    @property
    def high_limit(self):
        return self._high_limit
    @property
    def low_limit(self):
        return self._low_limit
    @property
    def avg(self,n=1):# 返回最近n天的平均价格
        return self._avg
    @property
    def preclose(self,n=1):# 返回n天前的收盘价
        return self._pre_close
    @property
    def paused(self):
        return self._paused


def initialize():# 用户编写，放到单独py文件中
    return 0


def handle_data():# 用户编写，放到单独py文件中
    return 0

class Security(object):# 模拟数据
    def __init__(self):
        dates = [
            datetime(2016, 11, 1, 0, 0),
            datetime(2016, 11, 1, 0, 1),
            datetime(2016, 11, 1, 0, 2),
            datetime(2016, 11, 1, 0, 3),
            datetime(2016, 11, 1, 0, 4),
            datetime(2016, 11, 1, 0, 0),
            datetime(2016, 11, 1, 1, 1),
            datetime(2016, 11, 1, 1, 2),
            datetime(2016, 11, 1, 1, 3),
            datetime(2016, 11, 1, 2, 0),
            datetime(2016, 11, 2, 0, 0),
            datetime(2016, 11, 2, 0, 1),
            datetime(2016, 11, 2, 0, 2),
            datetime(2016, 11, 3, 0, 0),
            datetime(2016, 11, 4, 0, 0)
        ]
        self._security = DataFrame(
            {
                'date': dates,
                'open': [
                50, 58, 68, 59, 69, 60, 50, 58, 68, 59, 69, 60, 61, 62, 62
            ], 'close': [
                58, 68, 59, 69, 60, 50, 58, 68, 59, 69, 60, 61, 62, 62, 62
            ], 'high': [
                58, 68, 59, 69, 60, 50, 58, 68, 59, 69, 60, 61, 62, 62, 62
            ], 'low': [
                50, 58, 68, 59, 69, 60, 50, 58, 68, 59, 69, 60, 61, 62, 62
            ]
            },
            index = dates
        )
        self._security.index.name = 'index'
        self._end = 14
    @property
    def security(self):
        return self._security
    def hasday(self,current_date):
        if isinstance(current_date,datetime):
            if (current_date>=self._security.iloc[0].date and current_date<=self._security.iloc[self._end].date):
                return True
            else:
                return False
        else:
            print 'Security received an invalid parameter: a non-datetime object'
            return False
    def day_not_end(self,current_date):# 未完成
        if isinstance(current_date,datetime):
            print
        else:
            print 'Security received an invalid parameter: a non-datetime object'
            return False
    def next_day(self,current_date):
        if isinstance(current_date,datetime):
            d = current_date+timedelta(days=1)
            if d<self._security.iloc[self._end].date:
               return datetime(year=d.year,month=d.month,day=d.day,hour=0,minute=0)
            else:
                return None
        else:
            print 'Security received an invalid parameter: a non-datetime object'
            return None



def run():
    # 初始化
    context = Context()
    security = Security()
    initialize()
    # 开始回测
    print 'start ',context.current_dt
    while security.hasday(context.current_dt):# 按日循环
        print '--in day loop'
        # 开盘前
        for p in context.portfolio.positions:
            p.Update()
        # 盘中
        for t in security.security[context.current_dt.strftime('%Y-%m-%d')]['date']:# 按分钟循环
            print '--in minute loop'
            context.Changetime(t)# 改变时间
            handle_data()
            # 处理订单
        # 收盘后
        # 取消所有未完成订单
        nxtday = security.next_day(context.current_dt)
        if nxtday is None:
            break
        else:
            context.Changetime(nxtday) # 计算下一天
            print context.current_dt
    # 反应结果
    # 打印日志


if __name__=='__main__':
    run()