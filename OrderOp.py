class OrderList(object):
	List = {} #unfinished orders set , do not include the canceled orders
	Backup = {} #orders set of all , do include the canceled orders
	i = 1 #index order id , first order's index is 1
	Trades = {} #finished orders set
	lock_amount = 0#locked stock amount of the day
	#####################################################################################
	#the following is for test. these are the ports of other files or classes
	total_amount = 1000 #for test , port : portfolio's total stock amount
	total_value  = 10000 #for test , port : portfolio's total stock value

	class Order(object):#for test , port: datas.py class Order
		def __init__(self,amount,stock_name,is_buy=True):
			self.is_buy=is_buy
			self.amount=amount
			self.stock_name=stock_name

	def get_current_price(self,stock_name):#for test , port : Query.py get_current_price
		return 1
	#####################################################################################

	def order(self,stock_name,amount,style=None):#return id
		if amount+self.total_amount < 0:
			raise Exception("Illegal order amount , return -1")
		else:
			if amount >= 0:
				o = self.Order(amount,stock_name)#port
			else:
				o = self.Order(-amount,stock_name,False)#port
	                self.List[self.i]=o
			self.Backup[self.i]=o
			self.i+=1
			return(self.i-1)
		return -1


	def order_target(self,stock_name,amount,style=None):#return id
		gap = amount - self.total_amount#port
		if amount < 0:
			raise Exception("Illegal stock toal amount, return -1")
		else:
			if gap >= 0:
				o = self.Order(gap,stock_name)#port
			else:
				o = self.Order(-gap,stock_name,False)#port
			self.List[self.i]=o
			self.Backup[self.i]=o
			self.i+=1
			return(self.i-1)
		return -1

	def order_value(self,stock_name,value,style=None):#return id
		if value+self.total_value < 0:
			raise Exception("Illegal order value , return -1")
		else:
			price = self.get_current_price(stock_name)#port
			if value >= 0:
				o = self.Order(value/price,stock_name)#port
			else:
				o = self.Order(-value/price,stock_name,False)#port
			self.List[self.i]=o
			self.Backup[self.i]=o
			self.i+=1
			return(self.i-1)

	def order_target_value(self,stock_name,value,style=None):#return id
		gap = value - self.total_value#port
		price = self.get_current_price(stock_name)#port
		if value < 0:
			raise Exception("Illegal stock total value, return -1")
		else:	
			if gap >= 0:
				o = self.Order(gap/price,stock_name)#port
			else:
				o = self.Order(-gap/price,stock_name,False)#port
			self.List[self.i]=o
			self.Backup[self.i]=o
			self.i+=1
			return(self.i-1)
		return -1

	def cancel_order(self,id):#return Order
		if id > self.i or id <=0:
			raise Exception("Illegal order id")
		elif id not in self.List:
			raise Exception("Order has been canceled or consumed. Can't cancel it !")
		else:
			o = self.List.pop(id)
			return o
		return None
		

	def get_open_orders(self):#return dict(id,object)
		return self.List

	def get_orders(self):#return dict(id,object)
		return self.Backup

	def get_trades(self):#return dict(id,object)
		return self.Trades

	def order_consume(self):#consume orders
		pop_id=[]
		for id in self.List.keys():
			if self.List[id].is_buy == True:
				self.total_amount+=self.List[id].amount#port
				self.lock_amount+=self.List[id].amount#port
				price = self.get_current_price(self.List[id].stock_name)#port
				self.total_value+=self.List[id].amount*price#port
				self.Trades[id]=self.List[id]
				#self.List.pop(id)
				pop_id.append(id)
			else:
				if (self.total_amount-self.List[id].amount)<self.lock_amount:#port
					continue #this order won't be consumed
				else:
					self.total_amount-=self.List[id].amount#port
					price = self.get_current_price(self.List[id].stock_name)#port
					self.total_value-=self.List[id].amount*price#port
					self.Trades[id]=self.List[id]
					#self.List.pop(id)
					pop_id.append(id)
		for i in pop_id:
			self.List.pop(id)
					
				

	def order_reset(self):#at the end of day , reset the order set 
		self.List = {}
		self.Backup = {}
		self.Trades = {}
		self.i = 1
		self.lock_amount = 0


