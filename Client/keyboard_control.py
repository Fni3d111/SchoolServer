import pyautogui
import keyboard

def press(pressed_keybinds):
    print('should write!')
    print(pressed_keybinds)
    for x in pressed_keybinds:
        pyautogui.write(x)


def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s))


def combo_control(combo):
    for x in combo:
        pyautogui.keyDown(x)
    for x in combo:
        pyautogui.keyUp(x)




