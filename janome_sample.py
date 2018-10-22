"""
========================================
** 日本語解析module janome について **
========================================
・日本語の携帯解析を実行可能
・オープンソース（サードパーティー）
・インストールが手軽 >> pip install janome
※ 参考 mynavi
"""

#Janomeを使うための宣言
from janome.tokenizer import Tokenizer

#Janome のインスタンス生成
tok = Tokenizer()


txt = input('========================================\nJanomeで携帯解析\n========================================\njanomeモデュールをつかってinput入力された日本語を携帯解析します。\n--------------------\n日本語で文章を入力してください:\v\n')


#形態素に分割
tokens = tok.tokenize(txt)

print('\v\n--------------------\n\v【**　解析結果　** 】')
#分析結果を確認
for i in tokens:
	print(i)
