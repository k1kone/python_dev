class Customer:
	bmi = 22
	def __init__ (self, number, name, height=100):
		self.number = number
		self.name = name
		self.height = height

	def std_weight(self):
		return Customer.bmi*(self.height/100)**2

def show_info(self):
	print("{} : {}".format(self.number, self.name))



taro = Customer(101, 'taro', 180)
hanako = Customer(102, 'hanako', 150)

Customer.show_info = show_info

taro.show_info()
hanako.show_info()
