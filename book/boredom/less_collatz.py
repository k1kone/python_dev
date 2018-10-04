import sys

try:
	num = int(input('please input number : '))

except ValueError:
	print('input in not number.')
	exit()

def collatz(num):
	if num%2 ==0:
			return int(num/2)
	if num%2 !=0:
			return 3*num + 1
			
			
while num > 1:
		num = collatz(num)
		print(num) 



"""
コラッツ関数を定義

numberというプロパティをもつ

inputのnumberに格納

numberが1になるまで
	numberが偶数なら2倍
	numberが奇数なら3倍して+1をする
を繰り返す

try節とexcept節を記述し
numberが文字列であったときにアラートを出す

"""
