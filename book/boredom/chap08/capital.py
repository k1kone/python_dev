import re

f = open('capital.txt', 'r')
fc = f.read()
fcl = f.readlines()
print('\n\v--------fc----------\n\v')
print(fc)
print('\n\v--------fcl----------\n\v')
for i in fcl:
	print(i)

regx_c = re.compile(r'(\S*\w*)\s(\S*\w*)')
#regx_c = re.compile(r'(\S\w*)\s(\S\w*)\s')
capital = regx_c.findall(fc)
#capital = fc.split('\n')
f.close()
print('\n\v--------capital----------\n\v')
print(capital)
#print('{},{}'.format(capital[0][0],capital[0][1]))







""""
print('\n\v------------------\n\v')

cl = fc.replace('\t','').split('\n')

cl = filter(lambda x:x !='', cl)
#del cl[len(cl)-1]
print('------ after lambda cl list ----')
print(cl)

ca = {}

print('\n\v-------cl list-----------\n\v')

for	date in cl:
	print(date)
	l = date.split()
	print(l)
	ca.setdefault(l[0], l[1])

print('\n\v------------------\n\v')
print(cl)
print('\n\v------------------\n\v')
print(ca)
"""
