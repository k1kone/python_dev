from test_class import testCl
from datetime import date

class clSub(testCl):
	def __init__(self, name, math=0, jap=0, eng=0, birth=0):
		self.__birth = birth
		super().__init__(name, math, jap, eng)

	def birthPrint(self):
		print("birthday:{}".format(self.__birth))


ichiro = clSub('ichiro', 30, 40, 56, date(1988, 4, 30))

ichiro.info()
ichiro.birthPrint()
