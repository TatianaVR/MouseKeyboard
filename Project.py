
import pyautogui
print('Press Ctrl-F2 to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
except KeyboardInterrupt:
    print('\ nDone.')
    print(positionStr)

