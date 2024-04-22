import time

def countdown(t):
    while t:
        min, secs = divmod(t,60)
        timer = "{:02d}:{:02d}".format(min,secs)
        print(timer, end = "\r")
        time.sleep(1)
        t -= 1
