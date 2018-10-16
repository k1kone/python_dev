import threading, time

print('\nprogram start.\n')
start_time = time.time()

def nap():
	time.sleep(5)
	print('weke up!\n\v')

thread_obj = threading.Thread(target=nap)
thread_obj.start()

print('\n====== program end. =========\n')
end_time =  time.time() - start_time
print('past time : {}'.format(end_time))
