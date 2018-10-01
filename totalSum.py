#1~50までの総和を表示

n = 0

b =0
while n <= 50:
		b +=n
		n = n+1	
		print(b, end=" ")
print()


""" ーーーーーーーーーーーーー
range関数を使って行う
for 変数 in range([始まりの数値], [終わりの数値])

●r range([開始の数値], [終わりの数値], [ステップ幅 ※ 省略可])
ーーーーーーーーーーーーーー """
s = 0
for x in range(1,51):
		s +=x
print("""
---range()--- """)
print(s)



""" ーーーーーーーーーーーーー
sum関数を使う場合

sum関数はリストに格納された数値の合計を出すことができます。
[sample]
lst = 1, 2, 3
sum(lst)
>> 6
ーーーーーーーーーーーーーー """
print("""
---sum()--- """)

r =  sum(range(1, 51))
print(r)


""" ーーーーーーーーーーーーー
generater式 を使う
 ーーーーーーーーーーーーー """
r = sum(i for i in range(1,51))
print("""
----- generater -------""")
print(r)

""" ーーーーーーーーーーーーー
reduce を使う
 ーーーーーーーーーーーーー """
#print("""
#---- reduce ---""")
#print reduce(lambda x,y: x+y, range(1, 51))
""" ※ python3 ではreduce は functools に移動されたため、
使用するには import する必要があります。 """
