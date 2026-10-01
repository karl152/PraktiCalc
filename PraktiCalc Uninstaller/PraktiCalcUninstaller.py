# PraktiCalc - a practical calculator written in Python
# Copyright (C) 2024-2026 Karl Wesseler
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
# SPDX-License-Identifier: GPL-3.0-only

import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except:
    pass
import subprocess
import threading
from pathlib import Path
import winreg, wx

class Uninstaller(wx.Dialog):
    def __init__(self):
        super().__init__(None, title="Uninstalling...")
        self.panel = wx.Panel(self)
        self.Spinner = wx.ActivityIndicator(self.panel)
        self.Description = wx.StaticText(self.panel, label="    Uninstalling PraktiCalc [1/2]")
        self.Progressbar = wx.Gauge(self.panel)
        self.Progressbar.Pulse()
        self.sizer = wx.GridBagSizer(5)
        self.sizer.Add(self.Spinner, pos=(0, 0), flag=wx.ALIGN_CENTER | wx.ALL, border=10)
        self.sizer.Add(self.Description, pos=(1, 0), flag=wx.RIGHT, border=200)
        self.sizer.Add(self.Progressbar, pos=(2, 0), flag=wx.EXPAND | wx.ALL, border=20)
        self.panel.SetSizerAndFit(self.sizer)
        self.Fit()
        self.Spinner.Start()
        threading.Thread(target=self.uninstall, daemon=True).start()
    def uninstall(self):
        username = Path.home().stem
        try:
            with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\PraktiCalc") as PraktiKey:
                InstallPath = winreg.QueryValueEx(PraktiKey, "InstallLocation")[0]
            subprocess.getoutput(r'reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\PraktiCalc" /f')
            subprocess.getoutput(f'rmdir /S /Q "{InstallPath}"')
            Path("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/PraktiCalc.url").unlink(missing_ok=True)
            Path("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/PraktiCalc.lnk").unlink(missing_ok=True)
            Path("C:/Users/" + username + "/Desktop/PraktiCalc.url").unlink(missing_ok=True)
            Path("C:/Users/" + username + "/Desktop/PraktiCalc.lnk").unlink(missing_ok=True)
            subprocess.Popen(["powershell.exe", "-NoProfile", "-Command", r'''Write-Host "Uninstalling PraktiCalc [2/2]...";
Write-Host
Write-Host "       If you got feedback or suggestions"
Write-Host "____\  for PraktiCalc, feel free to mail"
Write-Host "----/  them to karldpbkz@gmail.com"
Write-Host "       Thank you!"
Write-Host
Write-Host
Write-Host "Please wait until the uninstallation is finished."
Write-Host
Start-Sleep 5
try {
    Remove-Item "C:\Program Files\PraktiCalc" -Recurse -Force -Verbose -ErrorAction Stop
} catch {
    do {
        Write-Host "Removal failed, trying again in 5 seconds..."
        Write-Host "Please make sure PraktiCalc is closed."
        Start-Sleep 5
        Remove-Item "C:\Program Files\PraktiCalc" -Recurse -Force -Verbose
    } while (-not $?)
}
Write-Host
Write-Host "Uninstallation finished. Thank you for using PraktiCalc!"
Start-Sleep 2
'''])
        except:
            wx.MessageDialog(self, "Error during uninstall.\nTry running C:/Program Files/PraktiCalc/PraktiCalcUninstaller.exe as Administrator.", "Error", wx.ICON_ERROR).ShowModal()
        self.Close()
        self.Destroy()

if __name__ == "__main__":
    app = wx.App()
    Uninstaller = Uninstaller()
    Uninstaller.Show()
    app.MainLoop()
