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

# MODULES
import tkinter as tk
from tkinter import ttk, messagebox, font, scrolledtext, filedialog, colorchooser
from pathlib import Path
try:
    from ttkthemes import ThemedStyle
    theming = 1
except:
    theming = 0
# 0 = no theming
# 1 = theming from ttkthemes
# 2 = manual theming
import platform, subprocess, sys, shutil, math, getpass, time, configparser, importlib.util, webbrowser, zipfile, tempfile, hashlib, re
if platform.system() == "Windows":
    import winreg
    from ctypes import wintypes
elif platform.system() == "Darwin":
    import plistlib

# VARIABLES
CLIHelp = "--help" in sys.argv
CLIVersion = "--version" in sys.argv
PraktiCalcVersion = "1.5"
BypassWindowsDPIFix = "--nodpiawareness" in sys.argv
allowWindowsShutdownDialog = "--allowShutdownDialog" in sys.argv
MsgBoxStyles = ["Tkinter", "Alternative"]
if platform.system() == "Windows":
    import ctypes
    if theming != 0:
        NativeTheme = "vista"
    if shutil.which("wscript"):
        MsgBoxStyles.append("VBScript")
    if shutil.which("msg"):
        MsgBoxStyles.append("Windows Messaging Service")
    if allowWindowsShutdownDialog == True:
        MsgBoxStyles.append("Windows Shutdown")
    if BypassWindowsDPIFix == False:
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except:
            pass
    if platform.release() == "Vista" or platform.release() == "7" or platform.release() == "8" or platform.release() == "8.1":
        WingWebDings = True
    else:
        WingWebDings = False
        dwmapi = ctypes.WinDLL("dwmapi")
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
elif platform.system() == "Darwin":
    if theming != 0:
        NativeTheme = "aqua"
    WingWebDings = False
    MsgBoxStyles.append("AppleScript")
else:
    WingWebDings = False
    if theming != 0:
        NativeTheme = "default"
    AdditionalLinuxMsgBoxStyles = ["xmessage", "gxmessage", "yad", "kdialog", "zenity", "Xdialog", "notify-send"]
    for MsgBoxStyle in AdditionalLinuxMsgBoxStyles:
        if shutil.which(MsgBoxStyle):
            MsgBoxStyles.append(MsgBoxStyle)
ThemingDisabled = "--notheming" in sys.argv
if ThemingDisabled == True:
    theming = 0
if CLIHelp == True:
    if platform.system() == "Windows":
        messagebox.showinfo("PraktiCalc CLI Options", "PraktiCalc " + PraktiCalcVersion + """ CLI Options:
--borderdisplay: uses window title to show output
--debug: add a test button for debugging
--nodpiawareness: disable Windows DPI Awareness
--dark: enable dark mode by default
--console: show console for debugging
--equilux: set the dark theme to equilux
--help: display this help text and exit
--version: display version and exit""")
    else:
        print("PraktiCalc " + PraktiCalcVersion + " CLI Options")
        print("--debug         | add a test button for debugging")
        if platform.system() != "Darwin":
            if theming != 0:
                print("--dark          | enable dark mode by default")
        print("--console       | show console for debugging")
        if theming != 0:
            print("--notheming     | disables theming")
            print("--equilux       | set the dark theme to equilux")
        print("--help          | display this help text and exit")
        print("--version       | display version and exit")
    sys.exit(0)
if CLIVersion == True:
    if platform.system() == "Windows":
        messagebox.showinfo("PraktiCalc " + PraktiCalcVersion, "PraktiCalc " + PraktiCalcVersion)
    else:
        print("PraktiCalc " + PraktiCalcVersion)
    sys.exit(0)

def testPyInstallerOneFile():
    try:
        print(sys._MEIPASS)
        return True
    except:
        return False

RunningAsOneFileExe = testPyInstallerOneFile()

# ttkthemes directory workaround for AppImage
if Path("./usr/share/tcltk/ttkthemes").exists():
    # If started as AppImage:
    tcl_dir = Path("./usr/share/tcltk/ttkthemes").resolve()

if RunningAsOneFileExe == True:
    if platform.system() == "Darwin":
        PraktiCalcMacIconPath = (sys._MEIPASS + "/PraktiCalc-MacOS.png")
    PraktiCalcIconPath = (sys._MEIPASS + "/PraktiCalculator_icon.png")
    PraktiCalcIconMonoPath = (sys._MEIPASS + "/PraktiCalculator_icon.xbm")
    PraktiCalcIconMonoInvertedPath = (sys._MEIPASS + "/PraktiCalculator_icon_inverted.xbm")
    PythonPowerPath = (sys._MEIPASS + "/python-powered.png")
    VBSInfoPath = (sys._MEIPASS + "/info.vbs")
    VBSErrorPath = (sys._MEIPASS + "/error.vbs")
else:
    if platform.system() == "Darwin":
        PraktiCalcMacIconPath = "PraktiCalc-MacOS.png"
    PraktiCalcIconPath = "PraktiCalculator_icon.png"
    PraktiCalcIconMonoPath = "PraktiCalculator_icon.xbm"
    PraktiCalcIconMonoInvertedPath = "PraktiCalculator_icon_inverted.xbm"
    PythonPowerPath = "python-powered.png"
    VBSInfoPath = "info.vbs"
    VBSErrorPath = "error.vbs"

breeze = "--breeze" in sys.argv
yaru = "--yaru" in sys.argv
keramik = "--keramik" in sys.argv
equilux = "--equilux" in sys.argv
if breeze == True:
    thettktheme = "breeze"
elif yaru == True:
    thettktheme = "yaru"
elif keramik == True:
    thettktheme = "keramik"
else:
    thettktheme = "plastik"
if ThemingDisabled == False:
    DarkMode = "--dark" in sys.argv
    if DarkMode == True:
        thettktheme = "black"
    if equilux == True:
        thettktheme = "equilux"
else:
    DarkMode = False
debug = "--debug" in sys.argv

# CLASSES
class Configuration:
    def __init__(self):
        if platform.system() == "Windows":
            self.backend = WindowsConfig()
        elif platform.system() == "Darwin":
            self.backend = MacConfig()
        else:
            self.backend = XDGConfig()
        try:
            if str(self.get("configVersion")) == "1.0":
                fail = False
                return
            else:
                fail = True
        except:
            fail = True
        finally:
            if fail == True:
                try:
                    self.reset()
                except:
                    pass
                finally:
                    self.create()
    def get(self, key):
        try:
            return self.backend.get(key)
        except:
            try:
                self.reset()
            except:
                pass
            finally:
                self.create()
    def set(self, key, value):
        try:
            self.backend.set(key, value)
        except:
            try:
                self.reset()
            except:
                pass
            finally:
                self.create()
    def create(self):
        self.backend.create()
        if platform.system() == "Windows":
            DefaultConfiguration = (("theme", "black"),
                                    ("nativeTheme", True),
                                    ("dialogStyle", "Alternative"),
                                    ("roundResult", True),
                                    ("showTrailing0", False),
                                    ("angleUnit", "deg"),
                                    ("borderDisplay", False),
                                    ("allowShutdownDialog", False),
                                    ("noDPIAwareness", False),
                                    ("nativeMenuBar", False),
                                    ("menuTearoff", False),
                                    ("configVersion", "1.0"))
        elif platform.system() == "Darwin":
            DefaultConfiguration = (("theme", "plastik"),
                                    ("nativeTheme", True),
                                    ("dialogStyle", "Alternative"),
                                    ("roundResult", True),
                                    ("showTrailing0", False),
                                    ("angleUnit", "deg"),
                                    ("borderDisplay", False),
                                    ("nativeMenuBar", True),
                                    ("configVersion", "1.0"))
        else:
            DefaultConfiguration = (("theme", "plastik"),
                                    ("nativeTheme", False),
                                    ("dialogStyle", "Alternative"),
                                    ("roundResult", True),
                                    ("showTrailing0", False),
                                    ("angleUnit", "deg"),
                                    ("borderDisplay", False),
                                    ("nativeMenuBar", False),
                                    ("menuTearoff", False),
                                    ("configVersion", "1.0"))
        for value in DefaultConfiguration:
            self.backend.set(value[0], value[1])
            print("set " + value[0] + " to " + str(value[1]))
    def reset(self):
        self.backend.reset()
    def remove(self, key):
        try:
            self.backend.remove(key)
        except:
            pass

class WindowsConfig:
    def get(self, key):
        with winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\PraktiCalc") as PraktiKey:
            value = winreg.QueryValueEx(PraktiKey, str(key))[0]
            return value
    def set(self, key, value):
        with winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\PraktiCalc", 0, winreg.KEY_SET_VALUE) as PraktiKey:
            if isinstance(value, str):
                winreg.SetValueEx(PraktiKey, str(key), 0, winreg.REG_SZ, value)
            elif isinstance(value, int):
                winreg.SetValueEx(PraktiKey, str(key), 0, winreg.REG_DWORD, value)
            elif isinstance(value, bool):
                if value == True:
                    winreg.SetValueEx(PraktiKey, str(key), 0, winreg.REG_DWORD, 1)
                elif value == False:
                    winreg.SetValueEx(PraktiKey, str(key), 0, winreg.REG_DWORD, 0)
            else:
                try:
                    showError("Error saving Configuration")
                except:
                    messagebox.showerror("Error writing configuration")
    def create(self):
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\PraktiCalc")
    def reset(self):
        print(subprocess.getoutput(r'reg delete "HKEY_CURRENT_USER\Software\PraktiCalc" /f'))
    def remove(self, key):
        with winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\PraktiCalc", 0, winreg.KEY_SET_VALUE) as PraktiKey:
            winreg.DeleteValue(PraktiKey, key)

