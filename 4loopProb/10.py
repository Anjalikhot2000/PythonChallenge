#Implement an exponential backoff startegy that doubles the wait time between retries, starting from 1sec, but stops after 5 retries

import time

wait_time=1
max_retries=5
attempts=0

while attempts<max_retries:
    print(f"Attempt {attempts+1}-wait_time {wait_time}")
    time.sleep(wait_time)
    wait_time*=2
    attempts+=1

