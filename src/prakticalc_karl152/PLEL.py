#!/usr/bin/env python3

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

# MODULES
from core import Configuration, PraktiCalculator

import tkinter as tk
from tkinter import ttk, messagebox, font, scrolledtext, filedialog, colorchooser
from pathlib import Path
from decimal import Decimal
import platform, subprocess, sys, shutil, math, getpass, time, configparser, importlib.util, webbrowser, zipfile, tempfile, hashlib, re
if platform.system() == "Windows":
    import winreg
    from ctypes import wintypes
elif platform.system() == "Darwin":
    import plistlib

# VARIABLES
CLIHelp = "--help" in sys.argv
CLIVersion = "--version" in sys.argv
PraktiCalcVersion = "1.6"
BypassWindowsDPIFix = "--nodpiawareness" in sys.argv
allowWindowsShutdownDialog = "--allowShutdownDialog" in sys.argv
MsgBoxStyles = ["Tkinter", "Alternative"]
if platform.system() == "Windows":
    import ctypes
    NativeTheme = "vista"
    if shutil.which("wscript"):
        MsgBoxStyles.append("VBScript")
    if shutil.which("msg"):
        MsgBoxStyles.append("Windows Messaging Service")
    if allowWindowsShutdownDialog == True:
        MsgBoxStyles.append("Windows Shutdown")
    if BypassWindowsDPIFix == False:
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(2)
        except:
            pass
    if platform.release() == "Vista" or platform.release() == "7" or platform.release() == "8" or platform.release() == "8.1":
        WingWebDings = True
    else:
        WingWebDings = False
        dwmapi = ctypes.WinDLL("dwmapi")
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
elif platform.system() == "Darwin":
    NativeTheme = "aqua"
    WingWebDings = False
    MsgBoxStyles.append("AppleScript")
else:
    WingWebDings = False
    NativeTheme = "default"
    AdditionalLinuxMsgBoxStyles = ["xmessage", "gxmessage", "wmessage", "yad", "kdialog", "zenity", "Xdialog", "notify-send"]
    for MsgBoxStyle in AdditionalLinuxMsgBoxStyles:
        if shutil.which(MsgBoxStyle):
            MsgBoxStyles.append(MsgBoxStyle)
if CLIHelp == True:
    if platform.system() == "Windows":
        messagebox.showinfo("PraktiCalc CLI Options", "PraktiCalc " + PraktiCalcVersion + """ CLI Options:
--allowShutdownDialog: allow the shutdown dialog to be used
--debug: add a test button for debugging
--nodpiawareness: disable Windows DPI Awareness
--console: show console for debugging
--help: display this help text and exit
--version: display version and exit""")
    else:
        print("PraktiCalc " + PraktiCalcVersion + " CLI Options")
        print("--debug      | add a test button for debugging")
        print("--console    | show console for debugging")
        print("--notheming  | disables theming")
        print("--help       | display this help text and exit")
        print("--version    | display version and exit")
    sys.exit(0)
if CLIVersion == True:
    if platform.system() == "Windows":
        messagebox.showinfo("PraktiCalc " + PraktiCalcVersion, "PraktiCalc " + PraktiCalcVersion)
    else:
        print("PraktiCalc " + PraktiCalcVersion)
    sys.exit(0)

# test if this is running as a pyinstaller executable
def testForPyInstaller():
    try:
        print(sys._MEIPASS)
        return True
    except:
        return False

RunningAsOneFileExe = testForPyInstaller()

# ttkthemes directory workaround for AppImage
if Path("./usr/share/tcltk/ttkthemes").exists():
    # If started as AppImage:
    tcl_dir = Path("./usr/share/tcltk/ttkthemes").resolve()

if RunningAsOneFileExe == True:
    if platform.system() == "Darwin":
        PraktiCalcMacIconPath = (sys._MEIPASS + "/PLEL_macOS.png")
    PraktiCalcIconPath = (sys._MEIPASS + "/PLEL.png")
    PraktiCalcIconMonoPath = (sys._MEIPASS + "/PraktiCalculator_icon.xbm")
    PraktiCalcIconMonoInvertedPath = (sys._MEIPASS + "/PraktiCalculator_icon_inverted.xbm")
    PythonPowerPath = (sys._MEIPASS + "/python-powered.png")
    VBSInfoPath = (sys._MEIPASS + "/info.vbs")
    VBSErrorPath = (sys._MEIPASS + "/error.vbs")
else:
    if platform.system() == "Darwin":
        PraktiCalcMacIconPath = "PLEL_macOS.png"
    PraktiCalcIconPath = "PLEL.png"
    PraktiCalcIconMonoPath = "PraktiCalculator_icon.xbm"
    PraktiCalcIconMonoInvertedPath = "PraktiCalculator_icon_inverted.xbm"
    PythonPowerPath = "python-powered.png"
    VBSInfoPath = "info.vbs"
    VBSErrorPath = "error.vbs"

debug = "--debug" in sys.argv

# CLASSES

# provides settings, theming and ajustments for windows
class WindowHelper:
    def __init__(self, cfg):
        self.WindowList = []
        self.ConfigurationStorage = cfg
        self.refreshTheming()
        self.availableThemes = ["error loading list"]
    def refreshTheming(self):
        self.theming = 0
        self.DarkMode = False
        # 0 = theming from ttk
        # 1 = theming from ttkthemes
        # 2 = manual theming
    def changeTheme(self, WindowName): # sets the theme for a given window
        self.refreshTheming()
        theme = self.ConfigurationStorage.get("theme")
        if platform.system() == "Darwin":
            self.style = ttk.Style(WindowName)
            if subprocess.getoutput("defaults read -g AppleInterfaceStyle") == "Dark":
                self.DarkMode = True
            else:
                self.DarkMode = False
        elif platform.system() == "Windows":
            self.style = ttk.Style(WindowName)
            try:
                ClassicStyleEnabled = ctypes.c_bool()
                ctypes.windll.dwmapi.DwmIsCompositionEnabled(ctypes.byref(ClassicStyleEnabled))
                ClassicStyleEnabled = not ClassicStyleEnabled.value
            except Exception:
                ClassicStyleEnabled = True
            if ClassicStyleEnabled == True:
                if ctypes.windll.user32.GetSysColor(5) == 0:
                    self.DarkMode = True
            if platform.release() in "110":
                try:
                    with winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Control Panel\Accessibility\HighContrast") as ContrastKey:
                        if winreg.QueryValueEx(ContrastKey, "LastUpdatedThemeId")[0] in [1, 2, 3]:
                            self.DarkMode = True
                except:
                    pass
            if WingWebDings == True:
                self.style.configure("Webdings.TButton", font=webdingsfont)
                self.style.configure("Wingdings.TButton", font=wingdingsfont)
            else:
                self.style.configure("LargeUnicode.TButton", font=LargeUnicodeFont)
        else:
            self.style = ttk.Style(WindowName)
        try:
            self.style.configure("Treeview", rowheight=40)
            self.availableThemes = self.style.theme_names()
        except:
            print("Unable to increase row height of Treeview tables")
    def ajustTitleBar(self, hwnd): # changes the appearance of the Windows title bar
        if platform.system() == "Windows":
            try:
                value = wintypes.BOOL(self.DarkMode)
                dwmapi.DwmSetWindowAttribute(wintypes.HWND(hwnd), wintypes.DWORD(DWMWA_USE_IMMERSIVE_DARK_MODE), ctypes.byref(value), ctypes.sizeof(value))
            except:
                pass
    def ajustTitleBars(self): # changes the appearance of all Windows title bars
        for window in self.WindowList:
            try:
                self.ajustTitleBar(ctypes.windll.user32.GetParent(window.winfo_id()))
            except:
                pass
    def close(self, window): # closes the given window and removes it from the window list
        window.destroy()
        self.WindowList.remove(window)

