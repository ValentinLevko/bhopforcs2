#imports#
import keyboard
#from win32gui import GetWindowText, GetForegroundWindow
import pymem
import pymem.process
from colorama import Fore,init
from os import system as cmd
from time import sleep

#init program#
init()
cmd("cls")
cmd("title bhop by hellow7777(Discord)")

#check process
try:
    game = pymem.Pymem("cs2.exe")
# if we can't find the process, exit
except pymem.exception.ProcessNotFound:
    # print error message
    print(">>> CS2 not found.")
    exit()

#method#
def main():
    print(f"[{Fore.BLUE}INFO{Fore.RESET}] Started Bhop.")

    while True:

        if keyboard.is_pressed("space"):
            keyboard.write('space')
            sleep(0.07) #time between jumps (afais this one works the best)
            continue

        sleep(0.02)

#start#
if __name__ == '__main__':
    main()