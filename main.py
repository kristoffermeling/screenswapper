import psutil
import os
from ctypes import*
import subprocess
import pathlib
from time import sleep

programs = []
def refresh_programlist():
    with open(r"C:\Users\Kristoffer\PycharmProjects\screenswapper\programs.txt", "r") as f:
        for lines in f:
            programs.append(lines.rstrip())


def add_new_program(processname):
    with open("programs.txt", "a") as f:
        f.writelines(processname+"\n")
    refresh_programlist()

def desktop_mode():
    os.system(r"C:\Users\Kristoffer\PycharmProjects\screenswapper\DisplaySwitchFast.exe /extend")
    print("desktop")

while True:

    refresh_programlist()
    prosss = psutil.Process().children()

    for p in psutil.process_iter():
        try:
            #print(p)
            if p.name() in programs:
                os.system(r"C:\Users\Kristoffer\PycharmProjects\screenswapper\DisplaySwitchFast.exe /external")

                test = p.wait()
                if not test:
                    desktop_mode()


        except psutil.Error:
            pass
    sleep(30)