cats = []

while True:
	name = input('input cat\'s name.(if you want exit:press "Enter"key.)\n')
	if name == '':
		break
	cats = cats + [name]
	
"""
print('all cats name are :')
for n in cats:
	print(n)	
"""

for index,i in enumerate(cats):
	print('{}:{} / length({})'.format(index, i, len(i)))

w = "world"
print(w + ' of length ' + str(len(w)))
