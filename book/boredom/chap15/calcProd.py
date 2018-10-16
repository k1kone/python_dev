#!pyhton3

import time

def calc():
	product =1
	for i in range(1, 10000):
		product = product * i

	return product

setTime = time.time()

p = calc()

endTime = time.time()


print('計算結果：{}桁'.format(len(str(p))))
print('計算時間：{}'.format(endTime - setTime))
