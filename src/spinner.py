import threading
import time
import sys

# Spinner function
def spinner_task(stop_event):
    spinner = ['|', '/', '-', '\\', '_']
    i = 0
    while not stop_event.is_set():
        sys.stdout.write(f"\rLoading {spinner[i % len(spinner)]}")
        sys.stdout.flush()
        i += 1
        time.sleep(0.1)
    # Clear the line before printing final message
    sys.stdout.write("\r" + " " * 20 + "\r")
    sys.stdout.write("Dataset Loaded!\n")