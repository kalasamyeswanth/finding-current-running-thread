import threading
print('let us find the current thread')
print('current running thread :',threading.current_thread().getName())
print('the getName()',threading.gettrace)
if(threading.current_thread() == threading.main_thread()):
    print('the current thread is the main thread')
    print('threading.current_thread()-->',threading.current_thread())
    print('threading.main_thread()-->',threading.main_thread())
else:
    print('the current thread is not main thread :')
    
