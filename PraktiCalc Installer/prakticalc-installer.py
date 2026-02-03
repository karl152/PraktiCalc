# PraktiCalc - a practical calculator written in Python
# Copyright (C) 2024-2025 Karl "karl152"
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

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import subprocess
import platform
import ctypes
import sys
import zipfile
import getpass
import shutil
from pathlib import Path
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

def speak(string):
    subprocess.Popen(["wscript", narrator, string])
def speakAndWait(string):
    subprocess.run(["wscript", narrator, string])
auto = "--auto" in sys.argv
TTS = "--TTS" in sys.argv
if Path("C:/Program Files/PraktiCalc").exists() == True:
    UninstallBaseString = "PraktiCalc is already installed on your system. If you want to reinstall or update it, please uninstall it first using "
    UninstallWinString = "Control Panel -> Programs -> Programs and Features -> PraktiCalc -> Uninstall/Change"
    UninstallWin11String = "Settings -> Apps -> Installed Apps -> PraktiCalc -> Uninstall"
    if platform.release() == "11":
        messagebox.showerror("Not installing", UninstallBaseString + UninstallWin11String)
    else:
        messagebox.showerror("Not installing", UninstallBaseString + UninstallWinString)
    sys.exit(1)

if auto == False:
    WizardPage = 0
else:
    WizardPage = 6

def testPyInstallerOneFile():
    try:
        print(sys._MEIPASS)
        return True
    except:
        return False

RunningAsOneFileExe = testPyInstallerOneFile()
if RunningAsOneFileExe == True:
    PraktiCalcBannerPath = (sys._MEIPASS + "/PraktiCalcBanner.png")
    PraktiCalcContentZIPPath = (sys._MEIPASS + "/PraktiCalcProgramContent.zip")
    licensefile = (sys._MEIPASS + "/LICENSE")
    narrator = (sys._MEIPASS + "/narrator.vbs")
else:
    PraktiCalcBannerPath = "PraktiCalcBanner.png"
    PraktiCalcContentZIPPath = "PraktiCalcProgramContent.zip"
    licensefile = "../LICENSE"
    narrator = "narrator.vbs"
    print("""
----------------------------------------------------------
 WARNING: The PraktiCalc Installer will likely not work
 when not built to one file using PyInstaller! You should
 build it before execution using the provided script
----------------------------------------------------------
""")
    if TTS == True:
        speakAndWait("WARNING: The PraktiCalc Installer will likely not work when not built to one file using PyInstaller! You should build it before execution using the provided script")

if "--help" in sys.argv:
    print("""PraktiCalc Installer CLI Options:
--auto: starts automatic installation
--TTS: starts installer with text to speech
--help: shows this help text""")
    sys.exit(0)

ExtractTo = "C:/Program Files/PraktiCalc"
username = getpass.getuser()

def forward():
    global WizardPage
    if WizardPage == 6:
        pass
    else:
        WizardPage += 1
        pageReload()
def back():
    global WizardPage
    if WizardPage == 0:
        pass
    else:
        WizardPage -= 1
        pageReload()
