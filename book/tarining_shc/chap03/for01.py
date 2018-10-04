lst = ["月曜", "火曜", "水曜", "木曜", "金曜", "土曜", "日曜"]
for day in lst:
		print(day)


lst2 = "Monday", "Tuesday", "Wednesday", "Thurseday", "Friday", "Saturday", "Sunday"


""" zip()関数を使うと、複数のリストをまとめてループ処理できます。
要素数が違う場合は少ない方に合わせられます。 """
for (a, b) in zip(lst, lst2):
		print(a, b)


for i, (a, b) in enumerate(zip(lst, lst2),1):
		print(i, a, b)


lst3 = [1, 2, 3],[4, 5, 6],[7, 8, 9]

""" 行、列変換 """
for (a, b, c) in zip(*lst3):
		print(a, b, c)


#文字列をfor文で表示すると、一文字づつ取り出されます。
str = "Japan"
for s in str:
		print(s)


""" ---------------------------
リスト内表記方
--------------------------"""
print("""
ーーーリスト内表記ーーー""")
print([i for i in range(0,10)])


""" ---------------------------
ジェネレータ式表記方
式 for ターゲットリスト in 反復可能オブジェクト
--------------------------"""
print("""
ーーージェネレータ式表記ーーー""")
print(i for i in range(0,10))


