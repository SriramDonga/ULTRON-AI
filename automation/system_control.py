import subprocess


class SystemController:

    def open_calculator(self):
        subprocess.Popen("calc.exe")

        return "Calculator opened."