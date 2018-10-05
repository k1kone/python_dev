import copy

def fnc(list_date, word):
	list_date.append(word)

l = [4, 5, 'world', 34]
l2 = l
l3 = list(l)
l4 = copy.copy(l)

fnc(l2, 'is mine!')

print('''l = [4, 5, 'world', 34]
l2 = l
l3 = list(l)
l4 = copy.copy(l)

l2.append('is mine!')''')

print('\n---- first set list: l -----')
print('''l2に参照をわたしているため、
l2に変更があるとl1の内容も変更されます''')
for index, i in enumerate(l):
	print('{} : {}'.format(index, i))

print('\n---- second set list: l2 -----')
print('l2にはlの参照が代入されています')
for index, i in enumerate(l2):
	print('{} : {}'.format(index, i))

print('\n---- third set list: l3 -----')
print('l3にはlの値を代入しています')
for index, i in enumerate(l3):
	print('{} : {}'.format(index, i))

print('\n---- third set list: l4 -----')
print('l4にはlの値をコピーしています')
for index, i in enumerate(l4):
	print('{} : {}'.format(index, i))



var1 = 30
var2 = var1
var3 =0
var3 += var1

var1 +=20
print('''\v--- リストでない変数の代入では値渡し---
var1 = 30
var2 = var1
var3 =0
var3 += var1

var1 +=20''')
print('var1:{}, var2:{}, var3:{}'.format(var1, var2, var3))

print('''\v****************************
リストや辞書を参照渡しせずに複製したい場合は、
copyモジュールをimportし、

new_list = copy.copy(base_list)
# new_list = list(base_list) でもOK
とcopy()関数を使用すると、値渡しをせずに複製ができます。
リストを含むリストの複製には、

new_list = copy.deepcopy(base_list)

と deepcopy()関数をしようしてください。
****************************''')

