import threading
import time

def calculate_end_persist_top_5_app_single_thread(self):
	# find the 5 top recommended app for each app and persist them in app_info
	print "calculate_end_persist_top_5_app_single_thread()"
	start = time.clock() # start time of processor time

	download_history = self.dict_user_download_history.values()
	for app in self.dict_app_info.keys():
		task = self.create_task(app, download_history)
		task.run()

	end = time.clock() # end time of processor time
	print "time elapsed = " + str( end - start )


def calculate_end_persist_top_5_app_multi_thread(self):
	# find the 5 top recommended app for each app and persist them in app_info
	print "calculate_end_persist_top_5_app_multi_thread()"
	start = time.clock() # start time of processor time

	download_history = self.dict_user_download_history.values()
	for app in self.dict_app_info.keys():
		task = self.create_task(app, download_history)
		thread.start_new_thread(task.run, ())

	end = time.clock() # end time of processor time
	print "time elapsed = " + str( end - start )

class myThread(threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter

	def run(self):
		print "Staring " + self.name
		#get lock to synchronize threads
		threadLock.acquire()
		print_time(self.name, self.counter, 3)
		#free lock to release next thread
		threadLock.release()

def print_time(threadName, delay, counter):
	while counter:
		time.sleep(delay)
		print "%s: %s" % (threadName, time.ctime(time.time()))
		counter -= 1

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new threads
thread1.start()
thread2.start()

#Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
	t.join()
print "Exiting Main Thread"