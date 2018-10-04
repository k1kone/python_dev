ls_str = ['America', 'France', 'Canada', 'arizona', 'Brazil', 'Japan']
ls_int = [4, 7, 3, 23, 9, 54, 1, 8]

print("ls_str's contents are")
for i, con in enumerate(ls_str):
	print('{}:{}'.format(i, con))

print("\vls_int's contents are")
for i, con in enumerate(ls_int):
	print('{}:{}'.format(i, con))

print('''\vーーー 配列の数を取得 ーーー
len(list) ---''')
print('ls_str\'s is length : ' +  str(len(ls_str)))

print('''\vーーー 配列の中身を調べる ーーー
list.index(target) #インデックスを返す---''')
print('index of "Canada" in ls_str is ' + str(ls_str.index('Canada')))

print('\n"Ward" in list #ワードがリストに含まれているかを真偽で返す---')
print('ls_str have word "Canada":' + str('Canada' in ls_str))
print('ls_str have word "China":' + str('China' in ls_str))

print('''\vーーー 配列に要素を追加 ーーー
list.append(element) #リストの一番最後に要素を追加---''')
ls_str.append('Koria')
print('{}:{}'.format(len(ls_str), ls_str[len(ls_str)-1]))

print('\nlist.insert(index, element) #リストの指定した位置にに要素を追加---')
ls_str.insert(1, 'Oranda')
print('{}:{}'.format(1, ls_str[1]))


print('\nその他の要素の追加方---\n#リストの連結')
country = 'India'
ls_str = ls_str + [country]
print('ls_str + [country] = {}:{}'.format(len(ls_str), ls_str[len(ls_str)-1]))


print('\n#複数代入（リストの要素を複数の変数に一度の記述で代入）')
ls_test = ['test1', 'test2', 'tset3']
t1, t2, t3 = ls_test
print("""ls_test = ['test1', 'test2', 'tset3']
t1, t2, t3 = ls_test
print(t1, t2, t3) : """ + t1 +" "+ t2 + " " + t3)


print('''\vーーー 配列の中身をソート ーーー
list.sort(keyword propaty) ---''')
ls_str.sort()
print('ls_str.sort() : ')
for i, con in enumerate(ls_str):
	print('{}:{}'.format(i, con))

ls_int.sort()
print('\nls_int.sort() : ')
for i, con in enumerate(ls_int):
	print('{}:{}'.format(i, con))

print('\n#逆順')
print('ls_int.sort(reverse=True) : ')
ls_int.sort(reverse=True) 
for i, con in enumerate(ls_int):
	print('{}:{}'.format(i, con))

print('\n#小文字優先 ※ 文字列のソートはデフォルトは大文字優先')
ls_str.sort(key=str.lower)
print('ls_str.sort(key=str.lower) #すべて小文字としてソート : ')
for i, con in enumerate(ls_str):
	print('{}:{}'.format(i, con))


print('''\vーーー 配列の中身を削除 ーーー
del list[index] ---''')
del ls_int[3]
print('del ls_int[3] >')
for i, con in enumerate(ls_int):
	print('{}:{}'.format(i, con))


print('\nlist.remove(keyword) ---''')
ls_str.remove('Koria')
print('ls_str.remove("Koria") >')
for i, con in enumerate(ls_str):
	print('{}:{}'.format(i, con))