def pageReload():
    global WizardPage
    if WizardPage == 0:
        MainFrame.columnconfigure(0, weight=0)
        MainFrame.rowconfigure(1, weight=0)
        MainFrame.config(text="Welcome")
        clearMainFrame()
        InstallWizardWindow.geometry("408x420")
        WelcomeImage = ttk.Label(MainFrame, image=InstallWizardWindow.Banner)
        WelcomeText = ttk.Label(MainFrame, text="Welcome to the PraktiCalc Installer for Windows!\nThis Wizard will help you installing PraktiCalc.")
        WelcomeImage.grid(row=0, column=0)
        WelcomeText.grid(row=1, column=0, padx=10, pady=10)
        if TTS == True:
            speak("Welcome to the PraktiCalc Installer for Windows! This Wizard will help you installing PraktiCalc.")
    elif WizardPage == 1:
        MainFrame.config(text="License")
        MainFrame.columnconfigure(0, weight=1)
        MainFrame.rowconfigure(1, weight=1)
        clearMainFrame()
        InstallWizardWindow.geometry("870x620")
        LicensePreText = ttk.Label(MainFrame, text="This software is licensed under the GNU General Public License, Version 3.\nContinue if you accept that.")
        LicenseText = tk.Text(MainFrame, wrap="word")
        LicenseTextScrollbar = ttk.Scrollbar(MainFrame, orient="vertical", command=LicenseText.yview)
        LicenseText.configure(yscrollcommand=LicenseTextScrollbar.set)
        with open(licensefile, "r") as LicenseToInsert:
            LicenseText.insert(tk.END, LicenseToInsert.read())
        LicenseText.config(state="disabled")
        LicensePreText.grid(row=0, column=0, padx=10, pady=10)
        LicenseText.grid(row=1, column=0, padx=10, pady=10, sticky="nesw")
        LicenseTextScrollbar.grid(row=1, column=1, padx=10, pady=10, sticky="nes")
        if TTS == True:
            speak("This software is licensed under the GNU General Public License, Version 3. Continue if you accept that.")
    elif WizardPage == 2:
        MainFrame.config(text="Destination")
        MainFrame.columnconfigure(0, weight=0)
        MainFrame.rowconfigure(1, weight=0)
        clearMainFrame()
        InstallWizardWindow.geometry("408x420")
        DestinationText = ttk.Label(MainFrame, text="PraktiCalc will be installed into the following directory:")
        DestinationText.grid(row=0, column=0, padx=10, pady=10)
        DestinationPathFrame = ttk.Frame(MainFrame, borderwidth=1, relief="sunken")
        DestinationPathFrame.grid(row=1, column=0, padx=10, pady=10)
        DestinationPathLabel = ttk.Label(DestinationPathFrame, text="C:/Program Files/PraktiCalc")
        DestinationPathLabel.grid(row=0, column=0, padx=2, pady=2)
        if TTS == True:
            speak("PraktiCalc will be installed into the following directory: C:/Program Files/PraktiCalc")
    elif WizardPage == 3:
        MainFrame.config(text="Desktop Shortcut")
        clearMainFrame()
        DesktopShortcutText = ttk.Label(MainFrame, text="Do you want to create a Desktop Shortcut for PraktiCalc?")
        DesktopShortcutText.grid(row=0, column=0, padx=10, pady=10)
        DesktopShortcutOptionYes = ttk.Radiobutton(MainFrame, text="Yes", value=True, variable=DesktopShortcut)
        DesktopShortcutOptionYes.grid(row=1, column=0, padx=10)
        DesktopShortcutOptionNo = ttk.Radiobutton(MainFrame, text="No", value=False, variable=DesktopShortcut)
        DesktopShortcutOptionNo.grid(row=2, column=0, padx=10)
        if TTS == True:
            speak("Do you want to create a Desktop Shortcut for PraktiCalc?")
    elif WizardPage == 4:
        MainFrame.config(text="Start Menu Entry")
        clearMainFrame()
        DesktopShortcutText = ttk.Label(MainFrame, text="Do you want to add PraktiCalc to the Start Menu?")
        DesktopShortcutText.grid(row=0, column=0, padx=10, pady=10)
        DesktopShortcutOptionYes = ttk.Radiobutton(MainFrame, text="Yes", value=True, variable=StartMenuEntry)
        DesktopShortcutOptionYes.grid(row=1, column=0, padx=10)
        DesktopShortcutOptionNo = ttk.Radiobutton(MainFrame, text="No", value=False, variable=StartMenuEntry)
        DesktopShortcutOptionNo.grid(row=2, column=0, padx=10)
        if TTS == True:
            speak("Do you want to add PraktiCalc to the Start Menu?")
    elif WizardPage == 5:
        MainFrame.config(text="Ready for installation")
        clearMainFrame()
        ReadyText = ttk.Label(MainFrame, text="PraktiCalc is now ready to be installed.\nYour choices:")
        DestinationChoiceText = ttk.Label(MainFrame, text="- Install PraktiCalc to C:/Program Files/PraktiCalc")
        DesktopShortcutChoice = ttk.Label(MainFrame)
        StartMenuEntryChoice = ttk.Label(MainFrame)
        if DesktopShortcut.get() == True:
            DesktopShortcutChoice.config(text="- add a shortcut to the Desktop")
        else:
            DesktopShortcutChoice.config(text="- don't add a shortcut to the Desktop")
        if StartMenuEntry.get() == True:
            StartMenuEntryChoice.config(text="- add an entry to the Start Menu")
        else:
            StartMenuEntryChoice.config(text="- don't add an entry to the Start Menu")
        FinalAdvise = ttk.Label(MainFrame, text="Click continue to start the installation.")
        ReadyText.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        DestinationChoiceText.grid(row=1, column=0, padx=10, sticky="w")
        DesktopShortcutChoice.grid(row=2, column=0, padx=10, sticky="w")
        StartMenuEntryChoice.grid(row=3, column=0, padx=10, sticky="w")
        FinalAdvise.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        if TTS == True:
            speak("PraktiCalc is now ready to be installed like you chose in the previous screens. Click continue to start the installation.")
    elif WizardPage == 6:
        global Progress, InstallProgressText
        MainFrame.config(text="Installing PraktiCalc...")
        clearMainFrame()
        InstallText = ttk.Label(MainFrame, text="PraktiCalc is being installed. Please wait.\nThis process should take less than a minute.")
        InstallProgressText = tk.Label(MainFrame, bg="black", fg="white", font=("Lucida Console", 10))
        InstallText2 = ttk.Label(MainFrame, text="Please don't close this window.")
        InstallText.grid(row=0, column=0, padx=10, pady=10)
        InstallProgressText.grid(row=1, column=0, padx=10, pady=10)
        InstallText2.grid(row=2, column=0, padx=10, pady=10)
        for widgets in BottomFrame.winfo_children():
            widgets.destroy()
        Progress = ttk.Progressbar(BottomFrame, mode="indeterminate")
        Progress.start(10)
        Progress.grid(row=0, column=0, columnspan=2, sticky="esw")
        threading.Thread(target=actuallyInstall, daemon=True).start()
        if auto == False and TTS == True:
            speakAndWait("PraktiCalc is being installed. Please wait.\nThis process should take less than a minute.")
    elif WizardPage == 7:
        if auto == True:
            InstallWizardWindow.destroy()
        else:
            MainFrame.config(text="Installation finished")
            clearMainFrame()
            FinishIcon = tk.Label(MainFrame, text="ü", font=("Wingdings", 32))
            FinishText = ttk.Label(MainFrame, text="Installation successfull!\nPraktiCalc was installed")
            FinishIcon.grid(row=0, column=0, padx=50, pady=10)
            FinishText.grid(row=1, column=0, padx=20, pady=10)
            for widgets in BottomFrame.winfo_children():
                widgets.destroy()
            FinishButton = ttk.Button(BottomFrame, text="Close", command=lambda: InstallWizardWindow.destroy())
            FinishButton.grid(row=0, column=0, columnspan=2, sticky="esw")
            InstallWizardWindow.geometry("170x170")
            if TTS == True:
                speak("PraktiCalc was installed, you can close this window now")
