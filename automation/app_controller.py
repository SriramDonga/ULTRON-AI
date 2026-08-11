import subprocess
import time

import pyautogui


class AppController:

    def open_calculator(self):
        subprocess.Popen("calc.exe")
        time.sleep(2)
        return "Calculator opened."

    def open_notepad(self):
        subprocess.Popen("notepad.exe")
        time.sleep(2)
        return "Notepad opened."

    def open_browser(self):
        subprocess.Popen("start msedge", shell=True)
        time.sleep(3)
        return "Browser opened."

    def type_text(self, text):
        pyautogui.write(text, interval=0.03)

    def press(self, key):
        pyautogui.press(key)

    def hotkey(self, *keys):
        pyautogui.hotkey(*keys)

    def wait(self, seconds=1):
        time.sleep(seconds)