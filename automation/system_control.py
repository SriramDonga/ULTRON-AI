import os
import webbrowser
from datetime import datetime


class SystemController:

    def open_calculator(self):
        os.system("start calc")
        return "Calculator opened."

    def open_notepad(self):
        os.system("start notepad")
        return "Notepad opened."

    def open_browser(self):
        webbrowser.open("https://www.google.com")
        return "Browser opened."

    def get_time(self):
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    def get_date(self):
        current_date = datetime.now().strftime("%d %B %Y")
        return f"Today's date is {current_date}."