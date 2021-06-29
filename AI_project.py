import pyautogui
import time
import keyboard
#import random
import win32api,win32con



def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.07) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    

while keyboard.is_pressed('z') == False:

    try:
        
        if pyautogui.pixel(364, 440)[0] == 0:
            click(364, 440)
        if pyautogui.pixel(418, 440)[0] == 0:
            click(418, 440)
        if pyautogui.pixel(479, 440)[0] == 0:
            click(479, 440)
        if pyautogui.pixel(539, 440)[0] == 0:
            click(539, 440)
    except:
        
        if pyautogui.pixel(364, 440)[0] == 0:
            click(364, 440)
        if pyautogui.pixel(418, 440)[0] == 0:
            click(418, 440)
        if pyautogui.pixel(479, 440)[0] == 0:
            click(479, 440)
        if pyautogui.pixel(539, 440)[0] == 0:
            click(539, 440)
