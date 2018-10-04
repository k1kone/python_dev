countries = ["フランス", "アメリカ", "中国", "ドイツ", "日本"]

""" enumerate関数を使用すると、for文の中でリストの要素と同時に
インデックス番号を取得できます。 """

for index, country in enumerate( countries ):
		print( str(index+1) + " : " + country )


lst = "France", "America", "China", "Dunich", "Japan"

""" enumerate関数のインデックスはデフォルトでは0から始まりますが、
第二引数に任意の開始数値を指定できます。 """
#1から始める場合
for i, l in enumerate(lst , 1 ):
		print(i, l) 


""" format()関数との組み合わせ """

for i , c in enumerate(countries , 100):
		print('{:03}_{}'.format(i, c))
