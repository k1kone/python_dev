import re

f = open('capital.txt', 'r')
fc = f.read()
print('\n\v--------fc----------\n\v')
print(fc)

regx_c = re.compile(r'(\S\w*)\s*(\S\w*)\s*')
capital = regx_c.findall(fc)
f.close()
print('\n\v--------capital----------\n\v')
print(capital)
#print('{},{}'.format(capital[0][0],capital[0][1]))


cap_dic = {}

print('\n-----catiral for i,j ---------')

for i, j in capital:
	print('{}:{}'.format(i, j))
	cap_dic.setdefault(i, j)

print(cap_dic)


