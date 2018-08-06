
import pyautogui
pyautogui.size()
(1920, 1080)
width, height = pyautogui.size()

#перемещение мыши
#for i in range(10):
#      pyautogui.moveTo(100, 100, duration=0.25)
#      pyautogui.moveTo(200, 100, duration=0.25)
#      pyautogui.moveTo(200, 200, duration=0.25)
#      pyautogui.moveTo(100, 200, duration=0.25)

#перемещение мыши с текущей координаты
for i in range(10):
      pyautogui.moveRel(100, 0, duration=0.25)
      pyautogui.moveRel(0, 100, duration=0.25)
      pyautogui.moveRel(-100, 0, duration=0.25)
      pyautogui.moveRel(0, -100, duration=0.25)