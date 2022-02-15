import pyautogui

def organize(command):
    if command == 'desktop':
        pyautogui.hotkey('win','d')