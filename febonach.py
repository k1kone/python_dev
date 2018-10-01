import sys

def feb(n):
	a, b = 0, 1

	while a < n:
			print(a, end=" ")
			a, b= b, a+b
	print()



feb(int(input("input number : ")))
	
""" -----------------------------------------------

関数の定義は

def functionname():
	処理

になります。
------------------------------------------------ """
