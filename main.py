from req import *
import time

exe = True
try:
    while exe:
        time.sleep(1)
        send()
        time.sleep(2)
except Exception as e:
    print(f"Error: {e}")
