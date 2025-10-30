# PraktiCalc - a calculator with GUI I started at my student internship in 2024
# Copyright (C) 2024-2025 karl152
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

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import time
import threading
from pathlib import Path
import os

def actuallyUninstall():
    username = os.getlogin()
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
    Window.destroy()

Window = tk.Tk()
Window.title("Uninstalling...")
Desc = ttk.Label(Window, text="Please wait...")
Progress = ttk.Progressbar(Window, mode="indeterminate", length=220)
Progress.start()
Desc.pack(padx=20, pady=10)
Progress.pack(padx=20, pady=10)
threading.Thread(target=actuallyUninstall, daemon=True).start()
Window.mainloop()