class MacConfig:
    def __init__(self):
        self.folder = Path.home() / "Library" / "Preferences"
        self.filepath = self.folder / "com.github.karl152.PraktiCalc.plist"
    def get(self, key):
        with open(self.filepath, "rb") as file:
            content = plistlib.load(file)
            if not isinstance(content[str(key)], bool):
                return content[str(key)]
            else:
                if content[str(key)] == True:
                    return 1
                else:
                    return 0
    def set(self, key, value):
        if isinstance(value, str) or isinstance(value, int) or isinstance(value, bool):
            with open(self.filepath, "rb") as file:
                data = plistlib.load(file)
            data[str(key)] = value
            with open(self.filepath, "wb") as file:
                plistlib.dump(data, file)
        else:
            try:
                showError("Error saving Configuration")
            except:
                messagebox.showerror("Error writing configuration")
    def create(self):
        with open(self.filepath, "wb") as file:
            plistlib.dump({}, file)
    def reset(self):
        Path(self.filepath).unlink()
    def remove(self, key):
        with open(self.filepath, "rb") as file:
            data = plistlib.load(file)
        del data[str(key)]
        with open(self.filepath, "wb") as file:
            plistlib.dump(data, file)

class XDGConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.folder = Path.home() / ".config" / "PraktiCalc"
        self.path = self.folder / "config.ini"
    def get(self, key):
        self.config.read(self.path, encoding="utf-8")
        value = self.config["General"][str(key)]
        try:
            return int(value)
        except:
            if value == "true":
                return 1
            elif value == "false":
                return 0
            else:
                return value
    def set(self, key, value):
        if isinstance(value, str):
            self.config["General"][str(key)] = value
        elif isinstance(value, bool):
            if value == True:
                self.config["General"][str(key)] = "true"
            elif value == False:
                self.config["General"][str(key)] = "false"
        elif isinstance(value, int):
            self.config["General"][str(key)] = str(value)
        else:
            try:
                showError("Error saving Configuration")
            except:
                messagebox.showerror("Error writing configuration")
        with open(self.path, "w", encoding="utf-8") as configfile:
            self.config.write(configfile)
    def create(self):
        self.folder.mkdir(parents=True)
        self.config["General"] = {}
        with open(self.path, "w", encoding="utf-8") as configfile:
            self.config.write(configfile)
    def reset(self):
        shutil.rmtree(self.folder)
    def remove(self, key):
        self.config.read(self.path, encoding="utf-8")
        self.config.remove_option("General", key)
        with open(self.path, "w", encoding="utf-8") as configfile:
            self.config.write(configfile)

# Calculation Unit
class PraktiCalculator:
    def __init__(self, cfg):
        self.CalculationString = "0"
        self.Memory = "0"
        self.HistoryList = []
        self.LastResult = "0"
        self.updateFromSettings(cfg)
    def calculate(self): # does the actual calculation, used to include 171 if-statements
        TheCalc = self.CalculationString.replace("\u221a", "sqrt")
        TheCalc = TheCalc.replace("\u03c0", "pi")
        TheCalc = TheCalc.replace("^", "**")
        if "__" in TheCalc:
            raise ValueError
        try:
            Result = eval(TheCalc, {"__builtins__": None}, self.operators)
        except Exception as e:
            raise e
        if self.Rounding == True:
            Result = str(round(float(Result), 12))
        else:
            Result = str(Result)
        if str(Result).endswith(".0"):
            if self.no0 == False:
                Result = str(Result)[:-2]
            else:
                Result = str(Result)
        else:
            Result = str(Result)
        if Result == "-0":
            Result = "0"
        self.HistoryList.append(f"{self.CalculationString}={Result}")
        self.CalculationString = Result
        self.LastResult = Result
        return Result
    def zero(self): # processes the number zero, which is a special case and seperate
        if self.CalculationString != "0":
            self.CalculationString += "0"
    def clear(self): # resets the calculaton
        self.CalculationString = "0"
    def append(self, char): # append a character to the calculation string
        char = char.replace("plus", "+")
        char = char.replace("minus", "-")
        char = char.replace("asterisk", "*")
        char = char.replace("slash", "/")
        char = char.replace("comma", ".")
        char = char.replace("parenleft", "(")
        char = char.replace("parenright", ")")
        if self.CalculationString == "0" and char != ".":
            self.CalculationString = char
        else:
            self.CalculationString += char
    def backspace(self): # backspace button
        if self.CalculationString == "0":
            pass
        elif len(self.CalculationString) <= 1:
            self.CalculationString = "0"
        else:
            self.CalculationString = self.CalculationString[:-1]
    def setMemory(self): # sets the memory to the output
        self.Memory = self.CalculationString
    def getMemory(self): # adds the memory value to the calculation string
        if self.CalculationString == "0":
            self.CalculationString = self.Memory
        else:
            self.CalculationString += self.Memory
    def clearMemory(self):
        self.Memory = "0"
    def clearHistory(self): # clears the history list
        self.HistoryList.clear()
    def xcheck(self): # debug function to return some variables
        return self.CalculationString, self.Memory, self.LastResult, self.HistoryList, self.operators
    def quickCalc(self, expression):
        PreviousResult = self.LastResult
        self.clear()
        self.setOperators("rad")
        self.append(expression)
        result = self.calculate()
        self.clear()
        self.HistoryList.pop()
        self.LastResult = PreviousResult
        self.setOperators(self.TrigMode)
        return result
    def setOperators(self, TrigMode):
        self.operators = {}
        self.operators["sqrt"] = math.sqrt
        if TrigMode == "rad":
            self.operators["sin"] = math.sin
            self.operators["cos"] = math.cos
            self.operators["tan"] = math.tan
            self.operators["asin"] = math.asin
            self.operators["acos"] = math.acos
            self.operators["atan"] = math.atan
        elif TrigMode == "deg":
            self.operators["sin"] = lambda x: math.sin(math.radians(x))
            self.operators["cos"] = lambda x: math.cos(math.radians(x))
            self.operators["tan"] = lambda x: math.tan(math.radians(x))
            self.operators["asin"] = lambda x: math.asin(math.radians(x))
            self.operators["acos"] = lambda x: math.acos(math.radians(x))
            self.operators["atan"] = lambda x: math.atan(math.radians(x))
        elif TrigMode == "gon":
            self.operators["sin"] = lambda x: math.sin(x * math.pi / 200)
            self.operators["cos"] = lambda x: math.cos(x * math.pi / 200)
            self.operators["tan"] = lambda x: math.tan(x * math.pi / 200)
            self.operators["asin"] = lambda x: math.asin(x) * 200 / math.pi
            self.operators["acos"] = lambda x: math.acos(x) * 200 / math.pi
            self.operators["atan"] = lambda x: math.atan(x) * 200 / math.pi
        self.operators["sinh"] = math.sinh
        self.operators["cosh"] = math.cosh
        self.operators["tanh"] = math.tanh
        self.operators["asinh"] = math.asinh
        self.operators["acosh"] = math.acosh
        self.operators["atanh"] = math.atanh
        self.operators["ld"] = math.log2
        self.operators["ln"] = math.log
        self.operators["lg"] = math.log10
        self.operators["fact"] = math.factorial
        self.operators["pi"] = math.pi
        self.operators["e"] = math.e
    def updateFromSettings(self, cfg):
        self.TrigMode = cfg.get("angleUnit") # rad, deg, gon
        self.setOperators(self.TrigMode)
        self.Rounding = bool(cfg.get("roundResult"))
        self.no0 = bool(cfg.get("showTrailing0"))

# provides settings, theming and ajustments for windows
class WindowHelper:
    def __init__(self, cfg):
        self.WindowList = []
        self.ConfigurationStorage = cfg
    def changeTheme(self, WindowName): # sets the theme for a given window
        global theming, DarkMode
        if bool(cfg.get("nativeTheme")) == False and cfg.get("theme") == "black" or cfg.get("theme") == "equilux":
            DarkMode = True
        else:
            DarkMode = False
        if platform.system() == "Darwin":
            if bool(self.ConfigurationStorage.get("nativeTheme")) == False:
                self.style = ThemedStyle(WindowName)
                self.style.theme_use(self.ConfigurationStorage.get("theme"))
            else:
                self.style = ttk.Style(WindowName)
                self.style.theme_use(NativeTheme)
        elif platform.system() == "Windows":
            self.ajustTitleBars()
            if bool(self.ConfigurationStorage.get("nativeTheme")) == False:
                self.style = ThemedStyle(WindowName)
                self.style.theme_use(self.ConfigurationStorage.get("theme"))
            else:
                self.style = ttk.Style(WindowName)
                self.style.theme_use(NativeTheme)
            if WingWebDings == True:
                self.style.configure("Webdings.TButton", font=webdingsfont)
                self.style.configure("Wingdings.TButton", font=wingdingsfont)
            else:
                self.style.configure("LargeUnicode.TButton", font=LargeUnicodeFont)
            self.style.configure("Treeview", rowheight=40)
        elif theming == 1 or theming == 2:
            try:
                if bool(self.ConfigurationStorage.get("nativeTheme")) == False:
                    self.style = ThemedStyle(WindowName)
                    self.style.theme_use(self.ConfigurationStorage.get("theme"))
                else:
                    self.style = ttk.Style(WindowName)
                    self.style.theme_use(NativeTheme)
                    self.style.configure("LargeUnicode.TButton", font=LargeUnicodeFont)
                    self.style.configure("Treeview", rowheight=40)
            except:
                theming = 2
                if bool(self.ConfigurationStorage.get("nativeTheme")) == True:
                    self.style = ttk.Style(WindowName)
                    self.style.theme_use(NativeTheme)
                else:
                    theme_base = Path(sys._MEIPASS).joinpath("ttkthemes", "themes")
                    theme_path = Path(theme_base).joinpath(self.ConfigurationStorage.get("theme"))
                    WindowName.tk.call("lappend", "auto_path", theme_base)
                    try:
                        WindowName.tk.call("package", "require", f"ttk::theme::{self.ConfigurationStorage.get('theme')}")
                    except:
                        theme_tcl = Path(theme_path).joinpath(self.ConfigurationStorage.get("theme") + ".tcl")
                        if Path(theme_tcl).exists():
                            WindowName.tk.call("source", theme_tcl)
                        else:
                            print(f"Couldn't find theme {theme_tcl}")
                    self.style = ttk.Style()
                    try:
                        self.style.theme_use(self.ConfigurationStorage.get("theme"))
                    except:
                        print("Using default ttk theme")
            try:
                self.style.configure("LargeUnicode.TButton", font=LargeUnicodeFont)
                self.style.configure("Treeview", rowheight=40)
            except:
                print("Unable to increase font size of some buttons and row height in the history window")
    def ajustTitleBar(self, hwnd): # changes the appearance of the Windows title bar
        if platform.system() == "Windows":
            try:
                value = wintypes.BOOL(DarkMode)
                dwmapi.DwmSetWindowAttribute(wintypes.HWND(hwnd), wintypes.DWORD(DWMWA_USE_IMMERSIVE_DARK_MODE), ctypes.byref(value), ctypes.sizeof(value))
            except:
                pass
    def ajustTitleBars(self): # changes the appearance of all Windows title bars
        for window in self.WindowList:
            try:
                self.ajustTitleBar(ctypes.windll.user32.GetParent(window.winfo_id()))
            except:
                pass
    def close(self, window):
        window.destroy()
        self.WindowList.remove(window)

