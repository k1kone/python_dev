#!python3
#Googleの検索結果をいくつかひらく


#引数を検索ワードとして取得する

import webbrowser, requests, sys, bs4

baseUrl = 'https://google.co.jp'

if len(sys.argv) > 1:
	print('Google....')
	res = requests.get(baseUrl + '/search?q=' + ' '.join(sys.argv[1:]))
	res.raise_for_status()

#TODO:上位の検索結果の取得

soup = bs4.BeautifulSoup(res.text)
link_elm = soup.select('.r a')

#for i in link_elm:
#	print(i)

num_open = min(5, len(link_elm))

for i in range(num_open):
		webbrowser.open(baseUrl + link_elm[i].get('href'))
