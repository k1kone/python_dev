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