# info and error dialogs
class Dialog:
    def __init__(self, cfg):
        self.ConfigurationStorage = cfg
    def info(self, parent, helper): # shows info dialogs
        infotext = f"""PraktiCalc Legacy Extension Loader
Powered by PraktiCalc {PraktiCalcVersion}
Copyright \u00a9 2024-2026 Karl Wesseler
Running on Python {platform.python_version()} / Tk {tk.TkVersion}
Licensed under the GPLv3"""
        if self.ConfigurationStorage.get("dialogStyle") == "Alternative":
            CustomInfox = tk.Toplevel(parent)
            self.PythonPower = tk.PhotoImage(file=PythonPowerPath)
            try:
                self.TclTkPower = tk.PhotoImage(file=str(CustomInfox.tk.globalgetvar("tk_library")) + "/images/pwrdLogo150.gif")
            except:
                pass
            CustomInfox.title("About PLEL")
            CustomInfox.bind("<Return>", lambda event: helper.close(CustomInfox))
            CustomInfox.rowconfigure(0, weight=1)
            CustomInfox.columnconfigure(0, weight=1)
            if platform.system() == "Windows":
                CustomInfox.attributes("-toolwindow", True)
                CustomInfox.focus_set()
            CustomInfoFrame = ttk.Frame(CustomInfox)
            CustomInfoFrame.rowconfigure(0, weight=1)
            CustomInfoFrame.columnconfigure(0, weight=1)
            CustomInfoExit = ttk.Button(CustomInfoFrame, text="OK", command=lambda: helper.close(CustomInfox))
            ExtendedInfoFrame = ttk.LabelFrame(CustomInfoFrame, relief=tk.SUNKEN, text="[i]")
            ExtendedInfoFrame.rowconfigure(0, weight=1)
            ExtendedInfoFrame.rowconfigure(1, weight=1)
            ExtendedInfoFrame.columnconfigure(0, weight=1)
            ExtInfoIcon = ttk.Label(ExtendedInfoFrame, image=parent.icon)
            ExtInfoText1 = ttk.Label(ExtendedInfoFrame, text=infotext, justify=tk.LEFT)
            if "--debug" in sys.argv:
                DebugIconFrame = ttk.Frame(ExtendedInfoFrame)
                IconList = ["info", "question", "warning", "error", "hourglass", "gray75", "gray50", "gray25", "gray12"]
                for icon in IconList:
                    if helper.DarkMode == True:
                        tk.Label(DebugIconFrame, bitmap=icon, bg="black", fg="white").grid(row=0, column=IconList.index(icon), padx=(0, 10))
                    else:
                        tk.Label(DebugIconFrame, bitmap=icon).grid(row=0, column=IconList.index(icon), padx=(0, 10))
                DebugIconFrame.grid(row=2, column=0, padx=10, pady=(0, 5), sticky=tk.W)
            CustomInfoFrame.grid(row=0, column=0, sticky=tk.NSEW)
            CustomInfoExit.grid(row=1, column=1, padx=10, pady=10)
            CustomInfoExit.focus_set()
            if platform.system() == "Darwin" and self.ConfigurationStorage.get("nativeTheme") == 1:
                tk.Button(CustomInfoFrame, font=("Tk.DefaultFont", 11), image=self.PythonPower, command=lambda: webbrowser.open_new_tab("https://www.python.org/")).grid(row=1, column=0, padx=10, pady=10, sticky=tk.SW)
                if hasattr(self, "TclTkPower"):
                    tk.Button(CustomInfoFrame, font=("Tk.DefaultFont", 11), image=self.TclTkPower, command=lambda: webbrowser.open_new_tab("https://www.tcl-lang.org/")).grid(row=0, column=1, padx=10, pady=10, sticky=tk.N)
            else:
                ttk.Button(CustomInfoFrame, image=self.PythonPower, command=lambda: webbrowser.open_new_tab("https://www.python.org/")).grid(row=1, column=0, padx=10, pady=10, sticky=tk.SW)
                if hasattr(self, "TclTkPower"):
                    ttk.Button(CustomInfoFrame, image=self.TclTkPower, command=lambda: webbrowser.open_new_tab("https://www.tcl-lang.org/")).grid(row=0, column=1, padx=10, pady=10, sticky=tk.N)
            ExtendedInfoFrame.grid(row=0, column=0, padx=20, pady=10, sticky=tk.NSEW)
            ExtInfoIcon.grid(row=0, column=0)
            ExtInfoText1.grid(row=1, column=0, padx=10, pady=(0, 5))
            CustomInfox.protocol("WM_DELETE_WINDOW", lambda: helper.close(CustomInfox))
            CustomInfox.update_idletasks()
            helper.WindowList.append(CustomInfox)
            helper.changeTheme(CustomInfox)
        else:
            if platform.system() == "Windows":
                pyver = platform.python_version()
                styles = {
                    "VBScript": lambda: subprocess.Popen(["wscript", VBSInfoPath, PraktiCalcVersion, pyver, str(tk.TkVersion), str(helper.theming)]),
                    "Windows Messaging Service": lambda: subprocess.Popen(["msg", getpass.getuser(), infotext]),
                    }
                opendialog = styles.get(self.ConfigurationStorage.get("dialogStyle"))
                if opendialog:
                    opendialog()
                elif self.ConfigurationStorage.get("dialogStyle") == "Windows Shutdown":
                    subprocess.Popen(["shutdown", "/s", "/t", "60", "/c", infotext])
                    time.sleep(20)
                    subprocess.Popen(["shutdown", "/a"])
                else:
                    print("ERROR: Unknown Message Box Style")
            else:
                styles = {
                    "xmessage": lambda: subprocess.Popen(["xmessage", "-title", "About PLEL", "-buttons", "OK", "-default", "OK", infotext.replace("\u00a9", "(C)")]),
                    "gxmessage": lambda: subprocess.Popen(["gxmessage", "-title", "About PLEL", "-buttons", "OK", "-default", "OK", infotext]),
                    "wmessage": lambda: subprocess.Popen(["wmessage", "-title", "About PLEL", "-buttons", "OK", "-default", "OK", infotext]),
                    "yad": lambda: subprocess.Popen(["yad", "--title=About PLEL", "--info", "--image=" + PraktiCalcIconPath, "--button=OK", "--text=" + infotext]),
                    "kdialog": lambda: subprocess.Popen(["kdialog", "--title=About PLEL", "--msgbox", infotext]),
                    "zenity": lambda: subprocess.Popen(["zenity", "--title=About PLEL", "--info", "--icon=" + PraktiCalcIconPath, "--text=" + infotext]),
                    "AppleScript": lambda: subprocess.run(["osascript", "-e", f'display dialog "{infotext}" with icon POSIX file "{PraktiCalcIconPath}" with title "About PraktiCalc"']),
                    "Xdialog": lambda: subprocess.Popen(["Xdialog", "--title=About PLEL", "--msgbox", infotext.replace("\u00a9", "(C)"), "10", "40"]),
                    "notify-send": lambda: subprocess.Popen(["notify-send", "About PLEL", "--icon=de.karl_52.PraktiCalc", "--action=OK", infotext]),
                    }
                opendialog = styles.get(self.ConfigurationStorage.get("dialogStyle"))
                if opendialog:
                    opendialog()
                else:
                    messagebox.showinfo("About PLEL", infotext)
    def error(self, message, parent, helper): # shows error dialogs
        if self.ConfigurationStorage.get("dialogStyle") == "Alternative":
            ErrorWindow = tk.Toplevel(parent)
            ErrorWindow.title("Error")
            ErrorWindow.bind("<Return>", lambda event: helper.close(ErrorWindow))
            ErrorWindow.rowconfigure(0, weight=1)
            ErrorWindow.columnconfigure(0, weight=1)
            if platform.system() == "Windows":
                ErrorWindow.attributes("-toolwindow", True)
                ErrorWindow.focus_set()
            ErrorWindowFrame = ttk.Frame(ErrorWindow)
            ErrorWindowFrame.rowconfigure(0, weight=1)
            ErrorWindowFrame.columnconfigure(0, weight=1)
            ErrorExitButton = ttk.Button(ErrorWindowFrame, text="OK", command=lambda: helper.close(ErrorWindow))
            ExtendedErrorFrame = ttk.LabelFrame(ErrorWindowFrame, relief=tk.SUNKEN, text="[X]")
            ExtendedErrorFrame.rowconfigure(0, weight=1)
            ExtendedErrorFrame.columnconfigure(0, weight=1)
            ErrorTextLabel = ttk.Label(ExtendedErrorFrame, text=message)
            ErrorWindowFrame.grid(row=0, column=0, sticky=tk.NSEW)
            ErrorExitButton.grid(row=1, column=1, padx=10, pady=10)
            ErrorExitButton.focus_set()
            ExtendedErrorFrame.grid(row=0, column=0, padx=20, pady=10, sticky=tk.NSEW)
            ErrorTextLabel.grid(row=0, column=0)
            ErrorWindow.protocol("WM_DELETE_WINDOW", lambda: helper.close(ErrorWindow))
            ErrorWindow.update_idletasks()
            helper.WindowList.append(ErrorWindow)
            helper.changeTheme(ErrorWindow)
        else:
            if platform.system() == "Windows":
                styles = {
                    "VBScript": lambda: subprocess.Popen(["wscript", VBSErrorPath, message]),
                    "Windows Messaging Service": lambda: subprocess.Popen(["msg", getpass.getuser(), message]),
                    }
                opendialog = styles.get(self.ConfigurationStorage.get("dialogStyle"))
                if opendialog:
                    opendialog()
                elif self.ConfigurationStorage.get("dialogStyle") == "Windows Shutdown":
                    subprocess.Popen(["shutdown", "/s", "/t", "60", "/c", message])
                    time.sleep(10)
                    subprocess.Popen(["shutdown", "/a"])
                else:
                    print("ERROR: Unknown Message Box Style")
            else:
                styles = {
                    "xmessage": lambda: subprocess.Popen(["xmessage", "-title", "Error", "-buttons", "OK", "-default", "OK", "[X] " + message]),
                    "gxmessage": lambda: subprocess.Popen(["gxmessage", "-title", "Error", "-buttons", "OK", "-default", "OK", "[X] " + message]),
                    "wmessage": lambda: subprocess.Popen(["wmessage", "-title", "Error", "-buttons", "OK", "-default", "OK", "[X] " + message]),
                    "yad": lambda: subprocess.Popen(["yad", "--title=Error", "--error", "--image=dialog-error", "--button=OK", "--no-markup", "--text", message]),
                    "kdialog": lambda: subprocess.Popen(["kdialog", "--title=Error", "--error", message]),
                    "zenity": lambda: subprocess.Popen(["zenity", "--title=Error", "--error", "--no-markup", "--text", message]),
                    "AppleScript": lambda: subprocess.run(["osascript", "-e", f'display dialog "{message}" with icon stop with title "Error"']),
                    "Xdialog": lambda: subprocess.Popen(["Xdialog", "--title=Error", "--msgbox", message, "10", "40"]),
                    "notify-send": lambda: subprocess.Popen(["notify-send", "Error", "--icon=dialog-error", "--action=OK", message]),
                    }
                opendialog = styles.get(self.ConfigurationStorage.get("dialogStyle"))
                if opendialog:
                    opendialog()
                else:
                    messagebox.showerror("Error", message)

