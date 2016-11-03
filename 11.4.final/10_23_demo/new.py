
def initialize(context):
    stocks = ['SZ002680']
    context.set_universe(stocks)


def handle_data(context,o):
    for pos in context.portfolio.positions:
        o.order(pos.security, 1)
        o.order_target(pos.security, 30)
        o.order_target_value(pos.security, 100000)
        print ('position %s have %d amount' % (pos, pos.total_amount))
    return 0