from multiprocessing import Process
import time

# single process
def ask_user():
	start = time.time()
	user_input = input('Enter your name: ')
	greet = f'Hello, {user_input}'
	print(greet)
	print('ask_user: ', time.time() - start)

def complex_calculation():
	print('Started calculating...')
	start = time.time()
	[x**2 for x in range(20000000)]
	print('complex_calculation: ', time.time() - start)


# one at the time
start = time.time()
ask_user()
complex_calculation()
print('Single thread total time: ', time.time() - start, '\n\n')


# two processes
process = Process(target=complex_calculation)
process.start()

start = time.time()

ask_user()

process.join()  

print('Two process total time: ', time.time() - start)