# main window
class MainWindow(tk.Tk):
    def __init__(self, helper, calculator, dialog, cfg):
        global wingdingsfont, webdingsfont, LargeUnicodeFont
        super().__init__()
        self.title("PraktiCalc")
        self.DPI = self.winfo_fpixels("1i")
        if platform.system() == "Windows":
            if cfg.get("noDPIAwareness") == 1:
                self.ScaleFactor = 1
            else:
                self.ScaleFactor = self.DPI/72
        else:
            self.ScaleFactor = self.DPI/72
        print(self.DPI)
        print(self.ScaleFactor)
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
        self.UseNativeThemeTkVar = tk.BooleanVar(value=bool(cfg.get("nativeTheme")))
        self.BorderDisplayTkVar = tk.BooleanVar(value=bool(cfg.get("borderDisplay")))
        self.CurrentMsgBoxStyleTkVar = tk.StringVar(value=cfg.get("dialogStyle"))
        self.NativeMenubarTkVar = tk.BooleanVar(value=NativeMenubar)
        self.AngleUnitTkVar = tk.StringVar(value=cfg.get("angleUnit"))
        self.RoundResultTkVar = tk.BooleanVar(value=bool(cfg.get("roundResult")))
        self.showTrailingZeroTkVar = tk.BooleanVar(value=bool(cfg.get("showTrailing0")))
        self.config(width=256, height=315)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        if platform.system() != "Darwin":
            TheTearoff = cfg.get("menuTearoff")
        else:
            TheTearoff = 0
        self.MenuTearoffTkVar = tk.BooleanVar(value=bool(TheTearoff))
        self.Menubar = tk.Menu(self)
        self.CalculatorMenu = tk.Menu(self.Menubar, tearoff=TheTearoff)
        self.CalculatorMenu.add_command(label="Quit", command=lambda: helper.close(self))
        self.ToolMenu = tk.Menu(self.Menubar, tearoff=TheTearoff)
        self.ToolMenu.add_command(label="History", command=lambda: HistoryWindow(self, calculator, helper))
        self.ToolMenu.add_command(label="Extensions", command=lambda: ExtensionWindow(self, helper, calculator, dialog))
        self.ToolMenu.add_separator()
        self.ToolMenu.add_command(label="Settings", command=lambda: SettingsWindow(self, helper, calculator, cfg))
        self.HelpMenu = tk.Menu(self.Menubar, tearoff=TheTearoff)
        self.HelpMenu.add_command(label="About", command=lambda: dialog.info(self, helper))
        self.Menubar.add_cascade(label="Calculator", menu=self.CalculatorMenu)
        self.Menubar.add_cascade(label="Tools", menu=self.ToolMenu)
        self.Menubar.add_cascade(label="Help", menu=self.HelpMenu)
        self.MenuBarFrame = ttk.Frame(self)
        self.CalculatorMenuButton = ttk.Menubutton(self.MenuBarFrame, text="Calculator")
        self.CalculatorCustomMenu = tk.Menu(self.CalculatorMenuButton, tearoff=TheTearoff)
        self.CalculatorCustomMenu.add_command(label="Quit", command=lambda: helper.close(self))
        self.CalculatorMenuButton["menu"] = self.CalculatorCustomMenu
        self.ToolMenuButton = ttk.Menubutton(self.MenuBarFrame, text="Tools")
        self.ToolCustomMenu = tk.Menu(self.ToolMenuButton, tearoff=TheTearoff)
        self.ToolCustomMenu.add_command(label="History", command=lambda: HistoryWindow(self, calculator, helper))
        self.ToolCustomMenu.add_command(label="Extensions", command=lambda: ExtensionWindow(self, helper, calculator, dialog))
        self.ToolCustomMenu.add_separator()
        self.ToolCustomMenu.add_command(label="Settings", command=lambda: SettingsWindow(self, helper, calculator, cfg))
        self.ToolMenuButton["menu"] = self.ToolCustomMenu
        self.HelpMenuButton = ttk.Menubutton(self.MenuBarFrame, text="Help")
        self.HelpCustomMenu = tk.Menu(self.HelpMenuButton, tearoff=TheTearoff)
        self.HelpCustomMenu.add_command(label="About", command=lambda: dialog.info(self, helper))
        self.HelpMenuButton["menu"] = self.HelpCustomMenu
        self.CalculatorMenuButton.grid(row=0, column=0, sticky="w")
        self.ToolMenuButton.grid(row=0, column=1, sticky="w")
        self.HelpMenuButton.grid(row=0, column=2, sticky="w")
        if NativeMenubar == True:
            self.config(menu=self.Menubar)
        else:
            self.MenuBarFrame.grid(row=0, column=0, sticky="ew")
        self.WindowFrame = ttk.Frame(self)
        for colrow in range(5):
            self.WindowFrame.rowconfigure(colrow, weight=1, uniform="buttons")
            self.WindowFrame.columnconfigure(colrow, weight=1, uniform="buttons")
        self.WindowFrame.rowconfigure(5, weight=1)
        self.WindowFrame.rowconfigure(6, weight=1)
        if bool(cfg.get("borderDisplay")) == True:
            self.WindowFrame.rowconfigure(0, weight=0, uniform="")
        self.Output = ttk.Entry(self.WindowFrame)
        self.Output.insert(0, "0")
        self.Output.config(state="readonly")
        # BUTTONS
        PlusButton = ttk.Button(self.WindowFrame, text="+", command=lambda: self.append("plus", calculator, cfg))
        MinusButton = ttk.Button(self.WindowFrame, text="-", command=lambda: self.append("minus", calculator, cfg))
        MultiplyButton = ttk.Button(self.WindowFrame, text="x", command=lambda: self.append("asterisk", calculator, cfg))
        DivideButton = ttk.Button(self.WindowFrame, text="÷", command=lambda: self.append("slash", calculator, cfg))
        SevenButton = ttk.Button(self.WindowFrame, text="7", command=lambda: self.append("7", calculator, cfg))
        EightButton = ttk.Button(self.WindowFrame, text="8", command=lambda: self.append("8", calculator, cfg))
        NineButton = ttk.Button(self.WindowFrame, text="9", command=lambda: self.append("9", calculator, cfg))
        CEButton = ttk.Button(self.WindowFrame, text="CE", command=lambda: self.clear(calculator, cfg))
        FourButton = ttk.Button(self.WindowFrame, text="4", command=lambda: self.append("4", calculator, cfg))
        FiveButton = ttk.Button(self.WindowFrame, text="5", command=lambda: self.append("5", calculator, cfg))
        SixButton = ttk.Button(self.WindowFrame, text="6", command=lambda: self.append("6", calculator, cfg))
        CommaButton = ttk.Button(self.WindowFrame, text=",", command=lambda: self.append("comma", calculator, cfg))
        OneButton = ttk.Button(self.WindowFrame, text="1", command=lambda: self.append("1", calculator, cfg))
        TwoButton = ttk.Button(self.WindowFrame, text="2", command=lambda: self.append("2", calculator, cfg))
        ThreeButton = ttk.Button(self.WindowFrame, text="3", command=lambda: self.append("3", calculator, cfg))
        EqualButton = ttk.Button(self.WindowFrame, text="=", command=lambda: self.calculate(self, helper, calculator, dialog, cfg))
        InfoButton = ttk.Button(self.WindowFrame, text="i", command=lambda: dialog.info(self, helper))
        ZeroButton = ttk.Button(self.WindowFrame, text="0", command=lambda: self.zero(calculator, cfg))
        self.ExitButton = ttk.Button(self.WindowFrame, text="X", command=lambda: helper.close(self))
        LeftParenButton = ttk.Button(self.WindowFrame, text="(", command=lambda: self.append("parenleft", calculator, cfg))
        RightParenButton = ttk.Button(self.WindowFrame, text=")", command=lambda: self.append("parenright", calculator, cfg))
        if WingWebDings == True:
            SettingsButton = ttk.Button(self.WindowFrame, text="@", command=lambda: SettingsWindow(self, helper, calculator, cfg), style="Webdings.TButton")
            self.BackspaceButton = ttk.Button(self.WindowFrame, text="Õ", command=lambda: self.backspace(calculator, cfg), style="Wingdings.TButton")
            HistoryButton = ttk.Button(self.WindowFrame, text="0", command=lambda: HistoryWindow(self, calculator, helper), style="Wingdings.TButton")
            self.CopyButton = ttk.Button(self.WindowFrame, text="4", command=self.copyResult, style="Wingdings.TButton")
        else:
            SettingsButton = ttk.Button(self.WindowFrame, text="\u26ed", command=lambda: SettingsWindow(self, helper, calculator, cfg), style="LargeUnicode.TButton")
            self.BackspaceButton = ttk.Button(self.WindowFrame, text="\u232b", command=lambda: self.backspace(calculator, cfg))
            HistoryButton = ttk.Button(self.WindowFrame, text="\u23f2", command=lambda: HistoryWindow(self, calculator, helper), style="LargeUnicode.TButton")
            self.CopyButton = ttk.Button(self.WindowFrame, text="\u2398", command=self.copyResult, style="LargeUnicode.TButton")
        ModuloButton = ttk.Button(self.WindowFrame, text="%", command=lambda: self.append("%", calculator, cfg))
        Checkb = ttk.Button(self, text="Check", command=lambda: print(calculator.xcheck())) # some debug thing
        sqrtButton = ttk.Button(self.WindowFrame, text="\u221a", command=lambda: self.append("\u221a" + "(", calculator, cfg))
        More = ttk.Button(self.WindowFrame, text="...", command=lambda: ExtensionWindow(self, helper, calculator, dialog))
        PowerButton = ttk.Button(self.WindowFrame, text="x^y", command=lambda: self.append("^", calculator, cfg))
        SetMemoryButton = ttk.Button(self.WindowFrame, text="SM", command=lambda: self.setMemory(calculator))
        GetMemoryButton = ttk.Button(self.WindowFrame, text="GM", command=lambda: self.getMemory(calculator))
        SinButton = ttk.Menubutton(self.WindowFrame, text="sin")
        SinMenu = tk.Menu(SinButton, tearoff=TheTearoff)
        SinMenu.add_command(label="sin", command=lambda: self.append("sin(", calculator, cfg))
        SinMenu.add_command(label="asin", command=lambda: self.append("asin(", calculator, cfg))
        SinMenu.add_command(label="sinh", command=lambda: self.append("sinh(", calculator, cfg))
        SinMenu.add_command(label="asinh", command=lambda: self.append("asinh(", calculator, cfg))
        SinButton["menu"] = SinMenu
        CosButton = ttk.Menubutton(self.WindowFrame, text="cos")
        CosMenu = tk.Menu(CosButton, tearoff=TheTearoff)
        CosMenu.add_command(label="cos", command=lambda: self.append("cos(", calculator, cfg))
        CosMenu.add_command(label="acos", command=lambda: self.append("acos(", calculator, cfg))
        CosMenu.add_command(label="cosh", command=lambda: self.append("cosh(", calculator, cfg))
        CosMenu.add_command(label="acosh", command=lambda: self.append("acosh(", calculator, cfg))
        CosButton["menu"] = CosMenu
        TanButton = ttk.Menubutton(self.WindowFrame, text="tan")
        TanMenu = tk.Menu(TanButton, tearoff=TheTearoff)
        TanMenu.add_command(label="tan", command=lambda: self.append("tan(", calculator, cfg))
        TanMenu.add_command(label="atan", command=lambda: self.append("atan(", calculator, cfg))
        TanMenu.add_command(label="tanh", command=lambda: self.append("tanh(", calculator, cfg))
        TanMenu.add_command(label="atanh", command=lambda: self.append("atanh(", calculator, cfg))
        TanButton["menu"] = TanMenu
        LdButton = ttk.Button(self.WindowFrame, text="ld", command=lambda: self.append("ld(", calculator, cfg))
        LnButton = ttk.Button(self.WindowFrame, text="ln", command=lambda: self.append("ln(", calculator, cfg))
        LgButton = ttk.Button(self.WindowFrame, text="lg", command=lambda: self.append("lg(", calculator, cfg))
        MemoryButton = ttk.Menubutton(self.WindowFrame, text="M")
        MemoryMenu = tk.Menu(MemoryButton, tearoff=TheTearoff)
        MemoryMenu.add_command(label="Set", command=lambda: self.setMemory(calculator))
        MemoryMenu.add_command(label="Get", command=lambda: self.getMemory(calculator))
        MemoryMenu.add_command(label="Clear", command=lambda: self.clearMemory(calculator))
        MemoryButton["menu"] = MemoryMenu
        LogButton = ttk.Menubutton(self.WindowFrame, text="log")
        LogMenu = tk.Menu(LogButton, tearoff=TheTearoff)
        LogMenu.add_command(label="ld", command=lambda: self.append("ld(", calculator, cfg))
        LogMenu.add_command(label="ln", command=lambda: self.append("ln(", calculator, cfg))
        LogMenu.add_command(label="lg", command=lambda: self.append("lg(", calculator, cfg))
        LogButton["menu"] = LogMenu
        FactButton = ttk.Button(self.WindowFrame, text="!", command=lambda: self.append("fact(", calculator, cfg))
        KonstantButton = ttk.Menubutton(self.WindowFrame, text="\u03c0")
        KonstantMenu = tk.Menu(KonstantButton, tearoff=TheTearoff)
        KonstantMenu.add_command(label="\u03c0", command=lambda: self.append("\u03c0", calculator, cfg))
        KonstantMenu.add_command(label="e", command=lambda: self.append("e", calculator, cfg))
        KonstantButton["menu"] = KonstantMenu
        self.WindowFrame.grid(row=1, column=0, sticky="nesw")
        if bool(cfg.get("borderDisplay")) == False:
            self.Output.grid(row=0, column=0, columnspan=3, sticky="nesw")
            self.CopyButton.grid(row=0, column=3, sticky="nesw")
            self.BackspaceButton.grid(row=0, column=4, sticky="nesw")
        else:
            pass
        PlusButton.grid(row=1, column=3, sticky="nesw")
        MinusButton.grid(row=2, column=3, sticky="nesw")
        MultiplyButton.grid(row=3, column=3, sticky="nesw")
        DivideButton.grid(row=4, column=3, sticky="nesw")
        SevenButton.grid(row=2, column=0, sticky="nesw")
        EightButton.grid(row=2, column=1, sticky="nesw")
        NineButton.grid(row=2, column=2, sticky="nesw")
        CEButton.grid(row=1, column=4, sticky="nesw")
        FourButton.grid(row=3, column=0, sticky="nesw")
        FiveButton.grid(row=3, column=1, sticky="nesw")
        SixButton.grid(row=3, column=2, sticky="nesw")
        CommaButton.grid(row=5, column=2, sticky="nesw")
        OneButton.grid(row=4, column=0, sticky="nesw")
        TwoButton.grid(row=4, column=1, sticky="nesw")
        ThreeButton.grid(row=4, column=2, sticky="nesw")
        EqualButton.grid(row=5, column=3, sticky="nesw")
        ZeroButton.grid(row=5, column=0, columnspan=2, sticky="nesw")
        ModuloButton.grid(row=4, column=4, sticky="nesw")
        sqrtButton.grid(row=3, column=4, sticky="nesw")
        LeftParenButton.grid(row=1, column=1, sticky="nesw")
        RightParenButton.grid(row=1, column=2, sticky="nesw")
        PowerButton.grid(row=2, column=4, sticky="nesw")
        SinButton.grid(row=6, column=0, sticky="nesw")
        CosButton.grid(row=6, column=1, sticky="nesw")
        TanButton.grid(row=6, column=2, sticky="nesw")
        MemoryButton.grid(row=1, column=0, sticky="nesw")
        LogButton.grid(row=6, column=3, sticky="nesw")
        FactButton.grid(row=5, column=4, sticky="nesw")
        KonstantButton.grid(row=6, column=4, sticky="nesw")
        self.bind("<Key>", lambda event: self.KeyPress(event, calculator, helper, dialog))
        if debug == True:
            Checkb.grid(row=2, column=0, sticky="nesw")
        if platform.system() == "Darwin":
            pass
        else:
            self.geometry(f"{self.size}x{self.size}")
        self.protocol("WM_DELETE_WINDOW", lambda: helper.close(self))
        self.update_idletasks()
        helper.WindowList.append(self)
        helper.changeTheme(self)
    def KeyPress(self, event, calculator, helper, dialog): # processes keyboard input
        Key = event.keysym
        if Key in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "plus", "minus", "asterisk", "slash", "comma", "parenleft", "parenright"]:
            self.append(Key, calculator, cfg)
        else:
            Keys = {
                "0": lambda: self.zero(calculator, cfg),
                "equal": lambda: self.calculate(self, helper, calculator, dialog),
                "Return": lambda: self.calculate(self, helper, calculator, dialog),
                "h": lambda: HistoryWindow(self, calculator, helper),
                "H": lambda: HistoryWindow(self, calculator, helper),
                "i": lambda: dialog.info(self, helper),
                "s": lambda: SettingsWindow(self, helper, calculator, cfg),
                "S": lambda: SettingsWindow(self, helper, calculator, cfg),
                "BackSpace": lambda: self.backspace(calculator, cfg),
                }
            run = Keys.get(Key)
            if run:
                run()
    def applySettings(self, calculator, cfg): # toggles border display
        if bool(cfg.get("borderDisplay")) == False:
            self.title("PraktiCalc")
            self.Output.grid(row=0, column=0, columnspan=3, sticky="nesw")
            self.CopyButton.grid(row=0, column=3, sticky="nesw")
            self.BackspaceButton.grid(row=0, column=4, sticky="nesw")
            self.WindowFrame.rowconfigure(0, weight=1)
            self.updateDisplay(calculator, cfg)
        elif bool(cfg.get("borderDisplay")) == True:
            self.title("Border Display")
            self.Output.grid_remove()
            self.CopyButton.grid_remove()
            self.BackspaceButton.grid_remove()
            self.WindowFrame.rowconfigure(0, weight=0, uniform="")
            self.updateDisplay(calculator, cfg)
        if bool(cfg.get("nativeMenuBar")) == True:
            self.MenuBarFrame.grid_remove()
            self.config(menu=self.Menubar)
        elif bool(cfg.get("nativeMenuBar")) == False:
            self.MenuBarFrame.grid(row=0, column=0, sticky="ew")
            self.config(menu="")
        calculator.updateFromSettings(cfg)
            
    def copyResult(self): # copies the result
        self.clipboard_clear()
        self.clipboard_append(self.Output.get())
        self.update()
    def updateDisplay(self, calculator, cfg): # updates output
        if cfg.get("borderDisplay") == True:
            self.title(calculator.CalculationString)
        else:
            self.Output.config(state="normal")
            self.Output.delete(0, tk.END)
            self.Output.insert(0, calculator.CalculationString)
            self.Output.config(state="readonly")
    def append(self, value, calculator, cfg):
        calculator.append(value)
        self.updateDisplay(calculator, cfg)
    def zero(self, calculator, cfg):
        calculator.zero()
        self.updateDisplay(calculator, cfg)
    def calculate(self, parent, helper, calculator, dialog, cfg):
        try:
            calculator.calculate()
        except Exception as e:
            dialog.error(str(e), parent, helper)
        self.updateDisplay(calculator, cfg)
    def clear(self, calculator, cfg):
        calculator.clear()
        self.updateDisplay(calculator, cfg)
    def backspace(self, calculator, cfg):
        calculator.backspace()
        self.updateDisplay(calculator, cfg)
    def setMemory(self, calculator):
        calculator.setMemory()
    def getMemory(self, calculator, cfg):
        calculator.getMemory()
        self.updateDisplay(calculator, cfg)
    def clearMemory(self, calculator):
        calculator.clearMemory()

