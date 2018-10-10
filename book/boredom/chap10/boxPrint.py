

def box_print(symbol, width, height):
	if len(symbol) !=1:
		raise Exception('symbol must be one length character.')
	if width < 2:
		raise Exception('width must be more than two.')		
	if height < 2:
		raise Exception('height must be more than two.')		
	print(symbol * width)
	for i in range(height -2):
		print(symbol + ' ' * (width -2) + symbol)
	print(symbol * width)

l =[['*', 4, 4], ['0', 20, 5], ['x', 1, 3], ['ZZ', 3, 3]] 
#for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
for sym, w, h in l:
	try:
		box_print(sym, w, h)
	except Exception as error:
		print('it have happened exception :' + str(error))
