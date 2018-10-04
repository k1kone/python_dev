class Customer:
	bmi = 22
	def __init__ (self, number, name, height=100):
		self.number = number
		self.name = name
		self.height = height

	def std_weight(self):
		return Customer.bmi*(self.height/100)**2

	def sampledef(sefl):
		pass

if __name__ == "__main__":

	taro = Customer(101, 'taro', 180)
	hanako = Customer(102, 'hanako', 165)

	print("{} -->標準体重:{:.2f}kg".format(taro.name, 
	taro.std_weight()))
	print("{} -->標準体重:{:.2f}kg".format(hanako.name, 
	hanako.std_weight()))
