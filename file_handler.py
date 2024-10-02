# file_handler.py
import threading
import time

lock = threading.Lock()

def read_file(filename):
    if lock.acquire(timeout=5):  # Wait for 5 seconds to acquire the lock
        try:
            with open(filename, 'r') as file:
                data = file.read()
                print(f"{threading.current_thread().name} read data: {data}")
            time.sleep(2)
        finally:
            lock.release()
    else:
        print(f"{threading.current_thread().name} could not acquire lock, aborting.")

def write_file(filename, content):
    if lock.acquire(timeout=5):  # Wait for 5 seconds to acquire the lock
        try:
            with open(filename, 'a') as file:
                file.write(content)
                print(f"{threading.current_thread().name} wrote data: {content}")
            time.sleep(2)
        finally:
            lock.release()
    else:
        print(f"{threading.current_thread().name} could not acquire lock, aborting.")