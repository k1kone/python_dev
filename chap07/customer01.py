class Customer:
	def __init__ (self, number, name, height=100):
		self.number = number
		self.name = name
		self.height = height


taro = Customer(101, 'taro', 180)
print('{}:{} {}cm'.format(taro.number, taro.name, taro.height))

taro.height = 175
print('{}:{} {}cm'.format(taro.number, taro.name, taro.height))