# settings window
class SettingsWindow(tk.Toplevel):
    def __init__(self, parent, helper, calculator, cfg):
        global MsgBoxStyles, theming
        super().__init__(parent)
        self.title("Settings")
        self.config(width=250, height=152)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        if platform.system() == "Windows":
            self.attributes("-toolwindow", True)
            self.focus_force()
        SettingsWindowFrame = ttk.Frame(self)
        SettingsWindowFrame.columnconfigure(0, weight=1)
        SettingsWindowFrame.columnconfigure(1, weight=1)
        SettingsWindowFrame.rowconfigure(0, weight=1)
        SettingsTabs = ttk.Notebook(SettingsWindowFrame)
        SettingsTabs.grid(row=0, column=0, columnspan=2, sticky="news")
        AppearanceFrame = ttk.Frame(SettingsTabs)
        AppearanceFrame.columnconfigure(0, weight=1)
        BehaviorFrame = ttk.Frame(SettingsTabs)
        BehaviorFrame.columnconfigure(0, weight=1)
        SettingsTabs.add(AppearanceFrame, text="Appearance")
        SettingsTabs.add(BehaviorFrame, text="Behavior")
        ThemeFrame = ttk.LabelFrame(AppearanceFrame, text="Theme")
        ThemeFrame.columnconfigure(0, weight=1)
        self.ThemeSelector = ttk.Combobox(ThemeFrame, values=["plastik", "keramik", "breeze", "yaru", "black", "classic"])
        self.ThemeSelector.set(cfg.get("theme"))
        NativeThemeToggle = ttk.Checkbutton(ThemeFrame, text="Native theme", variable=parent.UseNativeThemeTkVar)
        ThemeFrame.grid(row=0, column=0, sticky="news", padx=10)
        self.ThemeSelector.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        NativeThemeToggle.grid(row=1, column=0, sticky="w")
        BorderDisplayToggle = ttk.Checkbutton(AppearanceFrame, text="Border display", variable=parent.BorderDisplayTkVar)
        NativeMenubarToggle = ttk.Checkbutton(AppearanceFrame, text="Native menubar", variable=parent.NativeMenubarTkVar)
        if platform.system() != "Darwin":
            MenuTearoffToggle = ttk.Checkbutton(AppearanceFrame, text="Menu tearoff", variable=parent.MenuTearoffTkVar, command=lambda: messagebox.showinfo("Restart required", "You have to restart PraktiCalc to apply this setting"))
        MsgBoxStyleFrame = ttk.LabelFrame(AppearanceFrame, text="Dialog style")
        MsgBoxStyleFrame.columnconfigure(0, weight=1)
        MsgBoxStyleSelect = ttk.OptionMenu(MsgBoxStyleFrame, parent.CurrentMsgBoxStyleTkVar, cfg.get("dialogStyle"), *MsgBoxStyles)
        AngleUnitFrame = ttk.LabelFrame(BehaviorFrame, text="Angle unit")
        ttk.Radiobutton(AngleUnitFrame, text="Degrees", value="deg", variable=parent.AngleUnitTkVar).grid(row=0, column=0, sticky="w")
        ttk.Radiobutton(AngleUnitFrame, text="Radians", value="rad", variable=parent.AngleUnitTkVar).grid(row=1, column=0, sticky="w")
        ttk.Radiobutton(AngleUnitFrame, text="Gradians", value="gon", variable=parent.AngleUnitTkVar).grid(row=2, column=0, sticky="w")
        AngleUnitFrame.grid(row=0, column=0, padx=10, sticky="we")
        ttk.Checkbutton(BehaviorFrame, text="Round result", variable=parent.RoundResultTkVar).grid(row=1, column=0, padx=10, sticky="w")
        ttk.Checkbutton(BehaviorFrame, text="Show trailing .0", variable=parent.showTrailingZeroTkVar).grid(row=2, column=0, padx=10, sticky="w")
        SettingsOKButton = ttk.Button(SettingsWindowFrame, text="OK", command=lambda: self.loadTheme(parent, helper, cfg, calculator))
        SettingsResetButton = ttk.Button(SettingsWindowFrame, text="Reset", command=lambda: self.reset(parent, helper, cfg))
        SettingsWindowFrame.grid(row=0, column=0, sticky="nesw")
        if theming == 0:
            self.ThemeSelector.config(state="disabled")
            NativeThemeToggle.config(state="disabled")
        BorderDisplayToggle.grid(row=1, column=0, sticky="w", padx=10)
        NativeMenubarToggle.grid(row=2, column=0, sticky="w", padx=10)
        if platform.system() != "Darwin":
            MenuTearoffToggle.grid(row=3, column=0, sticky="w", padx=10)
        MsgBoxStyleFrame.grid(row=4, column=0, sticky="ew", padx=10, pady=(0, 10))
        MsgBoxStyleSelect.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        SettingsOKButton.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
        SettingsResetButton.grid(row=1, column=1, sticky="ew", padx=10, pady=10)
        self.protocol("WM_DELETE_WINDOW", lambda: helper.close(self))
        self.update_idletasks()
        helper.WindowList.append(self)
        helper.changeTheme(self)
    def loadTheme(self, parent, helper, cfg, calculator): # saves the selected theme choice in the settigns window
        cfg.set("theme", self.ThemeSelector.get())
        cfg.set("nativeTheme", parent.UseNativeThemeTkVar.get())
        cfg.set("borderDisplay", parent.BorderDisplayTkVar.get())
        cfg.set("nativeMenuBar", parent.NativeMenubarTkVar.get())
        cfg.set("menuTearoff", parent.MenuTearoffTkVar.get())
        cfg.set("roundResult", parent.RoundResultTkVar.get())
        cfg.set("showTrailing0", parent.showTrailingZeroTkVar.get())
        cfg.set("angleUnit", parent.AngleUnitTkVar.get())
        try:
            helper.changeTheme(parent)
        except:
            pass
        helper.ajustTitleBars()
        cfg.set("dialogStyle", parent.CurrentMsgBoxStyleTkVar.get())
        parent.applySettings(calculator, cfg)
        helper.close(self)
    def reset(self, parent, helper, cfg):
        cfg.reset()
        helper.close(parent)

