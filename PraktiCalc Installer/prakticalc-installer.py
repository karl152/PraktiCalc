# PraktiCalc © 2024-2026 Karl Wesseler
# Licensed under the GNU General Public License v3.0.
# See https://www.gnu.org/licenses/gpl-3.0.txt for details.
# SPDX-License-Identifier: GPL-3.0-only

import wx, threading, subprocess, platform, ctypes, sys, zipfile, shutil, winreg
from wx.lib.agw.thumbnailctrl import ScrolledTextDialog
from pathlib import Path
from packaging.version import Version
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

PraktiCalcVersion = "1.6"

def testPyInstallerOneFile():
    try:
        print(sys._MEIPASS)
        return True
    except:
        return False

if testPyInstallerOneFile():
    PraktiCalcBannerPath = (sys._MEIPASS + "/PraktiCalcBanner.png")
    PraktiCalcContentZIPPath = (sys._MEIPASS + "/PraktiCalcProgramContent.zip")
    licensefile = (sys._MEIPASS + "/LICENSE")
else:
    PraktiCalcBannerPath = "PraktiCalcBanner.png"
    PraktiCalcContentZIPPath = "PraktiCalcProgramContent.zip"
    licensefile = "../LICENSE"
    print("""
----------------------------------------------------------
 WARNING: The PraktiCalc Installer will likely not work
 when not built to one file using PyInstaller! You should
 build it before execution using the provided script
----------------------------------------------------------
""")

class MainWindow(wx.Frame):
    def __init__(self):
        super().__init__(None, title="PraktiCalc Installer")
        self.panel = wx.Panel(self)
        self.BannerPNG = wx.Bitmap(PraktiCalcBannerPath)
        self.Banner = wx.StaticBitmap(self.panel, bitmap=self.BannerPNG)
        self.MenuEntryCheckbox = wx.CheckBox(self.panel, label="Add a start menu entry")
        self.DesktopIconCheckbox = wx.CheckBox(self.panel, label="Create a desktop shortcut")
        self.ResetSettingsCheckbox = wx.CheckBox(self.panel, label="Reset settings")
        self.MenuEntryCheckbox.SetValue(True)
        if Path("C:/Program Files/PraktiCalc").exists():
            self.UninstallFirst = True
        else:
            self.UninstallFirst = False
            self.ResetSettingsCheckbox.Disable()
        if "--auto" in sys.argv:
            ProgressWindow(self.UninstallFirst, self.MenuEntryCheckbox.GetValue(), self.DesktopIconCheckbox.GetValue(), self.ResetSettingsCheckbox.GetValue()).Show()
            self.Close()
        self.LicenseButton = wx.Button(self.panel, label="License")
        self.InstallButton = wx.Button(self.panel, label="Install")
        self.LicenseButton.Bind(wx.EVT_BUTTON, self.showLicense)
        self.InstallButton.Bind(wx.EVT_BUTTON, self.startInstall)
        self.sizer = wx.GridBagSizer(5, 5)
        self.sizer.Add(self.Banner, pos=(0, 0), span=(1, 3), flag=wx.EXPAND)
        self.sizer.AddGrowableCol(1)
        for i, element in enumerate((self.MenuEntryCheckbox, self.DesktopIconCheckbox, self.ResetSettingsCheckbox)):
            self.sizer.Add(element, pos=(i+1, 1), flag=wx.EXPAND)
        self.sizer.Add(self.LicenseButton, pos=(4, 0), flag=wx.ALL, border=10)
        self.sizer.Add(self.InstallButton, pos=(4, 2), flag=wx.ALIGN_RIGHT | wx.ALL, border=10)
        self.panel.SetSizerAndFit(self.sizer)
        self.Fit()
    def showLicense(self, _):
        with open(licensefile) as LicenseFile:
            text = LicenseFile.read()
        dlg = ScrolledTextDialog(self, title="GNU General Public License, Version 3.0", msg=text)
        dlg.ShowModal()
    def startInstall(self, _):
        win = ProgressWindow(self.UninstallFirst, self.MenuEntryCheckbox.GetValue(), self.DesktopIconCheckbox.GetValue(), self.ResetSettingsCheckbox.GetValue())
        win.Show()
        self.Close()

