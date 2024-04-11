import os
import time


def screen_roll():
    path = "C:\Windows"
    dir_list = os.listdir(path)
    for i in dir_list:
        time.sleep(0.15)
        print(f'{i} \n ')