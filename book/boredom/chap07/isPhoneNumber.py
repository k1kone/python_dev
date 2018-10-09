import sys
import re

if len(sys.argv) < 2:
	print("prease input text after fale's name.")
	exit()
else: txt = sys.argv[1]

comp = re.compile(r'(\d{3})-(\d{3}-\d{3})')
mo = comp.search(txt)

if mo == None :
	print('it is not have phone number.')
	print(txt)
else:
	localNum, mainNum = mo.groups()
	print('phone number :\4{}\nlocal number :\4{}\nmain number :\4{}'.format(mo.group(), localNum, mainNum))	