# extension window
class ExtensionWindow(tk.Tk):
    def __init__(self, helper, calculator, dialog, cfg):
        super().__init__()
        parent = self
        self.title("PraktiCalc Legacy Extension Loader")
        self.DPI = self.winfo_fpixels("1i")
        if platform.system() == "Windows":
            if cfg.get("noDPIAwareness") == 1:
                self.ScaleFactor = 1
            else:
                self.ScaleFactor = self.DPI/72
        else:
            self.ScaleFactor = self.DPI/72
        #print(self.DPI)
        #print(self.ScaleFactor)
        self.size = int(250*self.ScaleFactor)
        self.icon_mono = tk.BitmapImage(file=PraktiCalcIconMonoPath)
        self.icon = tk.PhotoImage(file=PraktiCalcIconPath)
        NativeMenubar = bool(cfg.get("nativeMenuBar"))
        if platform.system() == "Darwin":
            self.macicon = tk.PhotoImage(file=PraktiCalcMacIconPath)
            self.iconphoto(True, self.macicon)
        else:
            self.iconphoto(True, self.icon)
        self.icon_mono_inverted = tk.BitmapImage(file=PraktiCalcIconMonoInvertedPath)
        if WingWebDings == True:
            wingdingsfont = font.Font(family="Wingdings")
            webdingsfont = font.Font(family="Webdings")
        else:
            LargeUnicodeFont = font.Font(family="TkDefaultFont", size=14)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        if platform.system() == "Windows":
            if RunningAsOneFileExe == True:
                if sys.executable == r"C:\Program Files\PraktiCalc\prakticalc.exe":
                    self.FolderPath = Path.home() / "AppData" / "Roaming" / "PraktiXtensions"
                else:
                    f1 = Path(sys.executable).parent
                    self.FolderPath = f1 / "extensions"
            else:
                self.FolderPath = Path.home() / "AppData" / "Roaming" / "PraktiXtensions"
        elif platform.system() == "Darwin":
            self.FolderPath = Path.home() / "Library" / "PraktiXtensions"
        else:
            self.FolderPath = Path.home() / ".config" / "PraktiXtensions"
        self.Tabs = ttk.Notebook(self)
        self.Tabs.grid(row=0, column=0, sticky=tk.NSEW)
        self.protocol("WM_DELETE_WINDOW", lambda: helper.close(self))
        self.update_idletasks()
        helper.WindowList.append(self)
        helper.changeTheme(self)
        self.after(250, lambda: self.loadExtensions(parent, helper, calculator, dialog))
    def loadExtensions(self, parent, helper, calculator, dialog): # loads extensions from the folder, writes default extensions to folder if folder doesn't exist
        if not self.FolderPath.exists():
            self.FolderPath.mkdir(parents=True)
            self.updateDecimalConverter()
            self.updateExtensionManager()
            self.updatePraktiGraph()
        ContentIsThere = False
        for f in self.FolderPath.iterdir():
            if not str(f).endswith("__pycache__"):
                ContentIsThere = True
        if ContentIsThere == False:
            dialog.error(f"There are no extensions installed. You can install some manually in {self.FolderPath},\nor delete that folder to reset the extension system, which reinstalls the extension manager.", parent, helper)
            helper.close(self)
            return
        if Path(self.FolderPath / "DecimalConverter.ini").exists():
            DecimalConverterMeta = configparser.ConfigParser()
            DecimalConverterMeta.read(self.FolderPath / "DecimalConverter.ini", encoding="utf-8")
            if DecimalConverterMeta["PraktiXtension"]["version"] != "1.3":
                self.updateDecimalConverter()
        if Path(self.FolderPath / "ExtensionManager.ini").exists():
            ExtensionManagerMeta = configparser.ConfigParser()
            ExtensionManagerMeta.read(self.FolderPath / "ExtensionManager.ini", encoding="utf-8")
            if ExtensionManagerMeta["PraktiXtension"]["version"] != "1.13":
                self.updateExtensionManager()
        if Path(self.FolderPath / "PraktiGraph.ini").exists():
            PraktiGraphMeta = configparser.ConfigParser()
            PraktiGraphMeta.read(self.FolderPath / "PraktiGraph.ini", encoding="utf-8")
            if PraktiGraphMeta["PraktiXtension"]["version"] != "1.9":
                self.updatePraktiGraph()
        for file in self.FolderPath.iterdir():
            if file.suffix == ".py":
                if Path(self.FolderPath / f"{file.stem}.ini").exists():
                    meta = configparser.ConfigParser()
                    meta.read(Path(self.FolderPath / f"{file.stem}.ini"), encoding="utf-8")
                    if meta["PraktiXtension"]["minpython"] == "default":
                        if meta["PraktiXtension"]["maxpython"] == "default":
                            canload = True
                        elif tuple(meta["PraktiXtension"]["maxpython"].split(".")) >= platform.python_version_tuple()[:-1]:
                            canload = True
                        else: canload = False
                    elif tuple(meta["PraktiXtension"]["minpython"].split(".")) <= platform.python_version_tuple()[:-1]:
                        canload = True
                    else:
                        canload = False
                    if canload == True:
                        spec = importlib.util.spec_from_file_location(file.stem, file)
                        module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(module)
                        classs = getattr(module, file.stem)
                        instance = classs(self.Tabs, self, parent, helper, calculator, dialog, helper.DarkMode)
                        self.Tabs.add(instance, text=meta["PraktiXtension"]["name"])
                        print("loaded extension " + meta["PraktiXtension"]["name"])
                    else:
                        dialog.error("Incompatible Python version", parent, helper)
                else:
                    spec = importlib.util.spec_from_file_location(file.stem, file)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    classs = getattr(module, file.stem)
                    instance = classs(self.Tabs, self, parent, helper, calculator, dialog, helper.DarkMode)
                    self.Tabs.add(instance, text=file.stem)
                    print("loaded extension " + file.stem)
        self.geometry(f"{int(700*parent.ScaleFactor)}x{int(500*parent.ScaleFactor)}")
    def updateDecimalConverter(self): # updates decimal converter extension to the version embedded here
        if Path(self.FolderPath / "DecimalConverter.py").exists():
            Path(self.FolderPath / "DecimalConverter.py").unlink()
            Path(self.FolderPath / "DecimalConverter.ini").unlink(missing_ok=True)
            Path(self.FolderPath / "DecimalConverter.txt").unlink(missing_ok=True)
        if not Path(self.FolderPath / "DecimalConverter.py").exists():
            DecimalConverterCode = r"""# PraktiCalc Decimal Converter
# Copyright (C) 2024-2026 Karl Wesseler
# SPDX-License-Identifier: GPL-3.0-only

import tkinter as tk
from tkinter import ttk

class DecimalConverter(ttk.Frame):
    def __init__(self, tabs, parent, mainWin, helper, calculator, dialog, DarkMode):
        super().__init__(tabs)
        DecimalFrame = ttk.LabelFrame(self, text="Decimal")
        self.DecimalInput = ttk.Entry(DecimalFrame, width=70)
        DecimalFrame.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        InsertButton = ttk.Button(DecimalFrame, text="OK", command=lambda: self.convert(parent, helper, dialog))
        binFrame = ttk.LabelFrame(self, text="Binary")
        hexFrame = ttk.LabelFrame(self, text="Hexadecimal")
        frames = (binFrame, hexFrame)
        for i in range(2):
            frames[i].columnconfigure(0, weight=1)
            frames[i].rowconfigure(0, weight=1)
            frames[i].rowconfigure(1, weight=1)
        self.BinDisplay = ttk.Entry(binFrame)
        self.HexDisplay = ttk.Entry(hexFrame)
        self.BinScrollbar = ttk.Scrollbar(binFrame, orient=tk.HORIZONTAL, command=self.BinDisplay.xview)
        self.HexScrollbar = ttk.Scrollbar(hexFrame, orient=tk.HORIZONTAL, command=self.HexDisplay.xview)
        self.BinDisplay.config(state="readonly", xscrollcommand=self.BinScrollbar.set)
        self.HexDisplay.config(state="readonly", xscrollcommand=self.HexScrollbar.set)
        BinCopyButton = ttk.Button(binFrame, text="Copy", command=lambda: self.copybin(mainWin))
        HexCopyButton = ttk.Button(hexFrame, text="Copy", command=lambda: self.copyhex(mainWin))
        DecimalFrame.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW, padx=5)
        self.DecimalInput.grid(row=0, column=0, pady=5, padx=5, sticky=tk.NSEW)
        InsertButton.grid(row=0, column=1, padx=5, pady=5)
        binFrame.grid(row=1, column=0, sticky=tk.NSEW, padx=5, pady=(0, 5))
        hexFrame.grid(row=1, column=1, sticky=tk.NSEW, padx=5, pady=(0, 5))
        self.BinDisplay.grid(row=0, column=0, sticky=tk.EW + tk.S)
        self.HexDisplay.grid(row=0, column=0, sticky=tk.EW + tk.S)
        self.BinScrollbar.grid(row=1, column=0, sticky=tk.EW + tk.N)
        self.HexScrollbar.grid(row=1, column=0, sticky=tk.EW + tk.N)
        BinCopyButton.grid(row=2, column=0, pady=(0, 5))
        HexCopyButton.grid(row=2, column=0, pady=(0, 5))
        self.DecimalInput.focus_set()
    def convert(self, parent, helper, dialog): # converts decimal numbers into binary and hexadecimal
        cp = str(self.DecimalInput.get())
        try:
            displays = [self.BinDisplay, self.HexDisplay]
            DecimalNumber = int(cp)
            BinaryNumber = bin(DecimalNumber)[2:]
            HexadecimalNumber = hex(DecimalNumber)[2:]
            for display in displays:
                display.config(state=tk.NORMAL)
                display.delete(0, tk.END)
            self.BinDisplay.insert(0, str(BinaryNumber))
            self.HexDisplay.insert(0, str(HexadecimalNumber).upper())
            for display in displays:
                display.config(state="readonly")
        except:
            dialog.error("Please enter a real number!", parent, helper)
    def copybin(self, mainWin): # copies the binary output
        mainWin.clipboard_clear()
        mainWin.clipboard_append(self.BinDisplay.get())
        mainWin.update()
    def copyhex(self, mainWin): # copies the hexadecimal output
        mainWin.clipboard_clear()
        mainWin.clipboard_append(self.HexDisplay.get())
        mainWin.update()"""
            DecimalConverterMetadata = configparser.ConfigParser()
            DecimalConverterMetadata["PraktiXtension"] = {"name": "Decimal Converter",
                                                          "version": "1.3",
                                                          "filename": "DecimalConverter.py",
                                                          "description": "The PraktiCalc Decimal Converter",
                                                          "website": "",
                                                          "minpython": "default",
                                                          "maxpython": "default",
                                                          "sha256": "",
                                                          "requiresinternet": "false",
                                                          "pxtxlink": ""}
            DecimalConverterDescription = "This is the known decimal converter that PraktiCalc includes by default, now as an extension."
            with open(self.FolderPath / "DecimalConverter.py", "w", encoding="utf-8") as dcfile:
                dcfile.write(DecimalConverterCode)
            with open(self.FolderPath / "DecimalConverter.ini", "w", encoding="utf-8") as dcmeta:
                DecimalConverterMetadata.write(dcmeta)
            with open(self.FolderPath / "DecimalConverter.txt", "w", encoding="utf-8") as dcdesc:
                dcdesc.write(DecimalConverterDescription)
    def updateExtensionManager(self): # updates extension manager extension to the version embedded here
        if Path(self.FolderPath / "ExtensionManager.py").exists():
            Path(self.FolderPath / "ExtensionManager.py").unlink()
            Path(self.FolderPath / "ExtensionManager.ini").unlink(missing_ok=True)
            Path(self.FolderPath / "ExtensionManager.txt").unlink(missing_ok=True)
        if not Path(self.FolderPath / "ExtensionManager.py").exists():
            ExtensionManagerCode = r"""# PraktiCalc Extension Manager
# Copyright (C) 2026 Karl Wesseler
# SPDX-License-Identifier: GPL-3.0-only

import tkinter as tk
from tkinter import ttk, font, messagebox, filedialog
from pathlib import Path
import webbrowser, configparser, zipfile, tempfile, hashlib, shutil, platform, subprocess

class ExtensionManager(ttk.Frame):
    def __init__(self, tabs, parent, mainWin, helper, calculator, dialog, DarkMode):
        super().__init__(tabs)
        self.style = ttk.Style()
        self.style.configure("ExtensionTitle.TLabel", font=font.Font(family="TkDefaultFont", size=15))
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        ttk.Label(self, text="The Extension Manager allows you to manage extensions in the PraktiXtension (.pxt) format.").grid(row=0, column=0, sticky=tk.W)
        self.Splitter = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        self.LeftFrame = ttk.Frame(self.Splitter)
        self.RightFrame = ttk.LabelFrame(self.Splitter, text="Metadata")
        self.ExtensionTree = ttk.Treeview(self.LeftFrame, selectmode=tk.BROWSE)
        self.ExtensionTreeScrollbar = ttk.Scrollbar(self.LeftFrame, orient=tk.VERTICAL, command=self.ExtensionTree.yview)
        self.ExtensionTree.config(yscrollcommand=self.ExtensionTreeScrollbar.set)
        self.ExtensionTree.bind("<<TreeviewSelect>>", lambda event: self.updateMetadataDisplay(parent))
        self.ExtensionTree.heading("#0", text="Extensions")
        for file in parent.FolderPath.iterdir():
            if file.suffix == ".py":
                self.ExtensionTree.insert("", tk.END, text=file.stem)
        ttk.Label(self.RightFrame).grid(row=0, column=0)
        self.ExtensionTree.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW)
        self.ExtensionTreeScrollbar.grid(row=0, column=2, sticky=tk.NS)
        self.AddButton = ttk.Button(self.LeftFrame, text="Add", command=lambda: self.addExtension(parent, helper, dialog))
        self.AddButton.grid(row=1, column=0, padx=10, pady=10, sticky=tk.EW)
        self.RemoveButton = ttk.Button(self.LeftFrame, text="Remove", state=tk.DISABLED, command=lambda: self.removeExtension(parent))
        self.RemoveButton.grid(row=1, column=1, padx=10, pady=10, sticky=tk.EW)
        self.OpenFolderButton = ttk.Button(self.LeftFrame, text="Open Extension Folder", command=lambda: self.openFolder(parent))
        if platform.system() not in ("Windows", "Darwin"):
            if not shutil.which("xdg-open"):
                self.OpenFolderButton.config(state=tk.DISABLED)
        self.OpenFolderButton.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky=tk.EW)
        self.ResetButton = ttk.Button(self.LeftFrame, text="Reset Extension Folder", command=lambda: self.reset(parent, mainWin, helper))
        self.ResetButton.grid(row=3, column=0, columnspan=2, padx=10, pady=(10, 0), sticky=tk.EW)
        ttk.Separator(self.LeftFrame, orient=tk.HORIZONTAL).grid(row=4, rowspan=2, column=0, columnspan=2, pady=7, sticky=tk.EW)
        ttk.Button(self.LeftFrame, text="PraktiXtension Gallery", command=lambda: webbrowser.open_new("https://praktixtensions.blogspot.com/p/browse.html")).grid(row=6, column=0, columnspan=2, padx=10, pady=(0, 10), sticky=tk.EW)
        ttk.Separator(self.LeftFrame, orient=tk.VERTICAL).grid(row=5, rowspan=2, column=2, sticky=tk.NS + tk.W)
        self.LeftFrame.columnconfigure(0, weight=1)
        self.LeftFrame.columnconfigure(1, weight=1)
        self.RightFrame.columnconfigure(0, weight=1)
        self.TitleLabel = ttk.Label(self.RightFrame, text="", style="ExtensionTitle.TLabel")
        self.DescriptionLabel = ttk.Label(self.RightFrame, text="")
        self.InternetLabel = ttk.Label(self.RightFrame, text="requires internet connection")
        self.WebsiteButton = ttk.Button(self.RightFrame, text="Website")
        self.VersionDisplay = ttk.Entry(self.RightFrame, state="readonly")
        self.LicenseDisplay = ttk.Entry(self.RightFrame, state="readonly")
        self.minPyVerDisplay = ttk.Entry(self.RightFrame, state="readonly")
        self.maxPyVerDisplay = ttk.Entry(self.RightFrame, state="readonly")
        self.FileNameDisplay = ttk.Entry(self.RightFrame, state="readonly")
        self.WebLinkDisplay = ttk.Entry(self.RightFrame, state="readonly")
        self.ChecksumDisplay = ttk.Entry(self.RightFrame, state="readonly")
        self.TitleLabel.grid(row=0, column=0, columnspan=2, sticky=tk.NE + tk.W)
        self.DescriptionLabel.grid(row=1, column=0, columnspan=2, sticky=tk.EW)
        ttk.Separator(self.RightFrame, orient=tk.HORIZONTAL).grid(row=3, column=0, columnspan=2, sticky=tk.EW)
        Labels = ["Version", "File name", "License", "Website", "Minimal Python version", "Maximal Python version", "SHA256 checksum"]
        Entrys = [self.VersionDisplay, self.FileNameDisplay, self.LicenseDisplay, self.WebLinkDisplay, self.minPyVerDisplay, self.maxPyVerDisplay, self.ChecksumDisplay]
        for i in range(7):
            ttk.Label(self.RightFrame, text=Labels[i]).grid(row=i+4, column=0, sticky=tk.EW, padx=10)
            Entrys[i].grid(row=i+4, column=1, sticky=tk.EW, padx=10, pady=5)
        self.DescriptionFrame = ttk.LabelFrame(self.RightFrame, text="Description")
        self.DescriptionFrame.rowconfigure(0, weight=1)
        self.DescriptionFrame.columnconfigure(0, weight=1)
        self.DescriptionFrame.grid(row=11, column=0, columnspan=2, sticky=tk.NSEW, padx=5, pady=5)
        self.DescriptionText = tk.Text(self.DescriptionFrame, font="TkFixedFont", height=15, state=tk.DISABLED, wrap=tk.WORD)
        self.DescriptionScrollbar = ttk.Scrollbar(self.DescriptionFrame, orient=tk.VERTICAL, command=self.DescriptionText.yview)
        self.DescriptionText.config(yscrollcommand=self.DescriptionScrollbar.set)
        self.DescriptionScrollbar.grid(row=0, column=1, padx=(0, 5), pady=5, sticky=tk.NS)
        if DarkMode == True:
            self.DescriptionText.config(bg="black", fg="white")
        self.DescriptionText.grid(row=0, column=0, sticky=tk.NSEW, padx=(5, 0), pady=5)
        self.LeftFrame.rowconfigure(0, weight=1)
        self.RightFrame.columnconfigure(1, weight=1)
        self.RightFrame.rowconfigure(11, weight=1)
        self.Splitter.add(self.LeftFrame)
        self.Splitter.add(self.RightFrame)
        self.Splitter.grid(row=1, column=0, sticky=tk.NSEW)
    def updateMetadataDisplay(self, parent):
        self.RemoveButton.config(state=tk.NORMAL)
        ext = self.ExtensionTree.item(self.ExtensionTree.selection(), "text")
        labels = [self.TitleLabel, self.DescriptionLabel]
        displays = [self.VersionDisplay, self.FileNameDisplay, self.LicenseDisplay, self.WebLinkDisplay, self.minPyVerDisplay, self.maxPyVerDisplay, self.ChecksumDisplay]
        if Path(parent.FolderPath / f"{ext}.ini").exists():
            metadata = configparser.ConfigParser()
            metadata.read(Path(parent.FolderPath / f"{ext}.ini"), encoding="utf-8")
            self.TitleLabel.config(text=metadata["PraktiXtension"]["name"])
            self.DescriptionLabel.config(text=metadata["PraktiXtension"]["description"])
            if metadata["PraktiXtension"]["website"] != "":
                try:
                    self.WebsiteButton.config(command=lambda: webbrowser.open_new(metadata["PraktiXtension"]["website"]))
                    self.WebsiteButton.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)
                except:
                    pass
            else:
                try:
                    self.WebsiteButton.config(command=None)
                    self.WebsiteButton.grid_remove()
                except:
                    pass
            if metadata["PraktiXtension"]["requiresinternet"] == "true":
                try:
                    self.InternetLabel.grid(row=2, column=0, sticky=tk.EW)
                except:
                    pass
            else:
                try:
                    self.InternetLabel.grid_remove()
                except:
                    pass
            for display in displays:
                display.config(state=tk.NORMAL)
                display.delete(0, tk.END)
            self.VersionDisplay.insert(0, metadata["PraktiXtension"]["version"])
            self.FileNameDisplay.insert(0, metadata["PraktiXtension"]["filename"])
            self.WebLinkDisplay.insert(0, metadata["PraktiXtension"]["website"])
            self.minPyVerDisplay.insert(0, metadata["PraktiXtension"]["minpython"])
            self.maxPyVerDisplay.insert(0, metadata["PraktiXtension"]["maxpython"])
            self.ChecksumDisplay.insert(0, metadata["PraktiXtension"]["sha256"])
            with open(Path(parent.FolderPath / metadata["PraktiXtension"]["filename"]), "r", encoding="utf-8") as extensionfile:
                extensioncontent = extensionfile.read()
            if "SPDX-License-Identifier: " in extensioncontent:
                self.LicenseDisplay.insert(0, extensioncontent.split("SPDX-License-Identifier: ")[1].split()[0])
            for display in displays:
                display.config(state="readonly")
        else:
            self.TitleLabel.config(text=ext)
            self.DescriptionLabel.config(text="no metadata found :(")
            for display in displays:
                display.config(state=tk.NORMAL)
                display.delete(0, tk.END)
                display.config(state="readonly")
            try:
                self.WebsiteButton.config(command=None)
                self.WebsiteButton.grid_remove()
            except:
                pass
            try:
                self.InternetLabel.grid_remove()
            except:
                pass
            if ext == "":
                self.RemoveButton.config(state=tk.DISABLED)
                self.DescriptionLabel.config(text="")
            elif Path(parent.FolderPath / f"{ext}.py").exists():
                with open(Path(parent.FolderPath / f"{ext}.py"), "r", encoding="utf-8") as extensionfile:
                    extensioncontent = extensionfile.read()
                if "SPDX-License-Identifier: " in extensioncontent:
                    self.LicenseDisplay.config(state=tk.NORMAL)
                    self.LicenseDisplay.insert(0, extensioncontent.split("SPDX-License-Identifier: ")[1].split()[0])
                    self.LicenseDisplay.config(state="readonly")
        self.DescriptionText.config(state=tk.NORMAL)
        if Path(parent.FolderPath / f"{ext}.txt").exists():
            with open(Path(parent.FolderPath / f"{ext}.txt"), "r", encoding="utf-8") as txt:
                self.DescriptionText.delete("1.0", tk.END)
                self.DescriptionText.insert(tk.END, txt.read())
        else:
            self.DescriptionText.delete("1.0", tk.END)
        self.DescriptionText.config(state=tk.DISABLED)
    def removeExtension(self, parent):
        ext = self.ExtensionTree.item(self.ExtensionTree.selection(), "text")
        Path(parent.FolderPath / f"{ext}.py").unlink()
        Path(parent.FolderPath / f"{ext}.ini").unlink(missing_ok=True)
        Path(parent.FolderPath / f"{ext}.txt").unlink(missing_ok=True)
        self.ExtensionTree.delete(self.ExtensionTree.selection()[0])
    def addExtension(self, parent, helper, dialog):
        file = filedialog.askopenfilename(parent=parent, initialdir=Path.home(), filetypes=[("PraktiXtension", "*.pxt")])
        if file == () or file == "":
            return
        with tempfile.TemporaryDirectory() as tempdir:
            with zipfile.ZipFile(file, "r") as Extension:
                for filename in Extension.namelist():
                    if ".." in filename or filename.startswith("/"):
                        dialog.error("Installing this extension would creates files outside of the usual extension directories, thus it's installation is aborted.", parent, helper)
                        return
                if not "info.ini" in Extension.namelist():
                    abort = True
                elif not "description.txt" in Extension.namelist():
                    abort = True
                else:
                    abort = False
                if abort == False:
                    Extension.extractall(tempdir)
                else:
                    dialog.error("Extension couldn't be installed", parent, helper)
                    return
                try:
                    metadata = configparser.ConfigParser()
                    metadata.read(Path(tempdir) / "info.ini", encoding="utf-8")
                    ExtensionName = metadata["PraktiXtension"]["filename"]
                    if not ExtensionName in [file.name for file in Path(tempdir).iterdir() if file.is_file()]:
                        raise FileNotFoundError
                    with open(Path(tempdir) / ExtensionName, "rb") as ExtensionFile:
                        if not metadata["PraktiXtension"]["sha256"] == "" and hashlib.sha256(ExtensionFile.read()).hexdigest() != metadata["PraktiXtension"]["sha256"]:
                            raise ResourceWarning
                    if metadata["PraktiXtension"]["minpython"] == "default":
                        if metadata["PraktiXtension"]["maxpython"] == "default":
                            canload = True
                        elif tuple(metadata["PraktiXtension"]["maxpython"].split(".")) >= platform.python_version_tuple()[:-1]:
                            canload = True
                        else: canload = False
                    elif tuple(metadata["PraktiXtension"]["minpython"].split(".")) <= platform.python_version_tuple()[:-1]:
                        canload = True
                    else:
                        canload = False
                    if canload == False:
                        raise ImportWarning
                    if Path(parent.FolderPath / ExtensionName).exists():
                        overwritten = True
                    else:
                        overwritten = False
                    shutil.move(Path(tempdir) / "info.ini", parent.FolderPath / f"{ExtensionName[:-3]}.ini")
                    shutil.move(Path(tempdir) / "description.txt", parent.FolderPath / f"{ExtensionName[:-3]}.txt")
                    shutil.move(Path(tempdir) / ExtensionName, parent.FolderPath / ExtensionName)
                    if overwritten == False:
                        messagebox.showinfo(parent=parent, title="PraktiXtension installed", message="Extension installed successfully, reopen the extension window to load it")
                        self.ExtensionTree.insert("", tk.END, text=ExtensionName[:-3])
                    else:
                        messagebox.showinfo(parent=parent, title="PraktiXtension upgraded", message="Extension successfully upgraded, replaced or reinstalled.\nPlease reopen the extension window to reload it")
                except FileNotFoundError:
                    dialog.error("Extension not found in file", parent, helper)
                    return
                except ResourceWarning:
                    dialog.error("Cryptographic verification of extension failed", parent, helper)
                    return
                except ImportWarning:
                    dialog.error("Incompatible Python version", parent, helper)
                    return
                except Exception as e:
                    dialog.error(str(e), parent, helper)
                    return
    def openFolder(self, parent):
        if platform.system() == "Windows":
            subprocess.Popen(["explorer", str(parent.FolderPath)])
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", str(parent.FolderPath)])
        else:
            subprocess.Popen(["xdg-open", str(parent.FolderPath)])
    def reset(self, parent, mainWin, helper):
        shutil.rmtree(parent.FolderPath)
        helper.close(parent)"""
            ExtensionManagerMetadata = configparser.ConfigParser()
            ExtensionManagerMetadata["PraktiXtension"] = {"name": "Extension Manager",
                                                          "version": "1.13",
                                                          "filename": "ExtensionManager.py",
                                                          "description": "The PraktiCalc Extension Manager",
                                                          "website": "",
                                                          "minpython": "default",
                                                          "maxpython": "default",
                                                          "sha256": "",
                                                          "requiresinternet": "false",
                                                          "pxtxlink": ""}
            ExtensionManagerDescription = "A graphical user interface to easily manage extensions in PraktiCalc."
            with open(self.FolderPath / "ExtensionManager.py", "w", encoding="utf-8") as emfile:
                emfile.write(ExtensionManagerCode)
            with open(self.FolderPath / "ExtensionManager.ini", "w", encoding="utf-8") as emmeta:
                ExtensionManagerMetadata.write(emmeta)
            with open(self.FolderPath / "ExtensionManager.txt", "w", encoding="utf-8") as emdesc:
                emdesc.write(ExtensionManagerDescription)
    def updatePraktiGraph(self): # updates PraktiGraph extension to the version embedded here
        if Path(self.FolderPath / "PraktiGraph.py").exists():
            Path(self.FolderPath / "PraktiGraph.py").unlink()
            Path(self.FolderPath / "PraktiGraph.ini").unlink(missing_ok=True)
            Path(self.FolderPath / "PraktiGraph.txt").unlink(missing_ok=True)
        if not Path(self.FolderPath / "PraktiGraph.py").exists():
            PraktiGraphCode = r"""# PraktiGraph
# Copyright (C) 2026 Karl Wesseler
# SPDX-License-Identifier: GPL-3.0-only

import tkinter as tk
from tkinter import ttk, messagebox, colorchooser
from decimal import Decimal
import platform

class PraktiGraph(ttk.Frame):
    def __init__(self, tabs, parent, mainWin, helper, calculator, dialog, DarkMode):
        super().__init__(tabs)
        if DarkMode == False:
            self.ForegroundColor = "#000000"
            self.BackgroundColor = "#ffffff"
            self.fxColor = "#000000"
            self.gxColor = "#340098"
        else:
            self.ForegroundColor = "#ffffff"
            self.BackgroundColor = "#000000"
            self.fxColor = "#ffffff"
            self.gxColor = "#5d00ff"
        self.Scale = tk.IntVar(value=int(50*mainWin.ScaleFactor))
        self.ClearStatus = True
        self.TextOffset = 15
        self.Numbers = tk.BooleanVar(value=True)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.Canvas = tk.Canvas(self, background=self.BackgroundColor)
        self.Canvas.grid(row=0, column=0, columnspan=4, sticky=tk.NSEW)
        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=1, column=0, columnspan=4, sticky=tk.EW)
        ttk.Label(self, text="f(x) = ").grid(row=2, column=0, sticky=tk.E)
        ttk.Label(self, text="g(x) = ").grid(row=3, column=0, sticky=tk.E)
        self.fxEntry = ttk.Entry(self)
        self.gxEntry = ttk.Entry(self)
        self.fxEntry.grid(row=2, column=1, columnspan=2, sticky=tk.EW)
        self.gxEntry.grid(row=3, column=1, columnspan=2, sticky=tk.EW)
        self.fxColorButton = tk.Button(self, text="Color", fg=self.fxColor, bg=self.fxColor, command=lambda: self.setFxColor(parent, calculator))
        self.gxColorButton = tk.Button(self, text="Color", fg=self.gxColor, bg=self.gxColor, command=lambda: self.setGxColor(parent, calculator))
        if platform.system() == "Darwin":
            self.fxColorButton.config(font=("TkDefaultFont", 11))
            self.gxColorButton.config(font=("TkDefaultFont", 11))
        self.fxColorButton.grid(row=2, column=3, padx=10)
        self.gxColorButton.grid(row=3, column=3, padx=10)
        self.cols = ("-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5")
        self.Table = ttk.Treeview(self, columns=self.cols, height=2)
        self.Table.heading("#0", text="x")
        for col in self.cols:
            self.Table.heading(col, text=col)
        self.FirstTableRow = self.Table.insert("", tk.END, text="f(x)")
        self.SecondTableRow = self.Table.insert("", tk.END, text="g(x)")
        fullwidth = parent.winfo_width()
        self.Table.column("#0", width=fullwidth // 12)
        for col in self.Table["columns"]:
            self.Table.column(col, width=fullwidth // 12)
        self.Table.grid(row=4, column=0, columnspan=4, sticky=tk.NSEW)
        ttk.Button(self, text="Clear", command=self.clear).grid(row=5, column=1, pady=10, padx=20, sticky=tk.E)
        ttk.Button(self, text="Draw", command=lambda: self.redraw(calculator)).grid(row=5, column=2, pady=10, padx=20, sticky=tk.W)
        ttk.Checkbutton(self, text="Draw numbers", variable=self.Numbers, command=lambda: self.redraw(calculator) if self.ClearStatus == False else self.doNothing()).grid(row=5, column=0, padx=(10, 0), sticky=tk.W)
        self.ScaleSlider = ttk.Scale(self, from_=int(25*mainWin.ScaleFactor), to=int(250*mainWin.ScaleFactor), orient=tk.HORIZONTAL, variable=self.Scale, command=lambda _: self.redraw(calculator) if self.ClearStatus == False else self.doNothing())
        self.ScaleSlider.grid(row=5, column=3, padx=(0, 10), sticky=tk.E)
        self.bind("<Configure>", lambda event: self.after(200, lambda: self.redraw(calculator)) if self.ClearStatus == False else self.clear())
        self.fxEntry.focus_set()
    def redraw(self, calculator):
        fxFunction = self.convert(self.fxEntry.get())
        gxFunction = self.convert(self.gxEntry.get())
        self.clear()
        self.ClearStatus = False
        height = self.Canvas.winfo_height()
        width = self.Canvas.winfo_width()
        #Xvalues = []
        XvaluesConverted = []
        for X in range(width):
            #Xvalues.append(X)
            XvaluesConverted.append(self.XbacktoX(X))

        # Coordinate axes and arrows
        self.Canvas.create_line(0, height/2, width, height/2, fill="grey", width=2)
        self.Canvas.create_line(width/2, 0, width/2, height, fill="grey", width=2)
        self.Canvas.create_line(width, height/2, width-10, height/2-10, fill="grey", width=2)
        self.Canvas.create_line(width, height/2, width-10, height/2+10, fill="grey", width=2)
        self.Canvas.create_line(width/2, 0, width/2-10, 10, fill="grey", width=2)
        self.Canvas.create_line(width/2, 0, width/2+10, 10, fill="grey", width=2)
        # Coordinate grid
        for i in range(int(self.XbacktoX(width))+1):
            self.Canvas.create_line(width/2+i*self.Scale.get(), 0, width/2+i*self.Scale.get(), height, fill="grey")
            self.Canvas.create_text(width/2+i*self.Scale.get(), height/2+self.TextOffset, text=str(i), fill=self.ForegroundColor) if i != 0 and self.Numbers.get() == True else self.doNothing()
            self.Canvas.create_line(width/2-i*self.Scale.get(), 0, width/2-i*self.Scale.get(), height, fill="grey")
            self.Canvas.create_text(width/2-i*self.Scale.get(), height/2+self.TextOffset, text=f"-{i}", fill=self.ForegroundColor) if i != 0 and self.Numbers.get() == True else self.doNothing()
        for i in range(int(self.YbacktoY(height))+1):
            self.Canvas.create_line(0, height/2+i*self.Scale.get(), width, height/2+i*self.Scale.get(), fill="grey")
            self.Canvas.create_text(width/2+self.TextOffset, height/2+i*self.Scale.get(), text=f"-{i}", fill=self.ForegroundColor) if i != 0 and self.Numbers.get() == True else self.doNothing()
            self.Canvas.create_line(0, height/2-i*self.Scale.get(), width, height/2-i*self.Scale.get(), fill="grey")
            self.Canvas.create_text(width/2+self.TextOffset, height/2-i*self.Scale.get(), text=str(i), fill=self.ForegroundColor) if i != 0 and self.Numbers.get() == True else self.doNothing()

        # f(x)
        if fxFunction != "":
            # table
            values = []
            for col in self.cols:
                try:
                    values.append(calculator.quickCalc(fxFunction.replace("x", f"({col})")))
                except:
                    values.append("")
            self.Table.item(self.FirstTableRow, values=values)
            # graph
            values = []
            for i in XvaluesConverted:
                try:
                    values.append((i, calculator.quickCalc(fxFunction.replace("x", f"({i})"))))
                except:
                    pass
            for f in range(len(values)-1):
                if not abs(float(values[f][1]) - float(values[f+1][1])) > 10:
                    self.Canvas.create_line(self.XtoX(values[f][0]), self.YtoY(values[f][1]), self.XtoX(values[f+1][0]), self.YtoY(values[f+1][1]), fill=self.fxColor)
        # g(x)
        if gxFunction != "":
            # table
            values = []
            for col in self.cols:
                try:
                    values.append(calculator.quickCalc(gxFunction.replace("x", f"({col})")))
                except:
                    values.append("")
            self.Table.item(self.SecondTableRow, values=values)
            # graph
            values = []
            for i in XvaluesConverted:
                try:
                    values.append((i, calculator.quickCalc(gxFunction.replace("x", f"({i})"))))
                except:
                    pass
            for f in range(len(values)-1):
                if not abs(float(values[f][1]) - float(values[f+1][1])) > 10:
                    self.Canvas.create_line(self.XtoX(values[f][0]), self.YtoY(values[f][1]), self.XtoX(values[f+1][0]), self.YtoY(values[f+1][1]), fill=self.gxColor)

    def clear(self):
        self.Canvas.delete(tk.ALL)
        emptyness = []
        for col in self.cols:
            emptyness.append("")
            self.Table.item(self.FirstTableRow, values=emptyness)
            self.Table.item(self.SecondTableRow, values=emptyness)
        self.ClearStatus = True
    def setFxColor(self, parent, calculator):
        self.fxColor = colorchooser.askcolor(parent=parent, color=self.fxColor)[1]
        self.fxColorButton.config(fg=self.fxColor, bg=self.fxColor)
        if self.ClearStatus == False:
            self.redraw(calculator)
    def setGxColor(self, parent, calculator):
        self.gxColor = colorchooser.askcolor(parent=parent, color=self.gxColor)[1]
        self.gxColorButton.config(fg=self.gxColor, bg=self.gxColor)
        if self.ClearStatus == False:
            self.redraw(calculator)
    def YtoY(self, y):
        return Decimal(self.Canvas.winfo_height())/Decimal(2)-Decimal(y) * Decimal(self.Scale.get())
    def XtoX(self, x):
        return Decimal(self.Canvas.winfo_width())/Decimal(2)+Decimal(x) * Decimal(self.Scale.get())
    def YbacktoY(self, y):
        return Decimal(y) / Decimal(self.Scale.get()) - (Decimal(self.Canvas.winfo_height())/Decimal(2)) / Decimal(self.Scale.get())
    def XbacktoX(self, x):
        return Decimal(x) / Decimal(self.Scale.get()) - (Decimal(self.Canvas.winfo_width())/Decimal(2)) / Decimal(self.Scale.get())
    def convert(self, func):
        newfunc = ""
        SuperScriptDict = {"\u2070": "0",
                           "\u00b9": "1",
                           "\u00b2": "2",
                           "\u00b3": "3",
                           "\u2074": "4",
                           "\u2075": "5",
                           "\u2076": "6",
                           "\u2077": "7",
                           "\u2078": "8",
                           "\u2079": "9",
                           "\u207a": "+",
                           "\u207b": "-",
                           "\u207d": "(",
                           "\u207e": ")",
                           "\u00b7": "."}
        SuperScript = False
        for char in reversed(func):
            if char in SuperScriptDict:
                if SuperScript == True:
                    newfunc += char.translate(str.maketrans(SuperScriptDict))
                else:
                    newfunc += ")" + char.translate(str.maketrans(SuperScriptDict))
                    SuperScript = True
            else:
                if SuperScript == True:
                    newfunc += "(^"
                SuperScript = False
                newfunc += char
        newfunc = newfunc[::-1]
        print(newfunc)
        finalfunc = ""
        IgnoredChars = ("(", "^", "*", "+", "-", "*", "/", "%", ")")
        for char in newfunc:
            if finalfunc == "":
                finalfunc = char
            elif char == "x":
                if finalfunc[len(finalfunc)-1] not in IgnoredChars[:-1]:
                    finalfunc += "*x"
                else:
                    finalfunc += "x"
            elif char == "(":
                if finalfunc[len(finalfunc)-1].isdigit() or finalfunc[len(finalfunc)-1] in ("x", ")"):
                    finalfunc += "*("
                else:
                    finalfunc += "("
            else:
                if finalfunc[len(finalfunc)-1] in ("x", ")"):
                    if char not in IgnoredChars[1:]:
                        finalfunc += f"*{char}"
                    else:
                        finalfunc += char
                else:
                    if finalfunc[len(finalfunc)-1].isdigit() and not char.isdigit() and char not in IgnoredChars[1:]:
                        finalfunc += f"*{char}"
                    else:
                        finalfunc += char
        print("PraktiGraph: " + finalfunc)
        return finalfunc
    def doNothing(self):
        pass"""
            PraktiGraphMetadata = configparser.ConfigParser()
            PraktiGraphMetadata["PraktiXtension"] = {"name": "PraktiGraph",
                                                          "version": "1.9",
                                                          "filename": "PraktiGraph.py",
                                                          "description": "The PraktiCalc Graph Thing",
                                                          "website": "",
                                                          "minpython": "default",
                                                          "maxpython": "default",
                                                          "sha256": "",
                                                          "requiresinternet": "false",
                                                          "pxtxlink": ""}
            PraktiGraphDescription = """This extension allows to draw simple graphs from mathematical functions.
Please note that you have to write all multiplication operators."""
            with open(self.FolderPath / "PraktiGraph.py", "w", encoding="utf-8") as pgfile:
                pgfile.write(PraktiGraphCode)
            with open(self.FolderPath / "PraktiGraph.ini", "w", encoding="utf-8") as pgmeta:
                PraktiGraphMetadata.write(pgmeta)
            with open(self.FolderPath / "PraktiGraph.txt", "w", encoding="utf-8") as pgdesc:
                pgdesc.write(PraktiGraphDescription)

