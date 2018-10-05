print('''**********************************
	辞書型
**********************************''')

print('''辞書型の記述は以下です
dic = {'key':'value', 133:1000 } 

#keyに数値を使うこともできます。

#辞書型には順番がありません。リストのようにインデックス指定で
値を取得することはできません。
値を取得する場合は、
dic['key'] と記述し取得してください。''')

dic = {'key':'value', 133:1000}
print('print(dic[133]) >', dic[133])

print('''\v-------------------------------------
 keys(), values(), item() メソッド
-------------------------------------
for文と組み合わせることで辞書型から要素を取得できます。
values() : バリュー
items() : キーペアバリュー
''')
fruits_num = {'apple':2, 'banana':6, 'orange':9}


print("#fruits_num = {'apple':2, 'banana':6, 'orange':9}")


print('\v#for i in fruits_num.keys(): #キーの取得 >')
for i in fruits_num.keys():
	print(i)

print('\v#for i in fruits_num.values(): #バリューの取得 >')
for i in fruits_num.values():
	print(i)

print('\v#for i in fruits_num.items(): #キーペアバリューの取得 >')
for i in fruits_num.items():
	print(i)
print('''\n#for文を以下のようにすることもできます
for i,j in fruits_num.items():
	print('key : {} / value : {}'.format(i,j)) >''')
for i,j in fruits_num.items():
	print('key : {} / value : {}'.format(i,j))

print('''\v#辞書型を要素をリストへ代入する場合は以下のようにしてください
l = list(fruits_num.key())
l\'s contents >''')
l = list(fruits_num.keys())
for i in l:
	print(i, end=" / ")

print("""\v\n-------------------------------------
 get(), setdefault()メソッド
-------------------------------------
# in/not in をつかって辞書型の中身を調べることもできますが、
get()メソッドを使うと、値が存在すれば取得し
存在しなければ引数に渡された値をかえします

get('key', [存在しないときに渡す値)
# print(fruits_num.get('apple', 45)) > 存在する
# print(fruits_num.get('pine', 45)) > 存在しない""")

print("fruits_num['apple'] = " + str(fruits_num.get('apple', 45)))
print("fruits_num['pine'] = " + str(fruits_num.get('pine', 45)))

print("""\v\n#setdefault()メソッドでは辞書に第一引数のキーが
未登録の場合のみ、第一引数のキーと第二引数の値を登録できます。
# fruits_num.setdefault('banana', 45) > 存在する
# fruits_num.setdefault('grape', 45) > 存在しない""")
fruits_num.setdefault('banana', 45)
fruits_num.setdefault('grape', 45)

print("fruits_num['banana'] = " + str(fruits_num['banana']))
print("fruits_num['grape'] = " + str(fruits_num['grape']))
print("fruits_num's keys : values >")
for i,j in fruits_num.items():
	print('{} : {}'.format(i, j))








