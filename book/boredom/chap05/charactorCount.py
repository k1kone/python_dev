import pprint

message = "Drive'on through street roadblox, let me let me what you've got."
count = {}

for c in message:
	count.setdefault(c, 0)
	count[c] = count[c] + 1

print("""#辞書型は下記のようにfor文で出力することもできますが、

for i, j in count.items():
	print('{}:{}'.format(i, j), end=\", \")

pprint()やpformat()関数を使うとより明確に辞書型の内容を表示できます。
利用するには pprintモジュールをimportしてください。
pprint()ではキーがソートされた状態で出力されます。
辞書の中にリストや辞書が入れ子になっているときに便利です。
pformat()は整形されたテキストを画面に表示せずに文字列として
取得したい場合に利用してください。

pprint.pprint(辞書型)""")
pprint.pprint(count)

