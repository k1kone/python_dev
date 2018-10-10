#!python3

import webbrowser, requests, sys

baseUrl = 'https://google.co.jp/search?q='

if len(sys.argv) > 1:
	search_word = ' '.join(sys.argv[1:])

webbrowser.open(baseUrl + search_word)
