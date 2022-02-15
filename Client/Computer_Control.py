import pyautogui

data = {
    'desktop':['win','d']
}

def combo_keybinds(command_detector):
    for key,values in data.items():
        if key == command_detector:
            for keybind in values:
                pyautogui.keyDown(keybind)
            for keybind in values:
                pyautogui.keyUp(keybind)
            return
