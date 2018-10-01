#一行での記述
txt = "Hello world Python!"

#複数行での記述 """〜 """で挟む
txt2 = """
Goodby,world.
Hello Python.
"""
print(txt)
print(txt2)

#########書式指定いろいろ################
# zfill で桁数を指定して0詰め番号記述
print('5'.zfill(5))  #00005
print(str(101).zfill(5)) #00101

# format を使った書式指定
print("hello {0:05d} world.".format(5)) #hello 00005 world.

###########エスケープ#################
#ビープ音
print('escape sample01 \'.')
print('escape sample02 \a.')

#改行、エスケープ記号のエスケープ
print('escape sample03 \n.')
print('escape sample04 \\.')

##############文字取得#################
#txtの先頭5文字目を取得
print(txt[4])
#txtの後ろから5文字目を取得
print(txt[-3])


#[x:y] x〜yまでを取得
print(txt[3:6])

#[x:] x以降を取得
print(txt[3:])

#[:y] y以前を取得
print(txt[:3])

#replace をつかって文字を入れ替え
print(txt.replace("o","O"))
print(txt.replace("world","new world"))


##############文字検索#################
# '検索したい文字' in 文字列が格納された変数
"JAVA" in txt #文字が含まれていれば True、そうでなければ False を返す

if("Python" in txt):
		print('in the "Python"!!!')

# find('検索したい文字') で該当文字の順番を検索
txt.find('o') #見つからない場合は-1を返す

txt.find('o',10) #指定数飛ばして検索

txt.rfind('o') #右側から検索


##########文字を取り除く##############

# strip で改行コード、タブを取り除く
print(txt2.strip()) # strip() の引数を省略した場合は文字列前後の空白とタブ、改行が取り除かれます。


print(txt2.strip('o')) #引数に文字列を指定すると、指定したものが取り除かれます。

# split() を使って文字列を区切る
print(txt2.split(','))


"""
特定の区切りで文字列を分割して文字列のリストにする例
（CSVやログ解析などでつかうテクニック）
"""
txt3 = """1, taro, 35, male
2, jiro, 29, male
3, hanako, 23, female"""

for line in txt3.split('\n'):
		elems = line.split(',')
		print(elems)
		print('{} {}'.format(elems[1].strip(), elems[2].strip()))


#########特定の文字列で結合############
# join() でリストないの要素を指定文字で結合
#2次元配列に格納された情報をＣＳＶに書き出す際などに利用
lis = ['1', 'taro', '35', 'male']
print(', '.join(lis)) #1, taro, 35, male


###########ファイル処理################

f = open('text.txt', 'r') #'r' で読み込みでファイルを開く
print(type(f))

for line in f: # for文でファイルの中身を1行ごと取得
		print('hello ' + line)

f.close()

#ファイルを丸ごと読み込む
f2 = open('text.txt','r') #read()関数をつかうことでファイルの中身すべてを文字列として取得することができます。

text = f2.read()
print(text)

lines = text.split('\n')
print(lines)

f2.close()