# console
class Console:
    def __init__(self, cfg):
        self.ConfigurationStorage = cfg
    def execute(self, command): # interpretes and executes a given command
        global lcc
        lcc = command
        if command == "version":
            output = "PraktiCalc Console on PraktiCalc " + PraktiCalcVersion
        elif command == "help":
            output = """PraktiCalc Console Help
***********************
This console was mainly created for debugging purposes.
Available Commands:
function(<function>: executes a function in the program
eval(<command>: executed a Python command within the program
system(<command>: executes a system command and prints the output
varget(<variable>: shows the value of the given variable
confget(<key>: shows the value of the given key from the config

Useful Tips:
- don't close brackets
- use the system command with caution
- don't use sudo with the system command, use run0 instead
- the console is not interactive, it prints the output after processing
- there is a Minecraft reference hidden in the console
"""
        elif command == "/toggledownfall":
            output = "Toggled downfall"
        elif command.startswith("function("):
            command = command[9:]
            if command in globals() and callable(globals()[command]):
                globals()[command]()
                output = "Function executed"
            else:
                output = "[!] Unknown function"
        elif command.startswith("system("):
            command = command[7:]
            output = subprocess.getoutput(command)
        elif command.startswith("varget("):
            command = command[7:]
            if command in globals():
                output = globals()[command]
            else:
                output = "[!] Unknown variable"
        elif command.startswith("eval("):
            command = command[5:]
            try:
                output = eval(command, globals())
            except Exception as error:
                output = f"[!] Failed to execute command:\n{error}"
        elif command.startswith("confget("):
            command = command[8:]
            output = self.ConfigurationStorage.get(command)
            if output == None:
                output = "[!] Unknown value, resetting configuration"
        else:
            output = "[X] Unknown command"
        return output

if __name__ == "__main__":
    cfg = Configuration()
    Calculator = PraktiCalculator(cfg)
    WindowHelp = WindowHelper(cfg)
    WindowDialog = Dialog(cfg)
    PLEL = ExtensionWindow(WindowHelp, Calculator, WindowDialog, cfg)
    PLEL.mainloop()
