# boş sayfada çalıştırma !
import pywhatkit
import pyautogui
import time


def mesaj():
    pyautogui.write("selam!!")
    pyautogui.press("enter")

while True:
    mesaj()
    time.sleep(0)



