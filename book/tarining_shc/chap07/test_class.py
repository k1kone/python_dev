class testCl:
	def __init__(self, name, math=0, jap=0, eng=0):
		self.__name = name
		self.__math = math
		self.__jap = jap
		self.__eng = eng
		self.__total = self.__math+self.__jap+self.__eng 
		self.__avg = self.__total/3
		
	def get_name(self):
		return self.__name
		
	def set_name(self, name):
		self.__name = name
		
	def info(self):
		print("""name:{}
--score--
math:{}
jap:{}
eng:{}
average:{:.2f}""".format(self.__name, self.__math, self.__jap, self.__eng, self.__avg))	


if __name__ == "__main__":

		taro = testCl("taro", 20, 45, 87)
		
		taro.info()
