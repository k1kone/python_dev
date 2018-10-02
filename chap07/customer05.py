class Customer:
	bmi = 22
	def __init__ (self, number, name, height=100):
		self.number = number
		self.name = name
		self.height = height

	def std_weight(self):
		return Customer.bmi*(self.height/100)**2




taro = Customer(101, 'taro', 180)
hanako = Customer(102, 'hanako', 150)

Customer.LIMIT = 100;

print("Customer.LIMIT" + str(Customer.LIMIT))
print("{}.LIMIT --> {}" 
	.format(taro.name, taro.LIMIT))
print("{}.LIMIT --> {}"
	.format(hanako.name, hanako.LIMIT))

#定数として使用する変数は、他の変数と区別するため大文字で記述しましょう
