import time

def delay_print(text):
    for char in text:
        print(char, end = "", flush = True)
        time.sleep(0.05)
