from OrderOp import *

o = OrderList()
o.order_consume()
print o.get_trades()
print o.total_amount,o.total_value

o.order("23",100)
o.order_consume()
print o.get_trades()
print o.get_open_orders()
print o.total_amount,o.total_value

o.order_target("23",1200)
o.order_consume()
print o.get_trades()
print o.get_open_orders()
print o.total_amount,o.total_value

#o.order_target("23",-1)
#print o.get_orders()

o.order_target("23",1000)
o.order_consume()
print o.get_trades()
print o.get_open_orders()
print o.total_amount,o.total_value

o.order_value("23",10000)
o.order_consume()
print o.get_trades()
print o.get_open_orders()
print o.total_amount,o.total_value

o.order_target_value("23",40000)
o.order_consume()
print o.get_trades()
print o.get_open_orders()
print o.total_amount,o.total_value

#o.order_target_value("23",-1)
#print o.get_orders()

o.order_target_value("23",10000)
o.order_consume()
print o.get_trades()
print o.get_open_orders()
print o.total_amount,o.total_value

#o.cancel_order(6)
#o.order_consume()
#print o.get_trades()
#print o.total_amount,o.total_value

#o.cancel_order(6)
#print o.get_open_orders()

o.order_reset()
o.order_consume()
print o.get_trades()
print o.get_open_orders()
print o.total_amount,o.total_value

#o.order("23",500)
#o.order_consume()
#print o.get_trades()
#print o.get_open_orders()
#print o.total_amount,o.total_value

#o.order_target("23",400)
#o.order_consume()
#print o.get_trades()
#print o.get_open_orders()
#print o.total_amount,o.total_value

o.order("23",-1200)
o.order_consume()
print o.get_trades()
print o.get_open_orders()
print o.total_amount,o.total_value

o.order_value("23",-1000000)
o.order_consume()
print o.get_trades()
print o.get_open_orders()
print o.total_amount,o.total_value
