import pyautogui
from pyautogui import locateOnScreen
import time


pyautogui.press('win')
time.sleep(2)
pyautogui.write('chrome')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)

img = locateCenterOnScreen('botao.PNG')