class Customer:
	bmi = 0
	def __init__ (self, number, name, height=100):
		self.number = number
		self.name = name
		self.height = height


print('bmi:{}'.format(Customer.bmi))

taro = Customer(101, 'taro', 180)
hanako = Customer(102, 'hanako', 165)

Customer.bmi = 100
#print('{}:{} {}cm'.format(taro.number, taro.name, taro.height))
#print('{}:{} {}cm'.format(hanako.number, hanako.name, hanako.height))
print("{} -->bmi:{}".format(taro.name, taro.bmi))
print("{} -->bmi:{}".format(hanako.name, hanako.bmi))

"""

__init__ 内で宣言された変数 -> インスタンス変数
	インスタンス内でアクセス可能

それ以外の変数 -> クラス変数
	インスタンス外からアクセス可能

"""