# info and error dialogs
class Dialog:
    def __init__(self, cfg):
        self.ConfigurationStorage = cfg
    def info(self, parent, helper): # shows info dialogs
        infotext = "PraktiCalc\nVersion " + PraktiCalcVersion + "\nrunning on Python "+ platform.python_version() + "\nLicensed under GPLv3\nread more at https://www.gnu.org/licenses/\nthemes provided by the ttkthemes library"
        if self.ConfigurationStorage.get("dialogStyle") == "Tkinter":
            messagebox.showinfo("About PraktiCalc", infotext)
        elif self.ConfigurationStorage.get("dialogStyle") == "Alternative":
            CustomInfox = tk.Toplevel(parent)
            self.PythonPower = tk.PhotoImage(file=PythonPowerPath)
            CustomInfox.title("About PraktiCalc")
            CustomInfox.bind("<Return>", lambda event: self.close(helper, CustomInfox))
            CustomInfox.rowconfigure(0, weight=1)
            CustomInfox.columnconfigure(0, weight=1)
            if platform.system() == "Windows":
                CustomInfox.attributes("-toolwindow", True)
                CustomInfox.focus_force()
            CustomInfoFrame = ttk.Frame(CustomInfox)
            CustomInfoFrame.rowconfigure(0, weight=1)
            CustomInfoFrame.columnconfigure(0, weight=1)
            CustomInfoExit = ttk.Button(CustomInfoFrame, text="OK", command=lambda: helper.close(CustomInfox))
            ExtendedInfoFrame = ttk.LabelFrame(CustomInfoFrame, relief="sunken", text="[i]")
            ExtendedInfoFrame.rowconfigure(0, weight=1)
            ExtendedInfoFrame.rowconfigure(1, weight=1)
            ExtendedInfoFrame.columnconfigure(0, weight=1)
            ExtInfoIcon = ttk.Label(ExtendedInfoFrame, image=parent.icon)
            ExtInfoText1 = ttk.Label(ExtendedInfoFrame, text=infotext, justify="left")
            CustomInfoFrame.grid(row=0, column=0, sticky="nesw")
            CustomInfoExit.grid(row=1, column=1, padx=10, pady=10)
            ttk.Button(CustomInfoFrame, image=self.PythonPower, command=lambda: webbrowser.open_new_tab("https://www.python.org/")).grid(row=1, column=0, padx=10, pady=10, sticky="sw")
            ExtendedInfoFrame.grid(row=0, column=0, padx=20, pady=10, sticky="nesw")
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
                    "VBScript": lambda: subprocess.Popen(["wscript", VBSInfoPath, PraktiCalcVersion, pyver]),
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
                    "xmessage": lambda: subprocess.Popen(["xmessage", "-title", "About PraktiCalc", infotext]),
                    "gxmessage": lambda: subprocess.Popen(["gxmessage", "-title", "About PraktiCalc", infotext]),
                    "yad": lambda: subprocess.Popen(["yad", "--title=About PraktiCalc", "--info", "--image=" + PraktiCalcIconPath, "--button=OK", "--text=" + infotext]),
                    "kdialog": lambda: subprocess.Popen(["kdialog", "--title=About PraktiCalc", "--msgbox", infotext]),
                    "zenity": lambda: subprocess.Popen(["zenity", "--title=About PraktiCalc", "--info", "--icon=" + PraktiCalcIconPath, "--text=" + infotext]),
                    "AppleScript": lambda: subprocess.run(["osascript", "-e", f'display dialog "{infotext}" with icon POSIX file "{PraktiCalcIconPath}"']),
                    "Xdialog": lambda: subprocess.Popen(["Xdialog", "--title=About PraktiCalc", "--msgbox", infotext, "10", "40"]),
                    "notify-send": lambda: subprocess.Popen(["notify-send", "About PraktiCalc", infotext]),
                    }
                opendialog = styles.get(self.ConfigurationStorage.get("dialogStyle"))
                if opendialog:
                    opendialog()
                else:
                    print("ERROR: Unknown Message Box Style")
    def error(self, message, parent, helper): # shows error dialogs
        if self.ConfigurationStorage.get("dialogStyle") == "Tkinter":
            messagebox.showerror("Error", message)
        elif self.ConfigurationStorage.get("dialogStyle") == "Alternative":
            ErrorWindow = tk.Toplevel(parent)
            ErrorWindow.title("Error")
            ErrorWindow.bind("<Return>", lambda event: helper.close(ErrorWindow))
            ErrorWindow.rowconfigure(0, weight=1)
            ErrorWindow.columnconfigure(0, weight=1)
            if platform.system() == "Windows":
                ErrorWindow.attributes("-toolwindow", True)
                ErrorWindow.focus_force()
            ErrorWindowFrame = ttk.Frame(ErrorWindow)
            ErrorWindowFrame.rowconfigure(0, weight=1)
            ErrorWindowFrame.columnconfigure(0, weight=1)
            ErrorExitButton = ttk.Button(ErrorWindowFrame, text="OK", command=lambda: helper.close(ErrorWindow))
            ExtendedErrorFrame = ttk.LabelFrame(ErrorWindowFrame, relief="sunken", text="[X]")
            ExtendedErrorFrame.rowconfigure(0, weight=1)
            ExtendedErrorFrame.columnconfigure(0, weight=1)
            ErrorTextLabel = ttk.Label(ExtendedErrorFrame, text=message)
            ErrorWindowFrame.grid(row=0, column=0, sticky="nesw")
            ErrorExitButton.grid(row=1, column=1, padx=10, pady=10)
            ExtendedErrorFrame.grid(row=0, column=0, padx=20, pady=10, sticky="nesw")
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
                    "xmessage": lambda: subprocess.Popen(["xmessage", "-title", "Error", "[X] " + message]),
                    "gxmessage": lambda: subprocess.Popen(["gxmessage", "-title", "Error", "[X] " + message]),
                    "yad": lambda: subprocess.Popen(["yad", "--title=Error", "--error", "--image=dialog-error", "--button=OK", "--no-markup", "--text", message]),
                    "kdialog": lambda: subprocess.Popen(["kdialog", "--title=Error", "--error", message]),
                    "zenity": lambda: subprocess.Popen(["zenity", "--title=Error", "--error", "--no-markup", "--text", message]),
                    "AppleScript": lambda: subprocess.run(["osascript", "-e", f'display dialog "{message}" with icon stop']),
                    "Xdialog": lambda: subprocess.Popen(["Xdialog", "--title=Error", "--msgbox", message, "10", "40"]),
                    "notify-send": lambda: subprocess.Popen(["notify-send", "Error", message]),
                    }
                opendialog = styles.get(self.ConfigurationStorage.get("dialogStyle"))
                if opendialog:
                    opendialog()
                else:
                    print("ERROR: Unknown Message Box Style")