def actuallyInstall():
    global Progress, InstallProgressText, WizardPage
    ProgressText = "checking system compatibility..."
    InstallProgressText.config(text=ProgressText)
    if platform.system() == "Windows":
        Progress.stop()
        Progress.config(mode="determinate", maximum=13, value=1)
        ProgressText += ("\ncorrect operating system: " + platform.system())
        InstallProgressText.config(text=ProgressText)
        if platform.release() == "Vista" or "7" or "8" or "8.1" or "10" or "11":
            Progress.config(value=2)
            ProgressText += ("\ncorrect Windows version: " + platform.release())
            InstallProgressText.config(text=ProgressText)
            ProgressText += "\ncreating installation directory...\n"
            InstallProgressText.config(text=ProgressText)
            Path("C:/Program Files/PraktiCalc").mkdir(parents=True, exist_ok=True)
            Progress.config(value=3)
            ProgressText += "\nmoving PraktiCalc program files...\n"
            InstallProgressText.config(text=ProgressText)
            with zipfile.ZipFile(PraktiCalcContentZIPPath, 'r') as ZipRef:
                ZipRef.extractall(ExtractTo)
            Progress.config(value=4)
            ProgressText += "\nregistering program..."
            InstallProgressText.config(text=ProgressText)
            print(subprocess.getoutput(r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\PraktiCalc" /f'))
            Progress.config(value=5)
            print(subprocess.getoutput(r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\PraktiCalc" /v DisplayName /t REG_SZ /d "PraktiCalc" /f'))
            Progress.config(value=6)
            print(subprocess.getoutput(r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\PraktiCalc" /v DisplayVersion /t REG_SZ /d "1.4" /f'))
            Progress.config(value=7)
            print(subprocess.getoutput(r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\PraktiCalc" /v UninstallString /t REG_SZ /d "C:\Program Files\PraktiCalc\PraktiCalcUninstaller\PraktiCalcUninstaller.exe" /f'))
            Progress.config(value=8)
            print(subprocess.getoutput(r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\PraktiCalc" /v Publisher /t REG_SZ /d "karl152" /f'))
            Progress.config(value=9)
            print(subprocess.getoutput(r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\PraktiCalc" /v InstallLocation /t REG_SZ /d "C:\Program Files\PraktiCalc" /f'))
            Progress.config(value=10)
            print(subprocess.getoutput(r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\PraktiCalc" /v DisplayIcon /t REG_SZ /d "C:\Program Files\PraktiCalc\PraktiCalc.exe" /f'))
            Progress.config(value=11)
            if StartMenuEntry.get() == True:
                ProgressText += "\ncreating start menu entry..."
                InstallProgressText.config(text=ProgressText)
                shutil.copy(ExtractTo + "/PraktiCalc.url", "C:/ProgramData/Microsoft/Windows/Start Menu/Programs")
            Progress.config(value=12)
            if DesktopShortcut.get() == True:
                ProgressText += "\ncreating desktop shortcut..."
                InstallProgressText.config(text=ProgressText)
                shutil.copy(ExtractTo + "/PraktiCalc.url", "C:/Users/" + username + "/Desktop")
            Progress.config(value=13)
            WizardPage = 7
            pageReload()
        else:
            InstallWizardWindow.destroy()
            messagebox.showerror("Incompatible Windows Version", "The Windows Version you are using is not supported by the PraktiCalc Installer.\nThis installer only supports Windows Vista, 7, 8, 8.1, 10 and 11. \n\nIf your Windows Version is older, I am sorry.\nIf your Windows Version is newer than 11, you should be able to run this Installer in Compatibility Mode, which you can enable in the file properties.")
            exit()
    else:
        InstallWizardWindow.destroy()
        messagebox.showerror("Compatibility Error", "This installer is for Windows only. Downlaod the AppImage or the specific package if you're on Linux to install PraktiCalc. There are no packages for MacOS, as I don't have Apple Hardware to test and Build PraktiCalc for MacOS.\n\nIf you want to build this installer yourself, please note that you can only do that on Windows (maybe with Wine on Linux, just maybe)")
        exit()
def clearMainFrame():
    for widget in MainFrame.winfo_children():
        widget.destroy()
InstallWizardWindow = tk.Tk()
DesktopShortcut = tk.BooleanVar()
StartMenuEntry = tk.BooleanVar(value=True)
InstallWizardWindow.Banner = tk.PhotoImage(file=PraktiCalcBannerPath)
InstallWizardWindow.title("PraktiCalc Installer")
InstallWizardWindow.columnconfigure(0, weight=1)
InstallWizardWindow.rowconfigure(0, weight=1)
MainFrame = ttk.LabelFrame(InstallWizardWindow, text="Error, close this window now!")
MainFrame.grid(row=0, column=0, sticky="nesw")
BottomFrame = ttk.Frame(InstallWizardWindow)
BottomFrame.grid(row=1, column=0, sticky="nesw")
BottomFrame.columnconfigure(0, weight=1)
BottomFrame.columnconfigure(1, weight=1)
BottomFrame.rowconfigure(0, weight=1)
PrevButton = ttk.Button(BottomFrame, text="<< Back", command=back)
NextButton = ttk.Button(BottomFrame, text="Continue >>", command=forward)
PrevButton.grid(row=0, column=0, sticky="esw")
NextButton.grid(row=0, column=1, sticky="esw")
pageReload()
InstallWizardWindow.mainloop()
