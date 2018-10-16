#!python3

import time

print('''
press [Enter key] first time: set start time.
press [Enter key] from second time: display rap time.
press [Cntr key] + [c] : stop program.''')

input()
print('\n------------start---------------\n')

start_time = time.time()

last_time = start_time

rap_num =1

try:
	while True:
		input()
		now = time.time()
		rap_time = round(now - last_time, 2)
		total_time = round(now - start_time, 2)

		print('RAP {} :{} | TOTAL :{}'.format(rap_num, rap_time, total_time))
		rap_num +=1
		last_time = now

except KeyboardInterrupt:
	print('\n------------finish---------------\n')
