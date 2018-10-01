import os #osモジュールをインポート

##########現在のパスを取得#############
print(os.getcwd()) #getcwd()関数は現在のパスを文字列として返します。

os.chdir('../') #ディレクトリの移動
print(os.getcwd())




##########絶対パスを取得#############
print(os.path.abspath('./'))
print(os.path.abspath('python_dev'))
print(os.path.abspath('shell.py'))

