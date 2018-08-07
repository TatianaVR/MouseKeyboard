
import pyautogui
print('Press Ctrl-F2 to quit.')
x, y = pyautogui.position()
positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
print('\ nDone.')
print(positionStr)

