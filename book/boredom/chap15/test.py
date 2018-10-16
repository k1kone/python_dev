#!python3

import requests, bs4, os, time

start_time = time.time()

baseUrl = 'https://xkcd.com'

res = requests.get(baseUrl)
res.raise_for_status()

print('\n >> Access to {} .............\n'.format(baseUrl))

soup = bs4.BeautifulSoup(res.text)
prev = soup.select('a[rel="prev"]')[0].get('href')
os.makedirs('xkcd', exist_ok=True)


while not str(prev).endswith('#'):
	print('\n >> Access to {} .............\n'.format(baseUrl + prev))
	img_elm = 'http:' + soup.select('#comic img')[0].get('src')
	res = requests.get(img_elm)
	res.raise_for_status()

	print('\n >> Writing image file: {} .............\n'.format(img_elm))
	img_file = open(os.path.join('xkcd/','xkcd_' + os.path.basename(img_elm)), 'wb')
	for i in res.iter_content(100000):
		img_file.write(i)

	pastime = round(time.time() - start_time)
	start_time = time.time()
	print('past time : {}'.format(pastime))
	res = requests.get(baseUrl + prev)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text)
	prev = soup.select('a[rel="prev"]')[0].get('href')
	
print('\n>> Complete.\n')	
