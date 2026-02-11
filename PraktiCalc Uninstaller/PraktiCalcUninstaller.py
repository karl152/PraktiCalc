# PraktiCalc - a practical calculator written in Python
# Copyright (C) 2024-2026 Karl "karl152"
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# SPDX-License-Identifier: GPL-3.0

import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import threading
from pathlib import Path
import getpass

class Uninstaller(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Uninstalling...")
        self.Icon = tk.Label(self, text="6", font=("Wingdings", 32))
        self.Desc = ttk.Label(self, text="Please wait...")
        self.Progress = ttk.Progressbar(self, mode="indeterminate", length=300)
        self.Progress.start()
        self.Icon.pack(padx=50, pady=10)
        self.Desc.pack(padx=20, pady=5)
        self.Progress.pack(padx=20, pady=10)
        threading.Thread(target=self.uninstall, daemon=True).start()
    def uninstall(self):
        username = getpass.getuser()
        try:
            subprocess.getoutput(r'reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\PraktiCalc" /f')
            subprocess.getoutput('rmdir /S /Q "C:\Program Files\PraktiCalc"')
            Path("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/PraktiCalc.url").unlink(missing_ok=True)
            Path("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/PraktiCalc.lnk").unlink(missing_ok=True)
            Path("C:/Users/" + username + "/Desktop/PraktiCalc.url").unlink(missing_ok=True)
            Path("C:/Users/" + username + "/Desktop/PraktiCalc.lnk").unlink(missing_ok=True)
            FinishUninstall = r'cmd /c echo Finishing Uninstallation... && timeout /t 2 > NUL && rmdir /S /Q "C:\Program Files\PraktiCalc"'
            subprocess.Popen(FinishUninstall)
        except:
            messagebox.showerror("Error", "Error during uninstall.\nTry running C:/Program Files/PraktiCalc/PraktiCalcUninstaller.exe as Administrator.")
        self.destroy()

if __name__ == "__main__":
    Uninstaller = Uninstaller()
    Uninstaller.mainloop()
