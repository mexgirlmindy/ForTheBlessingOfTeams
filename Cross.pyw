import pyautogui
import time


x, y = pyautogui.size()
Father = ((x/2) ,(y/6) )
Son = ((x/2) ,((y/6)*5) )
Holy = ((x/6) ,(y/2) )
Spirit = (((x/6)*5) ,(y/2) )
Amen = ((x/2) ,(y/2) )


for x in range(1000):
    pyautogui.moveTo (Father[0] , Father[1], 2)
    pyautogui.moveTo (Son[0] , Son[1], 2)
    pyautogui.moveTo (Holy[0] , Holy[1], 2)
    pyautogui.moveTo (Spirit[0] , Spirit[1], 2)
    pyautogui.moveTo (Amen[0] , Amen[1], 2)
    time.sleep(240)