# unused help GUI
class HelpWindow(tk.Toplevel):
    def __init__(self, parent, helper):
        super().__init__(parent)
        self = tk.Toplevel(parent)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.title("PraktiCalc Help")
        if platform.system() == "Windows":
            self.focus_force()
        HelpFrame = ttk.Frame(self)
        HelpFrame.rowconfigure(0, weight=1)
        HelpFrame.columnconfigure(0, weight=1)
        HelpFrame.grid(row=0, column=0, sticky="nesw")
        HelpTabs = ttk.Notebook(HelpFrame)
        Content1 = tk.Text(HelpTabs)
        if DarkMode == True:
            Content1.config(fg="white", bg="black")
        Content1.pack(fill="both", expand=True)
        HelpTabs.add(Content1, text="Placeholder")
        HelpTabs.grid(row=0, column=0, sticky="nesw")
        Content1.insert(tk.END, "Sorry, this feature has been aborted.\n\n>_<")
        Content1.config(state="disabled")
        self.protocol("WM_DELETE_WINDOW", lambda: helper.close(self))
        self.update_idletasks()
        helper.WindowList.append(self)
        helper.changeTheme(self)

# history window
class HistoryWindow(tk.Toplevel):
    def __init__(self, parent, calculator, helper):
        super().__init__(parent)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.title("History")
        # self.config(height=400, width=256)
        if platform.system() == "Windows":
            self.attributes("-toolwindow", True)
            self.focus_force()
        HistoryWindowFrame = ttk.Frame(self)
        HistoryWindowFrame.columnconfigure(0, weight=1)
        HistoryWindowFrame.rowconfigure(0, weight=1)
        HistoryWindowFrame.grid(row=0, column=0, sticky="nesw")
        self.HistoryTreeview = ttk.Treeview(HistoryWindowFrame, height=15)
        self.HistoryTreeview.heading("#0", text="History")
        for entry in calculator.HistoryList:
            self.HistoryTreeview.insert("", tk.END, text=entry)
        HistoryClearButton = ttk.Button(HistoryWindowFrame, text="Clear history", command=lambda: self.clear(calculator))
        self.HistoryTreeview.grid(row=0, column=0, sticky="nesw")
        HistoryClearButton.grid(row=1, column=0, sticky="nesw", padx=5, pady=5)
        self.protocol("WM_DELETE_WINDOW", lambda: helper.close(self))
        self.update_idletasks()
        helper.WindowList.append(self)
        helper.changeTheme(self)
    def clear(self, calculator):
        calculator.clearHistory()
        self.HistoryTreeview.delete(*self.HistoryTreeview.get_children())

