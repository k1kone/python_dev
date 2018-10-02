import datetime
from datetime import date

class Customer:
	bmi = 22
	def __init__ (self, number, name, height=100):
		self.number = number
		self.name = name
		self.height = height

	def std_weight(self):
		return Customer.bmi*(self.height/100)**2


nowtime = datetime.datetime

print(nowtime.now())

taro = Customer(101, 'taro', 180)
taro.birthdate = date(1989, 7, 3)
print("{} -->誕生日:{}".format(taro.name, 
	taro.birthdate))

"""

__init__ 内で宣言された変数 -> インスタンス変数
	インスタンス内でアクセス可能

それ以外の変数 -> クラス変数
	インスタンス外からアクセス可能

"""