class ProgressWindow(wx.Frame):
    def __init__(self, existingInstall, menu, desktop, reset):
        super().__init__(None, title="Installing PraktiCalc...")
        self.featureList = []
        if existingInstall:
            self.featureList.append("existingInstall")
        self.featureList.extend(["main", "reg"])
        if menu:
            self.featureList.append("menuEntry")
        if desktop:
            self.featureList.append("desktopShortcut")
        if reset:
            self.featureList.append("settingsReset")
        self.panel = wx.Panel(self)
        self.Infobar = wx.InfoBar(self.panel)
        btnID = wx.NewIdRef()
        self.Infobar.AddButton(btnID, "Close")
        self.Infobar.Bind(wx.EVT_BUTTON, lambda _: self.Close(), id=btnID)
        self.DriveIcon = wx.StaticBitmap(self.panel, bitmap=wx.ArtProvider().GetBitmap(wx.ART_HARDDISK, wx.ART_OTHER, wx.Size(64, 64)))
        if existingInstall:
            MainLabel = f"Updating to PraktiCalc {PraktiCalcVersion}"
        else:
            MainLabel = f"Installing PraktiCalc {PraktiCalcVersion}"
        self.InstallText = wx.StaticText(self.panel, label=MainLabel)
        font = self.InstallText.GetFont()
        font.PointSize += 3
        font = font.Bold()
        self.InstallText.SetFont(font)
        self.Progressbar = wx.Gauge(self.panel)
        self.Progressbar.Pulse()
        self.Icons = []
        self.Texts = []
        FeatureTexts = {
            "existingInstall": "removing existing version",
            "main": "copying files",
            "reg": "registering the install",
            "menuEntry": "adding start menu entry",
            "desktopShortcut": "creating desktop shortcut",
            "settingsReset": "resetting the settings"
        }
        self.Icons.append(wx.StaticBitmap(self.panel, bitmap=wx.ArtProvider().GetBitmap(wx.ART_GO_FORWARD, wx.ART_OTHER, wx.Size(16, 16))))
        for _ in self.featureList[:-1]:
            self.Icons.append(wx.StaticBitmap(self.panel))
        for item in self.featureList:
            self.Texts.append(wx.StaticText(self.panel, label=FeatureTexts.get(item)))
        self.sizer = wx.GridBagSizer()
        self.sizer.Add(self.Infobar, pos=(0, 0), span=(1, 2), flag=wx.EXPAND)
        self.sizer.AddGrowableCol(1)
        self.sizer.Add(self.DriveIcon, pos=(1, 0), flag=wx.ALL, border=10)
        self.sizer.Add(self.InstallText, pos=(1, 1), flag=wx.EXPAND | wx.RIGHT, border=200)
        self.sizer.Add(self.Progressbar, pos=(2, 0), span=(1, 2), flag=wx.EXPAND | wx.ALL, border=10)
        for i in range(len(self.featureList)):
            self.sizer.Add(self.Icons[i], pos=(i+3, 0), flag=wx.ALIGN_RIGHT | wx.RIGHT, border=5)
            self.sizer.Add(self.Texts[i], pos=(i+3, 1))
        self.sizer.Add(wx.StaticText(self.panel, label=" "), pos=(len(self.featureList)+3, 1)) # spacer
        self.sizer.AddGrowableRow(len(self.featureList)+2)
        self.panel.SetSizerAndFit(self.sizer)
        self.Fit()
        self.status = 0
        threading.Thread(target=self.install, daemon=True).start()
    def markDone(self):
        self.Icons[self.status].SetBitmap(wx.ArtProvider().GetBitmap(wx.ART_TICK_MARK, wx.ART_OTHER, wx.Size(16, 16)))
        try:
            self.Icons[self.status+1].SetBitmap(wx.ArtProvider().GetBitmap(wx.ART_GO_FORWARD, wx.ART_OTHER, wx.Size(16, 16)))
        except IndexError:
            if "--auto" in sys.argv:
                self.Close()
            else:
                self.Infobar.ShowMessage("Installation completed successfully!", wx.ICON_INFORMATION)
                self.Fit()
        else:
            self.status += 1
    def markError(self, error="There was an error during the installation!"):
        self.Icons[self.status].SetBitmap(wx.ArtProvider().GetBitmap(wx.ART_CROSS_MARK, wx.ART_OTHER, wx.Size(16, 16)))
        if "--auto" in sys.argv:
            self.Close()
        else:
            self.Infobar.ShowMessage(error, wx.ICON_ERROR)
            self.Fit()
    def install(self):
        ExtractTo = "C:/Program Files/PraktiCalc"
        username = Path.home().stem
        if "existingInstall" in self.featureList:
            self.Progressbar.Pulse()
            with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\PraktiCalc") as PraktiKey:
                PrevInstallPath = winreg.QueryValueEx(PraktiKey, "InstallLocation")[0]
                PreviousVersion = winreg.QueryValueEx(PraktiKey, "DisplayVersion")[0]
                if Version(PraktiCalcVersion) < Version(PreviousVersion):
                    messagebox.showerror(parent=InstallWizardWindow, title="Error - Downgrading unsupported", message="You already have a newer version of PraktiCalc installed!")
                    InstallWizardWindow.destroy()
                    exit()
            subprocess.getoutput(r'reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\PraktiCalc" /f')
            try:
                shutil.rmtree(PrevInstallPath)
            except:
                self.markError()
                wx.MessageDialog(self, "Failed to uninstall the previous version of PraktiCalc.\nPlease make sure it's closed and try again.\nIf that doesn't work, restart your PC and try again.\nThank you!", "Uninstallation error", wx.ICON_ERROR).showModal()
                self.Close()
            Path("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/PraktiCalc.url").unlink(missing_ok=True)
            Path("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/PraktiCalc.lnk").unlink(missing_ok=True)
            Path("C:/Users/" + username + "/Desktop/PraktiCalc.url").unlink(missing_ok=True)
            Path("C:/Users/" + username + "/Desktop/PraktiCalc.lnk").unlink(missing_ok=True)
            self.markDone()
        try:
            Path("C:/Program Files/PraktiCalc").mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(PraktiCalcContentZIPPath, 'r') as ZipRef:
                files = []
                for file in ZipRef.infolist():
                    if not file.is_dir():
                        files.append(file)
                self.Progressbar.SetRange(len(files))
                for index, file in enumerate(files, 1):
                    ZipRef.extract(file, ExtractTo)
                    self.Progressbar.SetValue(index)
        except Exception as e:
            self.markError(str(e))
            return
        else:
            self.markDone()
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall", 0, winreg.KEY_WRITE) as UninstallKey:
                with winreg.CreateKey(UninstallKey, "PraktiCalc") as PraktiKey:
                    winreg.SetValueEx(PraktiKey, "DisplayName", 0, winreg.REG_SZ, "PraktiCalc")
                    winreg.SetValueEx(PraktiKey, "DisplayVersion", 0, winreg.REG_SZ, PraktiCalcVersion)
                    winreg.SetValueEx(PraktiKey, "UninstallString", 0, winreg.REG_SZ, r"C:\Program Files\PraktiCalc\PraktiCalcUninstaller.exe")
                    winreg.SetValueEx(PraktiKey, "Publisher", 0, winreg.REG_SZ, "Karl Wesseler")
                    winreg.SetValueEx(PraktiKey, "InstallLocation", 0, winreg.REG_SZ, r"C:\Program Files\PraktiCalc")
                    winreg.SetValueEx(PraktiKey, "DisplayIcon", 0, winreg.REG_SZ, r"C:\Program Files\PraktiCalc\PraktiCalc.exe")
                    winreg.SetValueEx(PraktiKey, "NoModify", 0, winreg.REG_DWORD, 1)
                    winreg.SetValueEx(PraktiKey, "NoRepair", 0, winreg.REG_DWORD, 1)
        except Exception as e:
            self.markError(str(e))
            return
        else:
            self.markDone()
        if "menuEntry" in self.featureList:
            try:
                shutil.copy(ExtractTo + "/PraktiCalc.url", "C:/ProgramData/Microsoft/Windows/Start Menu/Programs")
            except Exception as e:
                self.markError(str(e))
                return
            else:
                self.markDone()
        if "desktopShortcut" in self.featureList:
            try:
                shutil.copy(ExtractTo + "/PraktiCalc.url", "C:/Users/" + username + "/Desktop")
            except Exception as e:
                self.markError(str(e))
                return
            else:
                self.markDone()
        if "settingsReset" in self.featureList:
            try:
                subprocess.getoutput(r'reg delete "HKEY_CURRENT_USER\Software\PraktiCalc" /f')
            except Exception as e:
                self.markError(str(e))
                return
            else:
                self.markDone()

app = wx.App()
if "--help" in sys.argv:
    wx.MessageDialog(None, "--auto: starts an automatic unattended install", f"PraktiCalc {PraktiCalcVersion} Install Options", wx.OK | wx.ICON_INFORMATION).ShowModal()
elif platform.system() == "Windows" and int(platform.win32_ver()[1][0:2]) >= 6:
    frame = MainWindow()
    frame.Show()
    app.MainLoop()
else:
    wx.MessageDialog(None, "This installer is incompatible with your operating system", "Compatibility error", wx.OK | wx.ICON_ERROR).ShowModal()