# extension window
class ExtensionWindow(tk.Toplevel):
    def __init__(self, parent, helper, calculator, dialog):
        super().__init__(parent)
        self.title("Extensions")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        if platform.system() == "Windows":
            self.FolderPath = Path.home() / "AppData" / "Roaming" / "PraktiXtensions"
        elif platform.system() == "Darwin":
            self.FolderPath = Path.home() / "Library" / "PraktiXtensions"
        else:
            self.FolderPath = Path.home() / ".config" / "PraktiXtensions"
        self.Tabs = ttk.Notebook(self)
        self.Tabs.grid(row=0, column=0, sticky="news")
        self.protocol("WM_DELETE_WINDOW", lambda: helper.close(self))
        self.update_idletasks()
        helper.WindowList.append(self)
        helper.changeTheme(self)
        self.after(250, lambda: self.loadExtensions(parent, helper, calculator, dialog))
    def loadExtensions(self, parent, helper, calculator, dialog):
        global DarkMode
        if not self.FolderPath.exists():
            self.FolderPath.mkdir(parents=True)
            self.updateDecimalConverter()
            self.updateExtensionManager()
            self.updatePraktiGraph()
        if Path(self.FolderPath / "DecimalConverter.ini").exists():
            DecimalConverterMeta = configparser.ConfigParser()
            DecimalConverterMeta.read(self.FolderPath / "DecimalConverter.ini")
            if DecimalConverterMeta["PraktiXtension"]["version"] != "1.2":
                self.updateDecimalConverter()
        if Path(self.FolderPath / "ExtensionManager.ini").exists():
            ExtensionManagerMeta = configparser.ConfigParser()
            ExtensionManagerMeta.read(self.FolderPath / "ExtensionManager.ini")
            if ExtensionManagerMeta["PraktiXtension"]["version"] != "1.9":
                self.updateExtensionManager()
        if Path(self.FolderPath / "PraktiGraph.ini").exists():
            PraktiGraphMeta = configparser.ConfigParser()
            PraktiGraphMeta.read(self.FolderPath / "PraktiGraph.ini")
            if PraktiGraphMeta["PraktiXtension"]["version"] != "1.3":
                self.updatePraktiGraph()
        for file in self.FolderPath.iterdir():
            if file.suffix == ".py":
                if Path(self.FolderPath / f"{file.stem}.ini").exists():
                    meta = configparser.ConfigParser()
                    meta.read(Path(self.FolderPath / f"{file.stem}.ini"))
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
                        instance = classs(self.Tabs, self, parent, helper, calculator, dialog, DarkMode)
                        self.Tabs.add(instance, text=meta["PraktiXtension"]["name"])
                        print("loaded extension " + meta["PraktiXtension"]["name"])
                    else:
                        dialog.error("Incompatible Python version", parent, helper)
                else:
                    spec = importlib.util.spec_from_file_location(file.stem, file)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    classs = getattr(module, file.stem)
                    instance = classs(self.Tabs, self, parent, helper, calculator, dialog, DarkMode)
                    self.Tabs.add(instance, text=file.stem)
                    print("loaded extension " + file.stem)
    def updateDecimalConverter(self):
        if Path(self.FolderPath / "DecimalConverter.py").exists():
            Path(self.FolderPath / "DecimalConverter.py").unlink()
            Path(self.FolderPath / "DecimalConverter.ini").unlink(missing_ok=True)
            Path(self.FolderPath / "DecimalConverter.txt").unlink(missing_ok=True)
        if not Path(self.FolderPath / "DecimalConverter.py").exists():
            DecimalConverterCode = """import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import platform

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
        binFrame.rowconfigure(0, weight=1)
        binFrame.columnconfigure(0, weight=1)
        hexFrame.rowconfigure(0, weight=1)
        hexFrame.columnconfigure(0, weight=1)
        self.BinaryLabel = ttk.Label(binFrame, text="")
        self.HexLabel = ttk.Label(hexFrame, text="")
        BinCopyButton = ttk.Button(binFrame, text="Copy", command=lambda: self.copybin(mainWin))
        HexCopyButton = ttk.Button(hexFrame, text="Copy", command=lambda: self.copyhex(mainWin))
        DecimalFrame.grid(row=0, column=0, columnspan=2, sticky="nesw", padx=5)
        self.DecimalInput.grid(row=0, column=0, pady=5, padx=5, sticky="nesw")
        InsertButton.grid(row=0, column=1, padx=5, pady=5)
        binFrame.grid(row=1, column=0, sticky="nesw", padx=5, pady=(0, 5))
        hexFrame.grid(row=1, column=1, sticky="nesw", padx=5, pady=(0, 5))
        self.BinaryLabel.grid(row=0, column=0)
        self.HexLabel.grid(row=0, column=0)
        BinCopyButton.grid(row=1, column=0, pady=(0, 5))
        HexCopyButton.grid(row=1, column=0, pady=(0, 5))
        if platform.system() != "Windows":
            self.DecimalInput.focus_set()
    def convert(self, parent, helper, dialog): # converts decimal numbers into binary and hexadecimal
        cp = str(self.DecimalInput.get())
        try:
            DecimalNumber = int(cp)
            BinaryNumber = bin(DecimalNumber)[2:]
            HexadecimalNumber = hex(DecimalNumber)
            self.BinaryLabel.config(text=str(BinaryNumber))
            self.HexLabel.config(text=str(HexadecimalNumber))
        except:
            dialog.error("Please enter a real number!", parent, helper)
    def copybin(self, mainWin): # copies the binary output
        mainWin.clipboard_clear()
        mainWin.clipboard_append(self.BinaryLabel.cget("text"))
        mainWin.update()
    def copyhex(self, mainWin): # copies the hexadecimal output
        mainWin.clipboard_clear()
        mainWin.clipboard_append(self.HexLabel.cget("text"))
        mainWin.update()"""
            DecimalConverterMetadata = configparser.ConfigParser()
            DecimalConverterMetadata["PraktiXtension"] = {"name": "Decimal Converter",
                                                          "version": "1.2",
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
    def updateExtensionManager(self):
        if Path(self.FolderPath / "ExtensionManager.py").exists():
            Path(self.FolderPath / "ExtensionManager.py").unlink()
            Path(self.FolderPath / "ExtensionManager.ini").unlink(missing_ok=True)
            Path(self.FolderPath / "ExtensionManager.txt").unlink(missing_ok=True)
        if not Path(self.FolderPath / "ExtensionManager.py").exists():
            ExtensionManagerCode = """# PraktiCalc Extension Manager
# Copyright (C) 2026 Karl "karl152"
# SPDX-License-Identifier: GPL-3.0

import tkinter as tk
from tkinter import ttk, font, messagebox, filedialog
from pathlib import Path
import webbrowser, configparser, zipfile, tempfile, hashlib, shutil

class ExtensionManager(ttk.Frame):
    def __init__(self, tabs, parent, mainWin, helper, calculator, dialog, DarkMode):
        super().__init__(tabs)
        self.style = ttk.Style()
        self.style.configure("ExtensionTitle.TLabel", font=font.Font(family="TkDefaultFont", size=15))
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        ttk.Label(self, text="The Extension Manager allows you to easily manage your installed extensions and even install new ones in the PraktiXtension (.pxt) format.").grid(row=0, column=0, sticky="w")
        self.Splitter = ttk.PanedWindow(self, orient="horizontal")
        self.LeftFrame = ttk.Frame(self.Splitter)
        self.RightFrame = ttk.LabelFrame(self.Splitter, text="Metadata")
        self.ExtensionTree = ttk.Treeview(self.LeftFrame, selectmode="browse")
        self.ExtensionTree.bind("<<TreeviewSelect>>", lambda event: self.updateMetadataDisplay(parent))
        self.ExtensionTree.heading("#0", text="Extensions")
        for file in parent.FolderPath.iterdir():
            if file.suffix == ".py":
                self.ExtensionTree.insert("", tk.END, text=file.stem)
        ttk.Label(self.RightFrame).grid(row=0, column=0)
        self.ExtensionTree.grid(row=0, column=0, columnspan=2, sticky="news")
        self.AddButton = ttk.Button(self.LeftFrame, text="Add", command=lambda: self.addExtension(parent, helper, dialog))
        self.AddButton.grid(row=1, column=0, padx=10, pady=10, sticky="we")
        self.RemoveButton = ttk.Button(self.LeftFrame, text="Remove", state="disabled", command=lambda: self.removeExtension(parent))
        self.RemoveButton.grid(row=1, column=1, padx=10, pady=10, sticky="we")
        self.ResetButton = ttk.Button(self.LeftFrame, text="Reset Extension Folder", command=lambda: self.reset(parent, mainWin, helper))
        self.ResetButton.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="we")
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
        self.TitleLabel.grid(row=0, column=0, columnspan=2, sticky="new")
        self.DescriptionLabel.grid(row=1, column=0, columnspan=2, sticky="ew")
        ttk.Separator(self.RightFrame, orient="horizontal").grid(row=3, column=0, columnspan=2, sticky="ew")
        Labels = ["Version", "File name", "License", "Website", "Minimal Python version", "Maximal Python version", "SHA256 checksum"]
        Entrys = [self.VersionDisplay, self.FileNameDisplay, self.LicenseDisplay, self.WebLinkDisplay, self.minPyVerDisplay, self.maxPyVerDisplay, self.ChecksumDisplay]
        for i in range(7):
            ttk.Label(self.RightFrame, text=Labels[i]).grid(row=i+4, column=0, sticky="ew", padx=10)
            Entrys[i].grid(row=i+4, column=1, sticky="we", padx=10, pady=5)
        self.DescriptionFrame = ttk.LabelFrame(self.RightFrame, text="Description")
        self.DescriptionFrame.rowconfigure(0, weight=1)
        self.DescriptionFrame.columnconfigure(0, weight=1)
        self.DescriptionFrame.grid(row=11, column=0, columnspan=2, sticky="news", padx=5, pady=5)
        self.DescriptionText = ttk.Label(self.DescriptionFrame, text="")
        self.DescriptionText.grid(row=0, column=0, sticky="news", padx=5, pady=5)
        self.LeftFrame.rowconfigure(0, weight=1)
        self.RightFrame.columnconfigure(1, weight=1)
        self.RightFrame.rowconfigure(11, weight=1)
        self.Splitter.add(self.LeftFrame)
        self.Splitter.add(self.RightFrame)
        self.Splitter.grid(row=1, column=0, sticky="news")
    def updateMetadataDisplay(self, parent):
        self.RemoveButton.config(state="normal")
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
                    self.WebsiteButton.grid(row=2, column=1, sticky="e", padx=5, pady=5)
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
                    self.InternetLabel.grid(row=2, column=0, sticky="ew")
                except:
                    pass
            else:
                try:
                    self.InternetLabel.grid_remove()
                except:
                    pass
            for display in displays:
                display.config(state="normal")
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
            for label in labels:
                label.config(text="")
            for display in displays:
                display.config(state="normal")
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
                self.RemoveButton.config(state="disabled")
        if Path(parent.FolderPath / f"{ext}.txt").exists():
            with open(Path(parent.FolderPath / f"{ext}.txt"), "r", encoding="utf-8") as txt:
                self.DescriptionText.config(text=txt.read())
        else:
            self.DescriptionText.config(text="")
    def removeExtension(self, parent):
        ext = self.ExtensionTree.item(self.ExtensionTree.selection(), "text")
        Path(parent.FolderPath / f"{ext}.py").unlink()
        Path(parent.FolderPath / f"{ext}.ini").unlink(missing_ok=True)
        Path(parent.FolderPath / f"{ext}.txt").unlink(missing_ok=True)
        self.ExtensionTree.delete(self.ExtensionTree.selection()[0])
    def addExtension(self, parent, helper, dialog):
        file = filedialog.askopenfilename(parent=parent, filetypes=[("PraktiXtension", "*.pxt")])
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
                    shutil.move(Path(tempdir) / "info.ini", parent.FolderPath / f"{ExtensionName[:-3]}.ini")
                    shutil.move(Path(tempdir) / "description.txt", parent.FolderPath / f"{ExtensionName[:-3]}.txt")
                    shutil.move(Path(tempdir) / ExtensionName, parent.FolderPath / ExtensionName)
                    self.ExtensionTree.insert("", tk.END, text=ExtensionName[:-3])
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
    def reset(self, parent, mainWin, helper):
        shutil.rmtree(parent.FolderPath)
        helper.close(parent)"""
            ExtensionManagerMetadata = configparser.ConfigParser()
            ExtensionManagerMetadata["PraktiXtension"] = {"name": "Extension Manager",
                                                          "version": "1.9",
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
    def updatePraktiGraph(self):
        if Path(self.FolderPath / "PraktiGraph.py").exists():
            Path(self.FolderPath / "PraktiGraph.py").unlink()
            Path(self.FolderPath / "PraktiGraph.ini").unlink(missing_ok=True)
            Path(self.FolderPath / "PraktiGraph.txt").unlink(missing_ok=True)
        if not Path(self.FolderPath / "PraktiGraph.py").exists():
            PraktiGraphCode = """import tkinter as tk
from tkinter import ttk, messagebox, colorchooser

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
        self.Scale = tk.IntVar(value=100)
        self.ClearStatus = True
        self.TextOffset = 15
        self.Numbers = tk.BooleanVar(value=True)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.Canvas = tk.Canvas(self, background=self.BackgroundColor)
        self.Canvas.grid(row=0, column=0, columnspan=4, sticky="news")
        ttk.Separator(self, orient="horizontal").grid(row=1, column=0, columnspan=4, sticky="ew")
        ttk.Label(self, text="f(x) = ").grid(row=2, column=0, sticky="e")
        ttk.Label(self, text="g(x) = ").grid(row=3, column=0, sticky="e")
        self.fxEntry = ttk.Entry(self)
        self.gxEntry = ttk.Entry(self)
        self.fxEntry.grid(row=2, column=1, columnspan=2, sticky="ew")
        self.gxEntry.grid(row=3, column=1, columnspan=2, sticky="ew")
        self.fxColorButton = tk.Button(self, text="color", fg=self.fxColor, bg=self.fxColor, command=lambda: self.setFxColor(parent, calculator))
        self.gxColorButton = tk.Button(self, text="color", fg=self.gxColor, bg=self.gxColor, command=lambda: self.setGxColor(parent, calculator))
        self.fxColorButton.grid(row=2, column=3, padx=10)
        self.gxColorButton.grid(row=3, column=3, padx=10)
        self.cols = ("-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5")
        self.Table = ttk.Treeview(self, columns=self.cols, height=2)
        self.Table.heading("#0", text="x")
        for col in self.cols:
            self.Table.heading(col, text=col)
        self.FirstTableRow = self.Table.insert("", tk.END, text="f(x)")
        self.SecondTableRow = self.Table.insert("", tk.END, text="g(x)")
        self.Table.grid(row=4, column=0, columnspan=4, sticky="news")
        ttk.Button(self, text="Clear", command=self.clear).grid(row=5, column=1, pady=10, padx=20, sticky="e")
        ttk.Button(self, text="Draw", command=lambda: self.redraw(calculator)).grid(row=5, column=2, pady=10, padx=20, sticky="w")
        ttk.Checkbutton(self, text="Draw numbers", variable=self.Numbers, command=lambda: self.redraw(calculator) if self.ClearStatus == False else self.doNothing()).grid(row=5, column=0, padx=(10, 0), sticky="w")
        self.ScaleSlider = ttk.Scale(self, from_=50, to=500, orient="horizontal", variable=self.Scale, command=lambda _: self.redraw(calculator) if self.ClearStatus == False else self.doNothing())
        self.ScaleSlider.grid(row=5, column=3, padx=(0, 10), sticky="e")
        self.bind("<Configure>", lambda event: self.after(200, lambda: self.redraw(calculator)) if self.ClearStatus == False else self.clear())
    def redraw(self, calculator):
        self.clear()
        self.ClearStatus = False
        height = self.Canvas.winfo_height()
        width = self.Canvas.winfo_width()
        self.Canvas.create_line(0, height/2, width, height/2, fill="grey", width=2)
        self.Canvas.create_line(width/2, 0, width/2, height, fill="grey", width=2)
        for i in range(100):
            self.Canvas.create_line(width/2+i*self.Scale.get(), 0, width/2+i*self.Scale.get(), height, fill="grey")
            self.Canvas.create_text(width/2+i*self.Scale.get(), height/2+self.TextOffset, text=str(i), fill=self.ForegroundColor) if i != 0 and self.Numbers.get() == True else self.doNothing()
            self.Canvas.create_line(width/2-i*self.Scale.get(), 0, width/2-i*self.Scale.get(), height, fill="grey")
            self.Canvas.create_text(width/2-i*self.Scale.get(), height/2+self.TextOffset, text=f"-{i}", fill=self.ForegroundColor) if i != 0 and self.Numbers.get() == True else self.doNothing()
            self.Canvas.create_line(0, height/2+i*self.Scale.get(), width, height/2+i*self.Scale.get(), fill="grey")
            self.Canvas.create_text(width/2+self.TextOffset, height/2+i*self.Scale.get(), text=f"-{i}", fill=self.ForegroundColor) if i != 0 and self.Numbers.get() == True else self.doNothing()
            self.Canvas.create_line(0, height/2-i*self.Scale.get(), width, height/2-i*self.Scale.get(), fill="grey")
            self.Canvas.create_text(width/2+self.TextOffset, height/2-i*self.Scale.get(), text=str(i), fill=self.ForegroundColor) if i != 0 and self.Numbers.get() == True else self.doNothing()
        if self.fxEntry.get() != "":
            values = []
            for col in self.cols:
                try:
                    values.append(calculator.quickCalc(self.fxEntry.get().replace("x", f"({col})")))
                except:
                    values.append("")
            self.Table.item(self.FirstTableRow, values=values)
            values = []
            for i in range(-1000, 1000):
                realI = i*0.1 # because range doesn't support floats
                try:
                    values.append((realI, calculator.quickCalc(self.fxEntry.get().replace("x", f"({realI})"))))
                except:
                    pass
            for f in range(len(values)-1):
                self.Canvas.create_line(self.XtoX(values[f][0]), self.YtoY(values[f][1]), self.XtoX(values[f+1][0]), self.YtoY(values[f+1][1]), fill=self.fxColor)
        if self.gxEntry.get() != "":
            values = []
            for col in self.cols:
                try:
                    values.append(calculator.quickCalc(self.gxEntry.get().replace("x", f"({col})")))
                except:
                    values.append("")
            self.Table.item(self.SecondTableRow, values=values)
            values = []
            for i in range(-1000, 1000):
                realI = i*0.1 # because range doesn't support floats
                try:
                    values.append((realI, calculator.quickCalc(self.gxEntry.get().replace("x", f"({realI})"))))
                except:
                    pass
            for f in range(len(values)-1):
                self.Canvas.create_line(self.XtoX(values[f][0]), self.YtoY(values[f][1]), self.XtoX(values[f+1][0]), self.YtoY(values[f+1][1]), fill=self.gxColor)

    def clear(self):
        self.Canvas.delete("all")
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
        return float(self.Canvas.winfo_height())/2.0-float(y) * self.Scale.get()
    def XtoX(self, x):
        return float(self.Canvas.winfo_width())/2.0+float(x) * self.Scale.get()
    def doNothing(self):
        pass"""
            PraktiGraphMetadata = configparser.ConfigParser()
            PraktiGraphMetadata["PraktiXtension"] = {"name": "PraktiGraph",
                                                          "version": "1.3",
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
        else:
            output = "[X] Unknown command"
        return output

# console window
class ConsoleWindow(tk.Toplevel):
    def __init__(self, parent, helper, console):
        super().__init__(parent)
        self.lcc = ""
        self.title("PraktiCalc Console")
        self.config(bg="black")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.bind("<Key>", lambda event: self.run(parent, helper, console) if event.keysym == "Return" else self.ConsoleKey(event))
        self.ConsoleOutput = scrolledtext.ScrolledText(self, bg="black", fg="white")
        self.ConsoleOutput.vbar.config(bg="black")
        ConsoleInputLabel = tk.Label(self, text="INPUT: ", bg="black", fg="white")
        self.ConsoleInput = tk.Entry(self, bg="black", fg="white")
        ConsoleExecuteButton = tk.Button(self, text="--^", bg="black", fg="white", command=lambda: self.run(parent, helper, console))
        self.ConsoleOutput.grid(row=0, column=0, columnspan=3, sticky="nesw")
        ConsoleInputLabel.grid(row=1, column=0, sticky="ew")
        self.ConsoleInput.grid(row=1, column=1, sticky="ew")
        ConsoleExecuteButton.grid(row=1, column=2, sticky="ew", pady=2, padx=2)
        self.ConsoleInput.focus_set()
        self.protocol("WM_DELETE_WINDOW", lambda: helper.close(self))
        self.update_idletasks()
        helper.WindowList.append(self)
        helper.ajustTitleBars()
    def run(self, parent, helper, console):
        self.lcc = command = self.ConsoleInput.get()
        if command == "clear":
            self.ConsoleOutput.delete("1.0", tk.END)
        elif command == "aboutwindow":
            self.AboutWindow(parent, helper)
        elif command == "exit":
            helper.close(parent)
            return
        else:
            comoutput = console.execute(self.ConsoleInput.get())
            self.ConsoleOutput.insert(tk.END, str(comoutput) + "\n")
            self.ConsoleOutput.see("end")
        self.ConsoleInput.delete(0, tk.END)
    def ConsoleKey(self, event):
        key = event.keysym
        if key == "Up":
            self.ConsoleInput.delete(0, tk.END)
            self.ConsoleInput.insert(0, self.lcc)
    def AboutWindow(self, parent, helper): # shows console about window
        ConsoleAboutWindow = tk.Toplevel(parent)
        if platform.system() == "Windows":
            ConsoleAboutWindow.attributes("-toolwindow", True)
            ConsoleAboutWindow.focus_force()
        ConsoleAboutWindow.columnconfigure(0, weight=1)
        for cw in range(4):
            ConsoleAboutWindow.rowconfigure(cw, weight=1)
        ConsoleAboutWindow.title("About PraktiCalc Console")
        ConsoleAboutWindow.config(bg="black")
        ConsoleAboutSpacer1 = tk.Label(ConsoleAboutWindow, bg="black")
        ConsoleAboutSpacer2 = tk.Label(ConsoleAboutWindow, bg="black")
        ConsoleAboutIcon = tk.Label(ConsoleAboutWindow, image=parent.icon_mono_inverted, fg="black", bg="white")
        ConsoleAboutText = tk.Label(ConsoleAboutWindow, bg="black", text="PraktiCalc Console\nrunning on PraktiCalc " + PraktiCalcVersion + "\npowered by Python " + platform.python_version(), fg="white")
        ConsoleAboutSpacer1.grid(row=0, column=0, sticky="nesw")
        ConsoleAboutIcon.grid(row=0, column=0, padx=152, pady=20)
        ConsoleAboutText.grid(row=2, column=0, sticky="nesw")
        ConsoleAboutSpacer2.grid(row=3, column=0, sticky="nesw")
        ConsoleAboutWindow.protocol("WM_DELETE_WINDOW", lambda: helper.close(ConsoleAboutWindow))
        ConsoleAboutWindow.update_idletasks()
        helper.WindowList.append(ConsoleAboutWindow)
        helper.ajustTitleBars()

if __name__ == "__main__":
    cfg = Configuration()
    Calculator = PraktiCalculator(cfg)
    WindowHelp = WindowHelper(cfg)
    WindowDialog = Dialog(cfg)
    Window = MainWindow(WindowHelp, Calculator, WindowDialog, cfg)
    if "--console" in sys.argv:
        cmd = Console(cfg)
        CMDWindow = ConsoleWindow(Window, WindowHelp, cmd)
    Window.mainloop()
