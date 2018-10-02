from customer_m2 import Customer
from datetime import date

class GoldCustomer(Customer):
	def __init__(self, number, name, height=0, birthdate=0):
		self.__birthdate = birthdate
		super().__init__(number, name, height)

	#property
	def get_birthdate(self):
		return self.__birthdate
	birthdate = property(get_birthdate)


if __name__ == "__main__":
		taro = GoldCustomer(101, "taro", 180, date(1978,9,1))

		name = taro.name
		number = taro.number
		height = taro.height
		std_weight = taro.std_weight()
		birth = taro.birthdate

		print("{} {} 身長:{} 適正体重:{:.2f} 誕生日:{}".format(number, 
			name, height, std_weight, birth))
