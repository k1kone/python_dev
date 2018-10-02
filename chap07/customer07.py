class Customer:
	bmi = 22
	def __init__ (self, number, name, height=100):
		self.__number = number
		self.__name = name
		self.__height = height

	def std_weight(self):
		return Customer.bmi*(self.height/100)**2

	def get_name(self):
		return self.__name

	def get_number(self):
		return self.__number

	def get_height(self):
		return self.__height

	def set_name(self, name):
		self.__name = name

	def set_number(self, number):
		self.__number = number

	def set_height(self, height):
		self.__height = height

	def show_info(self):
		print("{} : {}".format(self.number, self.name))

	#property
	name = property(get_name)
	number = property(get_number, set_number)
	height = property(get_height, set_height)


taro = Customer(101, 'taro', 180)

name = taro.name
taro.number = 99
number = taro.number
height = taro.height

print("{}:{} {}cm".format(number, name, height))
