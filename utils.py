import os
import time


def screen_roll():
    path = "C:\Windows"
    dir_list = os.listdir(path)
    for i in dir_list:
        time.sleep(0.15)
        print(f'{i} \n ')


def delay_print(text):
    for char in text:
        print(char, end = "", flush = True)
        time.sleep(0.05)
        

def countdown(t):
    while t:
        min, secs = divmod(t,60)
        timer = "{:02d}:{:02d}".format(min,secs)
        print(timer, end = "\r")
        time.sleep(1)
        t -= 1