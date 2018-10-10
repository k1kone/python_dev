#!python3

import requests, bs4, webbrowser, os

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
	print('downloading now...{}'.format(url))
	res = requests.get(url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text)
	comicImg = soup.select('#comic img')
	if comicImg == []:
		print('it is not image')
	else:
		comicUrl = 'http:' + comicImg[0].get('src')
		print('downloading now...{}'.format(comicUrl))
		res = requests.get(comicUrl)
		res.raise_for_status()
		image_file = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
		for chunk in res.iter_content(100000):
			image_file.write(chunk)
		image_file.close()
	prev_link = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prev_link.get('href')
print('complete.')
