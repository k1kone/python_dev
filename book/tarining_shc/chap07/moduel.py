import sys
sys.dont_write_bytecode = True #モジュール実行時にpycファイルを生成させない

"""
pythonではモジュールをimportするとデフォルトで
インタープリンターがソースコードをバイトコードに変換した結果を
.pycファイルに書き出すようになっています。

python3 より「__pycache__」というディレクトリに
保存されるようになりました。

pycファイルにはバージョン毎の互換性がありません。
同じスクリプトをバージョンを変えて実行させた場合、
.pycファイルが上書きされるので注意してください。

.pycファイル（および__pycache__）を生成させたくない場合は、
シェルスクリプトでファイルを実行する場合は

python -B file.py

と記述してください。ファイル内に

import sys
sys.dont_write_bytecode = True 
と記入することでも可能です。

.pycファイル（および__pycache__）をショルスクリプトで
削除する場合は、

find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

を実行してください

●　.pycファイルが存在すれば、python実行時のバイトコードへの
コンパイルが省略されます。存在しなければ都度コンパイルが走ります。

● 同じバージョンであれば生成されたpycファイルを他環境で実行可能です。
ソースを見せたくないときなどはこの方法で。

● .pycファイルが存在しなくても特に問題はありません。
あくまでimportの速度が早くなるだけで、本ソースの処理速度が
上がるわけではありません。

"""

from test_class import testCl
from datetime import date

class clSub(testCl):
	def __init__(self, name, math=0, jap=0, eng=0, birth=0):
		self.__birth = birth
		super().__init__(name, math, jap, eng)

	def birthPrint(self):
		print("birthday:{}".format(self.__birth))


ichiro = clSub('ichiro', 30, 40, 56, date(1988, 4, 30))

ichiro.info()
ichiro.birthPrint()
