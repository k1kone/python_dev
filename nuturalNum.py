""" ２つの整数の最大公約数を求める """

def yakusu(n1, n2):
		ar1 = []
		ar2 = []
		ar3 = []
		x, y = 1, 1

		while(x <= n1):
				if(n1%x == 0): ar1.append(x)
				x +=1
		print(str(n1) + "の約数は")
		for n in ar1:
				print(n, end=" ")

		while(y <= n2):
				if(n2%y == 0): ar2.append(y)
				y +=1
		print("\n----------\n" + str(n2) + "の約数は")
		for m in ar2:
				print(m, end=" ")

		for a in ar1:
				for b in ar2:
						if(a == b): ar3.append(a)
		print("\n-----------\n最大公約数は" + str(max(ar3)))

yakusu(int(input("input number1:")), int(input("input number2:")))


""" ーーーーーーーーーーー
再起法（ユーリグッドの除去法）
ーーーーーーーーーーーーーー """

x, y = input(), input()

def gbc(a, b):
	if(b == 0):return a
	else:
		return gbc(b, a%b)

num = gbc(int(x), int(y))
print(num)
