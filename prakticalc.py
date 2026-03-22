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
from tkinter import ttk, messagebox, font, scrolledtext
from pathlib import Path
try:
    from ttkthemes import ThemedStyle
    theming = 1
except:
    theming = 0
# 0 = no theming
# 1 = theming from ttkthemes
# 2 = manual theming
import platform
import subprocess
import sys
import shutil
import math
import getpass # for getting the username
import time
if platform.system() == "Windows":
    import winreg
    from ctypes import wintypes
elif platform.system() == "Darwin":
    import plistlib
else:
    import configparser

# VARIABLES
CLIHelp = "--help" in sys.argv
CLIVersion = "--version" in sys.argv
PraktiCalcVersion = "1.5"
BypassWindowsDPIFix = "--nodpiawareness" in sys.argv
allowWindowsShutdownDialog = "--allowShutdownDialog" in sys.argv
WindowList = ["MainWindow", "SettingsWindow", "HistoryX", "MoreWindow", "CustomInfox", "ErrorWindow", "ConsoleWindow", "ConsoleAboutWindow", "HelpWindow"]
UseNativeTheme = False
MsgBoxStyles = ["Tkinter", "Alternative"]
if platform.system() == "Windows":
    import ctypes
    UseNativeTheme = True
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
    UseNativeTheme = True
    if theming != 0:
        NativeTheme = "aqua"
    WingWebDings = False
    MsgBoxStyles.append("AppleScript")
else:
    WingWebDings = False
    if theming != 0:
        NativeTheme = "default"
    AdditionalLinuxMsgBoxStyles = ["xmessage", "yad", "kdialog", "zenity", "Xdialog"]
    for MsgBoxStyle in AdditionalLinuxMsgBoxStyles:
        if shutil.which(MsgBoxStyle):
            MsgBoxStyles.append(MsgBoxStyle)
CurrentMsgBoxStyle = "Alternative"
ThemingDisabled = "--notheming" in sys.argv
if ThemingDisabled == True:
    theming = 0
if CLIHelp == True:
    if platform.system() == "Windows":
        messagebox.showinfo("PraktiCalc CLI Options", "PraktiCalc " + PraktiCalcVersion + """ CLI Options:
--allowShutdownDialog: allow the use of the shutdown command to display messages
--big: start with bigger main window
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
        if platform.system() != "Darwin":
            print("--big           | start with bigger main window")
        print("--borderdisplay | uses window title to show output")
        print("--debug         | add a test button for debugging")
        if platform.system() != "Darwin":
            if theming != 0:
                print("--dark          | enable dark mode by default")
        print("--console       | show console for debugging")
        if theming != 0:
            print("--notheming     | disables theming")
            print("--breeze        | set the light theme to breeze")
            print("--yaru          | set the light theme to yaru")
            print("--keramik       | set the light theme to keramik")
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
    VBSInfoPath = (sys._MEIPASS + "/info.vbs")
    VBSErrorPath = (sys._MEIPASS + "/error.vbs")
else:
    if platform.system() == "Darwin":
        PraktiCalcMacIconPath = "PraktiCalc-MacOS.png"
    PraktiCalcIconPath = "PraktiCalculator_icon.png"
    PraktiCalcIconMonoPath = "PraktiCalculator_icon.xbm"
    PraktiCalcIconMonoInvertedPath = "PraktiCalculator_icon_inverted.xbm"
    VBSInfoPath = "info.vbs"
    VBSErrorPath = "error.vbs"

breeze = "--breeze" in sys.argv
yaru = "--yaru" in sys.argv
keramik = "--keramik" in sys.argv
equilux = "--equilux" in sys.argv
if platform.system() != "Darwin":
    big = "--big" in sys.argv
else:
    big = False
if breeze == True:
    thettktheme = "breeze"
elif yaru == True:
    thettktheme = "yaru"
elif keramik == True:
    thettktheme = "keramik"
else:
    thettktheme = "plastik"
if equilux == True:
    thettktheme = "equilux"
if ThemingDisabled == False:
    DarkMode = "--dark" in sys.argv
    if DarkMode == True:
        thettktheme = "black"
        UseNativeTheme = False
else:
    DarkMode = False
if breeze == True or yaru == True or keramik == True or equilux == True:
    UseNativeTheme = False
BorderDisplay = "--borderdisplay" in sys.argv
debug = "--debug" in sys.argv

# CLASSES
class Configuration:
    def __init__(self):
        # Configuration TODO:
        # - make it possible to delete values
        # - does overwriting work?
        if platform.system() == "Windows":
            self.backend = WindowsConfig()
        elif platform.system() == "Darwin":
            self.backend = MacConfig()
        else:
            self.backend = XDGConfig()
    def get(self, key):
        return self.backend.get(key)
    def set(self, key, value):
        self.backend.set(key, value)
    def create(self):
        self.backend.create()
    def reset(self):
        self.backend.reset()
        MainWindow.destroy()
        sys.exit(0)

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

class XDGConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.folder = Path.home() / ".config" / "PraktiCalc"
        self.path = self.folder / "config.ini"
    def get(self, key):
        self.config.read(self.path)
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
        with open(self.path, "w") as configfile:
            self.config.write(configfile)
    def create(self):
        self.folder.mkdir(parents=True)
        self.config["General"] = {}
        with open(self.path, "w") as configfile:
            self.config.write(configfile)
    def reset(self):
        shutil.rmtree(self.folder)

# Calculation Unit
class PraktiCalculator:
    def __init__(self):
        self.CalculationString = "0"
        self.Memory = "0"
        self.HistoryList = []
        self.LastResult = "0"
        self.operators = {}
        self.operators["sqrt"] = math.sqrt
        self.operators["sin"] = lambda x: math.sin(math.radians(x))
        self.operators["cos"] = lambda x: math.cos(math.radians(x))
        self.operators["tan"] = lambda x: math.tan(math.radians(x))
        self.operators["ld"] = math.log2
        self.operators["ln"] = math.log
        self.operators["lg"] = math.log10
        self.operators["pi"] = math.pi
    def calculate(self): # does the actual calculation, used to include 171 if-statements
        TheCalc = self.CalculationString.replace("\u221a", "sqrt")
        TheCalc = TheCalc.replace("\u03c0", "pi")
        TheCalc = TheCalc.replace("x", "*")
        TheCalc = TheCalc.replace("^", "**")
        if "__" in TheCalc:
            raise ValueError
        try:
            Result = eval(TheCalc, {"__builtins__": None}, self.operators)
        except Exception as e:
            raise e
        Result = str(round(float(Result), 12))
        if str(Result).endswith(".0"):
            Result = str(Result)[:-2]
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
        char = char.replace("asterisk", "x")
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
        self.Memory = self.LastResult
    def getMemory(self): # adds the memory value to the calculation string
        if self.CalculationString == "0":
            self.CalculationString = self.Memory
        else:
            self.CalculationString += self.Memory
    def clearHistory(self): # clears the history list
        self.HistoryList.clear()
    def xcheck(self): # debug function to return some variables
        return self.CalculationString, self.Memory, self.LastResult, self.HistoryList, self.operators
    def quickCalc(self, expression):
        self.clear()
        self.append(expression)
        result = self.calculate()
        return result

# provides settings, theming and ajustments for windows
class WindowHelper:
    def changeTheme(self, WindowName): # sets the theme for a given window
        global theming
        if platform.system() == "Darwin":
            if UseNativeTheme == False:
                self.style = ThemedStyle(WindowName)
                self.style.theme_use(thettktheme)
            else:
                self.style = ttk.Style(WindowName)
                self.style.theme_use(NativeTheme)
        elif platform.system() == "Windows":
            ajustTitleBars()
            if UseNativeTheme == False:
                self.style = ThemedStyle(WindowName)
                self.style.theme_use(thettktheme)
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
                if UseNativeTheme == False:
                    self.style = ThemedStyle(WindowName)
                    self.style.theme_use(thettktheme)
                else:
                    self.style = ttk.Style(WindowName)
                    self.style.theme_use(NativeTheme)
                    self.style.configure("LargeUnicode.TButton", font=LargeUnicodeFont)
                    self.style.configure("Treeview", rowheight=40)
            except:
                theming = 2
                if UseNativeTheme == True:
                    self.style = ttk.Style(WindowName)
                    self.style.theme_use(NativeTheme)
                else:
                    theme_base = Path(sys._MEIPASS).joinpath("ttkthemes", "themes")
                    theme_path = Path(theme_base).joinpath(thettktheme)
                    WindowName.tk.call("lappend", "auto_path", theme_base)
                    try:
                        WindowName.tk.call("package", "require", f"ttk::theme::{thettktheme}")
                    except:
                        theme_tcl = Path(theme_path).joinpath(thettktheme + ".tcl")
                        if Path(theme_tcl).exists():
                            WindowName.tk.call("source", theme_tcl)
                        else:
                            print(f"Couldn't find theme {theme_tcl}")
                    self.style = ttk.Style()
                    try:
                        self.style.theme_use(thettktheme)
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
        for window in WindowList:
            try:
                exec(f"{window}.update_idletasks()")
                exec(f"self.ajustTitleBar(ctypes.windll.user32.GetParent({window}.winfo_id()))")
            except:
                pass

# main window
class MainWindow(tk.Tk):
    def __init__(self, helper, calculator):
        global wingdingsfont, webdingsfont, LargeUnicodeFont
        super().__init__()
        self.title("PraktiCalc")
        self.icon_mono = tk.BitmapImage(file=PraktiCalcIconMonoPath)
        self.icon = tk.PhotoImage(file=PraktiCalcIconPath)
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
        self.UseNativeThemeTkVar = tk.BooleanVar(value=UseNativeTheme)
        self.BorderDisplayTkVar = tk.BooleanVar(value=BorderDisplay)
        self.CurrentMsgBoxStyleTkVar = tk.StringVar(value=CurrentMsgBoxStyle)
        self.config(width=256, height=315)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        helper.changeTheme(self)
        self.WindowFrame = ttk.Frame(self)
        for colrow in range(6):
            self.WindowFrame.rowconfigure(colrow, weight=1, uniform="buttons")
            self.WindowFrame.columnconfigure(colrow, weight=1, uniform="buttons")
        self.WindowFrame.rowconfigure(6, weight=1)
        if BorderDisplay == True:
            self.WindowFrame.rowconfigure(0, weight=0, uniform="")
        self.OutputFrame = ttk.Frame(self.WindowFrame, borderwidth=1, relief="sunken")
        self.Output = ttk.Label(self.OutputFrame, text="0")
        # BUTTONS
        PlusButton = ttk.Button(self.WindowFrame, text="+", command=lambda: self.append("plus", calculator))
        MinusButton = ttk.Button(self.WindowFrame, text="-", command=lambda: self.append("minus", calculator))
        MultiplyButton = ttk.Button(self.WindowFrame, text="x", command=lambda: self.append("asterisk", calculator))
        DivideButton = ttk.Button(self.WindowFrame, text="÷", command=lambda: self.append("slash", calculator))
        SevenButton = ttk.Button(self.WindowFrame, text="7", command=lambda: self.append("7", calculator))
        EightButton = ttk.Button(self.WindowFrame, text="8", command=lambda: self.append("8", calculator))
        NineButton = ttk.Button(self.WindowFrame, text="9", command=lambda: self.append("9", calculator))
        CEButton = ttk.Button(self.WindowFrame, text="CE", command=lambda: self.clear(calculator))
        FourButton = ttk.Button(self.WindowFrame, text="4", command=lambda: self.append("4", calculator))
        FiveButton = ttk.Button(self.WindowFrame, text="5", command=lambda: self.append("5", calculator))
        SixButton = ttk.Button(self.WindowFrame, text="6", command=lambda: self.append("6", calculator))
        CommaButton = ttk.Button(self.WindowFrame, text=",", command=lambda: self.append("comma", calculator))
        OneButton = ttk.Button(self.WindowFrame, text="1", command=lambda: self.append("1", calculator))
        TwoButton = ttk.Button(self.WindowFrame, text="2", command=lambda: self.append("2", calculator))
        ThreeButton = ttk.Button(self.WindowFrame, text="3", command=lambda: self.append("3", calculator))
        EqualButton = ttk.Button(self.WindowFrame, text="=", command=lambda: self.calculate(self, helper, calculator))
        InfoButton = ttk.Button(self.WindowFrame, text="i", command=lambda: Dialog().info(self, helper))
        ZeroButton = ttk.Button(self.WindowFrame, text="0", command=lambda: self.zero(calculator))
        self.ExitButton = ttk.Button(self.WindowFrame, text="X", command=self.destroy)
        LeftParenButton = ttk.Button(self.WindowFrame, text="(", command=lambda: self.append("parenleft", calculator))
        RightParenButton = ttk.Button(self.WindowFrame, text=")", command=lambda: self.append("parenright", calculator))
        if WingWebDings == True:
            SettingsButton = ttk.Button(self.WindowFrame, text="@", command=lambda: SettingsWindow(self, helper, calculator), style="Webdings.TButton")
            self.BackspaceButton = ttk.Button(self.WindowFrame, text="Õ", command=lambda: self.backspace(calculator), style="Wingdings.TButton")
            HistoryButton = ttk.Button(self.WindowFrame, text="0", command=lambda: HistoryWindow(self, calculator, helper), style="Wingdings.TButton")
            self.CopyButton = ttk.Button(self.WindowFrame, text="4", command=self.copyResult, style="Wingdings.TButton")
        else:
            SettingsButton = ttk.Button(self.WindowFrame, text="\u26ed", command=lambda: SettingsWindow(self, helper, calculator), style="LargeUnicode.TButton")
            self.BackspaceButton = ttk.Button(self.WindowFrame, text="\u232b", command=lambda: self.backspace(calculator))
            HistoryButton = ttk.Button(self.WindowFrame, text="\u23f2", command=lambda: HistoryWindow(self, calculator, helper), style="LargeUnicode.TButton")
            self.CopyButton = ttk.Button(self.WindowFrame, text="\u2398", command=self.copyResult, style="LargeUnicode.TButton")
        ModuloButton = ttk.Button(self.WindowFrame, text="%", command=lambda: self.append("%", calculator))
        Checkb = ttk.Button(self, text="Check", command=lambda: print(calculator.xcheck())) # some debug thing
        sqrtButton = ttk.Button(self.WindowFrame, text="\u221a", command=lambda: self.append("\u221a" + "(", calculator))
        More = ttk.Button(self.WindowFrame, text="...", command=lambda: ExtensionWindow(self, helper, calculator))
        PowerButton = ttk.Button(self.WindowFrame, text="x^y", command=lambda: self.append("^", calculator))
        SetMemoryButton = ttk.Button(self.WindowFrame, text="SM", command=calculator.setMemory)
        GetMemoryButton = ttk.Button(self.WindowFrame, text="GM", command=calculator.getMemory)
        SinButton = ttk.Button(self.WindowFrame, text="sin", command=lambda: self.append("sin(", calculator))
        CosButton = ttk.Button(self.WindowFrame, text="cos", command=lambda: self.append("cos(", calculator))
        TanButton = ttk.Button(self.WindowFrame, text="tan", command=lambda: self.append("tan(", calculator))
        LdButton = ttk.Button(self.WindowFrame, text="ld", command=lambda: self.append("ld(", calculator))
        LnButton = ttk.Button(self.WindowFrame, text="ln", command=lambda: self.append("ln(", calculator))
        LgButton = ttk.Button(self.WindowFrame, text="lg", command=lambda: self.append("lg(", calculator))
        self.WindowFrame.grid(row=0, column=0, sticky="nesw")
        if BorderDisplay == False:
            self.OutputFrame.grid(row=0, column=0, columnspan=4, sticky="nesw")
            self.CopyButton.grid(row=0, column=4, sticky="nesw")
            self.BackspaceButton.grid(row=0, column=5, sticky="nesw")
            self.ExitButton.grid(row=6, column=0, sticky="nesw")
        else:
            self.BackspaceButton.grid(row=6, column=0, sticky="nesw")
        self.Output.pack(pady=1)
        PlusButton.grid(row=1, column=5, sticky="nesw")
        MinusButton.grid(row=2, column=5, sticky="nesw")
        MultiplyButton.grid(row=3, column=5, sticky="nesw")
        DivideButton.grid(row=4, column=5, sticky="nesw")
        SevenButton.grid(row=3, column=2, sticky="nesw")
        EightButton.grid(row=3, column=3, sticky="nesw")
        NineButton.grid(row=3, column=4, sticky="nesw")
        CEButton.grid(row=2, column=4, sticky="nesw")
        FourButton.grid(row=4, column=2, sticky="nesw")
        FiveButton.grid(row=4, column=3, sticky="nesw")
        SixButton.grid(row=4, column=4, sticky="nesw")
        CommaButton.grid(row=6, column=4, sticky="nesw")
        OneButton.grid(row=5, column=2, sticky="nesw")
        TwoButton.grid(row=5, column=3, sticky="nesw")
        ThreeButton.grid(row=5, column=4, sticky="nesw")
        EqualButton.grid(row=6, column=5, sticky="nesw")
        InfoButton.grid(row=1, column=0, sticky="nesw")
        ZeroButton.grid(row=6, column=2, columnspan=2, sticky="nesw")
        ModuloButton.grid(row=5, column=0, sticky="nesw")
        sqrtButton.grid(row=5, column=5, sticky="nesw")
        SettingsButton.grid(row=2, column=0, sticky="nesw")
        HistoryButton.grid(row=4, column=0, sticky="nesw")
        LeftParenButton.grid(row=2, column=2, sticky="nesw")
        RightParenButton.grid(row=2, column=3, sticky="nesw")
        PowerButton.grid(row=1, column=4, sticky="nesw")
        SetMemoryButton.grid(row=1, column=2, sticky="nesw")
        GetMemoryButton.grid(row=1, column=3, sticky="nesw")
        SinButton.grid(row=1, column=1, sticky="nesw")
        CosButton.grid(row=2, column=1, sticky="nesw")
        TanButton.grid(row=3, column=1, sticky="nesw")
        LdButton.grid(row=4, column=1, sticky="nesw")
        LnButton.grid(row=5, column=1, sticky="nesw")
        LgButton.grid(row=6, column=1, sticky="nesw")
        self.bind("<Key>", lambda event: self.KeyPress(event, calculator, helper))
        More.grid(row=3, column=0, sticky="nesw")
        if debug == True:
            Checkb.grid(row=1, column=0, sticky="nesw")
        if platform.system() == "Darwin":
            pass
        elif big == False:
            self.geometry("250x250")
        else:
            self.geometry("400x400")
        self.update_idletasks()
        if platform.system() == "Windows":
            hwnd = ctypes.windll.user32.GetParent(self.winfo_id())
            if DarkMode == True:
                helper.ajustTitleBar(hwnd)
    def KeyPress(self, event, calculator, helper): # processes keyboard input
        Key = event.keysym
        if Key in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "plus", "minus", "asterisk", "slash", "comma", "parenleft", "parenright"]:
            self.append(Key, calculator)
        elif Key == "0":
            self.zero(calculator)
        elif Key == "equal" or Key == "Return":
            self.calculate(self, helper, calculator)
        elif Key == "h" or Key == "H":
            HistoryWindow(self, calculator, helper)
        elif Key == "c" or Key == "C":
            self.clear(calculator)
        elif Key == "i":
            Dialog().info(self, helper)
        elif Key == "s" or Key == "S":
            SettingsWindow(self, helper, calculator)
        elif Key == "BackSpace":
            self.backspace(calculator)
    def toggleBorderDisplay(self, calculator): # toggles border display
        global BorderDisplay
        if BorderDisplay == True:
            BorderDisplay = False
            self.title("PraktiCalc")
            self.OutputFrame.grid(row=0, column=0, columnspan=4, sticky="nesw")
            self.CopyButton.grid(row=0, column=4, sticky="nesw")
            self.BackspaceButton.grid(row=0, column=5, sticky="nesw")
            self.ExitButton.grid(row=6, column=0, sticky="nesw")
            self.WindowFrame.rowconfigure(0, weight=1)
            self.updateDisplay(calculator)
        elif BorderDisplay == False:
            BorderDisplay = True
            self.title("Border Display")
            self.OutputFrame.grid_remove()
            self.CopyButton.grid_remove()
            self.BackspaceButton.grid_remove()
            self.ExitButton.grid_remove()
            self.BackspaceButton.grid(row=6, column=0, sticky="nesw")
            self.WindowFrame.rowconfigure(0, weight=0, uniform="")
            self.updateDisplay(calculator)
    def copyResult(self): # copies the result
        self.clipboard_clear()
        self.clipboard_append(self.Output.cget("text"))
        self.update()
    def updateDisplay(self, calculator): # updates output
        if BorderDisplay == True:
            self.title(calculator.CalculationString)
        else:
            self.Output.config(text=calculator.CalculationString)
    def append(self, value, calculator):
        calculator.append(value)
        self.updateDisplay(calculator)
    def zero(self, calculator):
        calculator.zero()
        self.updateDisplay(calculator)
    def calculate(self, parent, helper, calculator):
        try:
            calculator.calculate()
        except Exception as e:
            Dialog().error(str(e), parent, helper)
        self.updateDisplay(calculator)
    def clear(self, calculator):
        calculator.clear()
        self.updateDisplay(calculator)
    def backspace(self, calculator):
        calculator.backspace()
        self.updateDisplay(calculator)

# settings window
class SettingsWindow(tk.Toplevel):
    def __init__(self, parent, helper, calculator):
        global MsgBoxStyles, CurrentMsgBoxStyle, BorderDisplay, theming
        super().__init__(parent)
        self.title("Settings")
        self.config(width=250, height=152)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        if platform.system() == "Windows":
            self.attributes("-toolwindow", True)
            self.focus_force()
        helper.changeTheme(self)
        SettingsWindowFrame = ttk.Frame(self)
        SettingsWindowFrame.columnconfigure(0, weight=1)
        ThemeFrame = ttk.LabelFrame(SettingsWindowFrame, text="Theme")
        ThemeFrame.columnconfigure(0, weight=1)
        self.ThemeSelector = ttk.Combobox(ThemeFrame, values=["plastik", "keramik", "breeze", "yaru", "black", "scidgrey", "scidblue", "scidpurple", "scidpink", "scidgreen", "scidmint", "scidsand", "classic"])
        self.ThemeSelector.set(thettktheme)
        NativeThemeToggle = ttk.Checkbutton(ThemeFrame, text="native theme", variable=parent.UseNativeThemeTkVar)
        ThemeFrame.grid(row=0, column=0, sticky="news", padx=10)
        self.ThemeSelector.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        NativeThemeToggle.grid(row=1, column=0, sticky="w")
        BorderDisplayToggle = ttk.Checkbutton(SettingsWindowFrame, text="Border Display", variable=parent.BorderDisplayTkVar, command=lambda: parent.toggleBorderDisplay(calculator))
        MsgBoxStyleFrame = ttk.LabelFrame(SettingsWindowFrame, text="Dialog Style")
        MsgBoxStyleFrame.columnconfigure(0, weight=1)
        MsgBoxStyleSelect = ttk.OptionMenu(MsgBoxStyleFrame, parent.CurrentMsgBoxStyleTkVar, CurrentMsgBoxStyle, *MsgBoxStyles)
        SettingsOKButton = ttk.Button(SettingsWindowFrame, text="OK", command=lambda: self.loadTheme(parent, helper))
        SettingsWindowFrame.grid(row=0, column=0, sticky="nesw")
        if theming == 0:
            self.ThemeSelector.config(state="disabled")
            NativeThemeToggle.config(state="disabled")
        BorderDisplayToggle.grid(row=1, column=0, sticky="w", padx=10)
        MsgBoxStyleFrame.grid(row=3, column=0, sticky="ew", padx=10)
        MsgBoxStyleSelect.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        SettingsOKButton.grid(row=4, column=0, sticky="ew", padx=10, pady=10)
    def loadTheme(self, parent, helper): # saves the selected theme choice in the settigns window
        global CurrentMsgBoxStyle, thettktheme, DarkMode, UseNativeTheme
        thettktheme = self.ThemeSelector.get()
        UseNativeTheme = parent.UseNativeThemeTkVar.get()
        if UseNativeTheme == False and self.ThemeSelector.get() == "black" or self.ThemeSelector.get() == "equilux":
            DarkMode = True
        else:
            DarkMode = False
        helper.ajustTitleBars()
        CurrentMsgBoxStyle = parent.CurrentMsgBoxStyleTkVar.get()
        try:
            helper.changeTheme(parent)
        except:
            pass
        self.destroy()

# info and error dialogs
class Dialog:
    def info(self, parent, helper): # shows info dialogs
        infotext = "PraktiCalc\nVersion " + PraktiCalcVersion + "\nrunning on Python "+ platform.python_version() + "\nLicensed under GPLv3\nread more at https://www.gnu.org/licenses/\nthemes provided by the ttkthemes library"
        if CurrentMsgBoxStyle == "Tkinter":
            messagebox.showinfo("About PraktiCalc", infotext)
        elif CurrentMsgBoxStyle == "Alternative":
            CustomInfox = tk.Toplevel(parent)
            CustomInfox.title("About PraktiCalc")
            CustomInfox.rowconfigure(0, weight=1)
            CustomInfox.columnconfigure(0, weight=1)
            if platform.system() == "Windows":
                CustomInfox.attributes("-toolwindow", True)
                CustomInfox.focus_force()
            helper.changeTheme(CustomInfox)
            CustomInfoFrame = ttk.Frame(CustomInfox)
            CustomInfoFrame.rowconfigure(0, weight=1)
            CustomInfoFrame.columnconfigure(0, weight=1)
            CustomInfoExit = ttk.Button(CustomInfoFrame, text="OK", command=CustomInfox.destroy)
            ExtendedInfoFrame = ttk.LabelFrame(CustomInfoFrame, relief="sunken", text="[i]")
            ExtendedInfoFrame.rowconfigure(0, weight=1)
            ExtendedInfoFrame.rowconfigure(1, weight=1)
            ExtendedInfoFrame.columnconfigure(0, weight=1)
            ExtInfoIcon = ttk.Label(ExtendedInfoFrame, image=parent.icon)
            ExtInfoText1 = ttk.Label(ExtendedInfoFrame, text=infotext, justify="left")
            CustomInfoFrame.grid(row=0, column=0, sticky="nesw")
            CustomInfoExit.grid(row=1, column=1, padx=10, pady=10)
            ExtendedInfoFrame.grid(row=0, column=0, padx=20, pady=10, sticky="nesw")
            ExtInfoIcon.grid(row=0, column=0)
            ExtInfoText1.grid(row=1, column=0)
        else:
            if platform.system() == "Windows":
                pyver = platform.python_version()
                if CurrentMsgBoxStyle == "VBScript":
                    subprocess.Popen(["wscript", VBSInfoPath, PraktiCalcVersion, pyver])
                elif CurrentMsgBoxStyle == "Windows Messaging Service":
                    subprocess.Popen(["msg", getpass.getuser(), infotext])
                elif CurrentMsgBoxStyle == "Windows Shutdown":
                    subprocess.Popen(["shutdown", "/s", "/t", "60", "/c", infotext])
                    time.sleep(20)
                    subprocess.Popen(["shutdown", "/a"])
                else:
                    print("ERROR: Unknown Message Box Style")
            else:
                if CurrentMsgBoxStyle == "xmessage":
                    subprocess.Popen(["xmessage", "-title", "About PraktiCalc", infotext])
                elif CurrentMsgBoxStyle == "yad":
                    subprocess.Popen(["yad", "--title=About PraktiCalc", "--info", "--image=" + PraktiCalcIconPath, "--button=OK", "--text=" + infotext])
                elif CurrentMsgBoxStyle == "kdialog":
                    subprocess.Popen(["kdialog", "--title=About PraktiCalc", "--msgbox", infotext])
                elif CurrentMsgBoxStyle == "zenity":
                    subprocess.Popen(["zenity", "--title=About PraktiCalc", "--info", "--icon=" + PraktiCalcIconPath, "--text=" + infotext])
                elif CurrentMsgBoxStyle == "AppleScript":
                    asc = f'display dialog "{infotext}" with icon POSIX file "{PraktiCalcIconPath}"'
                    subprocess.run(["osascript", "-e", asc])
                elif CurrentMsgBoxStyle == "Xdialog":
                    subprocess.Popen(["Xdialog", "--title=About PraktiCalc", "--msgbox", infotext, "10", "40"])
                else:
                    print("ERROR: Unknown Message Box Style")
    def error(self, message, parent, helper): # shows error dialogs
        if CurrentMsgBoxStyle == "Tkinter":
            messagebox.showerror("Error", message)
        elif CurrentMsgBoxStyle == "Alternative":
            ErrorWindow = tk.Toplevel(parent)
            ErrorWindow.title("Error")
            ErrorWindow.rowconfigure(0, weight=1)
            ErrorWindow.columnconfigure(0, weight=1)
            if platform.system() == "Windows":
                ErrorWindow.attributes("-toolwindow", True)
                ErrorWindow.focus_force()
            helper.changeTheme(ErrorWindow)
            ErrorWindowFrame = ttk.Frame(ErrorWindow)
            ErrorWindowFrame.rowconfigure(0, weight=1)
            ErrorWindowFrame.columnconfigure(0, weight=1)
            ErrorExitButton = ttk.Button(ErrorWindowFrame, text="OK", command=ErrorWindow.destroy)
            ExtendedErrorFrame = ttk.LabelFrame(ErrorWindowFrame, relief="sunken", text="[X]")
            ExtendedErrorFrame.rowconfigure(0, weight=1)
            ExtendedErrorFrame.columnconfigure(0, weight=1)
            ErrorTextLabel = ttk.Label(ExtendedErrorFrame, text=message)
            ErrorWindowFrame.grid(row=0, column=0, sticky="nesw")
            ErrorExitButton.grid(row=1, column=1, padx=10, pady=10)
            ExtendedErrorFrame.grid(row=0, column=0, padx=20, pady=10, sticky="nesw")
            ErrorTextLabel.grid(row=0, column=0)
        else:
            if platform.system() == "Windows":
                if CurrentMsgBoxStyle == "VBScript":
                    subprocess.Popen(["wscript", VBSErrorPath, message])
                elif CurrentMsgBoxStyle == "Windows Messaging Service":
                    subprocess.Popen(["msg", getpass.getuser(), message])
                elif CurrentMsgBoxStyle == "Windows Shutdown":
                    subprocess.Popen(["shutdown", "/s", "/t", "60", "/c", message])
                    time.sleep(10)
                    subprocess.Popen(["shutdown", "/a"])
                else:
                    print("ERROR: Unknown Message Box Style")
            else:
                if CurrentMsgBoxStyle == "xmessage":
                    subprocess.Popen(["xmessage", "-title", "Error", "[X] " + message])
                elif CurrentMsgBoxStyle == "yad":
                    subprocess.Popen(["yad", "--title=Error", "--error", "--image=dialog-error", "--button=OK", "--no-markup", "--text", message])
                elif CurrentMsgBoxStyle == "kdialog":
                    subprocess.Popen(["kdialog", "--title=Error", "--error", message])
                elif CurrentMsgBoxStyle == "zenity":
                    subprocess.Popen(["zenity", "--title=Error", "--error", "--no-markup", "--text", message])
                elif CurrentMsgBoxStyle == "AppleScript":
                    asc = f'display dialog "{message}" with icon stop'
                    subprocess.run(["osascript", "-e", asc])
                elif CurrentMsgBoxStyle == "Xdialog":
                    subprocess.Popen(["Xdialog", "--title=Error", "--msgbox", message, "10", "40"])
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
        helper.changeTheme(self)
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
        helper.changeTheme(self)
        HistoryWindowFrame = ttk.Frame(self)
        HistoryWindowFrame.columnconfigure(0, weight=1)
        HistoryWindowFrame.rowconfigure(0, weight=1)
        HistoryWindowFrame.grid(row=0, column=0, sticky="nesw")
        self.HistoryTreeview = ttk.Treeview(HistoryWindowFrame, height=15)
        self.HistoryTreeview.heading("#0", text="History")
        for entry in calculator.HistoryList:
            self.HistoryTreeview.insert("", tk.END, text=entry)
        HistoryClearButton = ttk.Button(HistoryWindowFrame, text="Clear History", command=lambda: self.clear(calculator))
        self.HistoryTreeview.grid(row=0, column=0, sticky="nesw")
        HistoryClearButton.grid(row=1, column=0, sticky="nesw", padx=5, pady=5)
    def clear(self, calculator):
        calculator.clearHistory()
        self.HistoryTreeview.delete(*self.HistoryTreeview.get_children())

# extension window
class ExtensionWindow(tk.Toplevel):
    def __init__(self, parent, helper, calculator):
        super().__init__(parent)
        self.title("Decimal Converter")
        self.config(height=200, width=500)
        self.bind("<Key>", lambda event: self.MoreWindowEnterKey(event, parent, helper))
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        if platform.system() == "Windows":
            self.attributes("-toolwindow", True)
            self.focus_force()
        helper.changeTheme(self)
        ConverterWindowFrame = ttk.Frame(self)
        DecimalFrame = ttk.LabelFrame(ConverterWindowFrame, text="Decimal")
        self.DecimalInput = ttk.Entry(DecimalFrame, width=70)
        DecimalFrame.columnconfigure(0, weight=1)
        ConverterWindowFrame.columnconfigure(0, weight=1)
        ConverterWindowFrame.columnconfigure(1, weight=1)
        ConverterWindowFrame.rowconfigure(1, weight=1)
        InsertButton = ttk.Button(DecimalFrame, text="OK", command=lambda: self.convert(parent, helper))
        binFrame = ttk.LabelFrame(ConverterWindowFrame, text="Binary")
        hexFrame = ttk.LabelFrame(ConverterWindowFrame, text="Hexadecimal")
        binFrame.rowconfigure(0, weight=1)
        binFrame.columnconfigure(0, weight=1)
        hexFrame.rowconfigure(0, weight=1)
        hexFrame.columnconfigure(0, weight=1)
        self.BinaryLabel = ttk.Label(binFrame, text="")
        self.HexLabel = ttk.Label(hexFrame, text="")
        BinCopyButton = ttk.Button(binFrame, text="Copy", command=lambda: self.copybin(parent))
        HexCopyButton = ttk.Button(hexFrame, text="Copy", command=lambda: self.copyhex(parent))
        ConverterWindowFrame.grid(row=0, column=0, sticky="nesw")
        DecimalFrame.grid(row=0, column=0, columnspan=2, sticky="nesw", padx=5)
        self.DecimalInput.grid(row=0, column=0, pady=5, padx=5, sticky="nesw")
        InsertButton.grid(row=0, column=1, padx=5, pady=5)
        binFrame.grid(row=1, column=0, sticky="nesw", padx=5)
        hexFrame.grid(row=1, column=1, sticky="nesw", padx=5)
        self.BinaryLabel.grid(row=0, column=0)
        self.HexLabel.grid(row=0, column=0)
        BinCopyButton.grid(row=1, column=0)
        HexCopyButton.grid(row=1, column=0)
        if platform.system() != "Windows":
            self.DecimalInput.focus_set()
    def MoreWindowEnterKey(self, event, parent, helper): # processes the enter key inside the window
        MoreWindowKey = event.keysym
        if MoreWindowKey == "Return":
            self.convert(parent, helper)
    def convert(self, parent, helper): # converts decimal numbers into binary and hexadecimal
        cp = str(self.DecimalInput.get())
        try:
            DecimalNumber = int(cp)
            BinaryNumber = bin(DecimalNumber)[2:]
            HexadecimalNumber = hex(DecimalNumber)
            self.BinaryLabel.config(text=str(BinaryNumber))
            self.HexLabel.config(text=str(HexadecimalNumber))
        except:
            Dialog().error("Please enter a real number!", parent, helper)
    def copybin(self, parent): # copies the binary output
        parent.clipboard_clear()
        parent.clipboard_append(self.BinaryLabel.cget("text"))
        parent.update()
    def copyhex(self, parent): # copies the hexadecimal output
        parent.clipboard_clear()
        parent.clipboard_append(self.HexLabel.cget("text"))
        parent.update()

# console
class Console:
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
    def run(self, parent, helper, console):
        self.lcc = command = self.ConsoleInput.get()
        if command == "clear":
            self.ConsoleOutput.delete("1.0", tk.END)
        elif command == "aboutwindow":
            self.AboutWindow(parent, helper)
        elif command == "exit":
            parent.destroy()
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
        ConsoleIconFrame = tk.Frame(ConsoleAboutWindow, bg="black")
        ConsoleAboutIcon = tk.Label(ConsoleIconFrame, image=parent.icon_mono_inverted, fg="white")
        ConsoleAboutText = tk.Label(ConsoleAboutWindow, bg="black", text="PraktiCalc Console\nrunning on PraktiCalc " + PraktiCalcVersion + "\npowered by Python " + platform.python_version(), fg="white")
        ConsoleAboutSpacer1.grid(row=0, column=0, sticky="nesw")
        ConsoleIconFrame.grid(row=1, column=0, sticky="nesw")
        ConsoleAboutIcon.grid(row=0, column=0, padx=152, pady=20)
        ConsoleAboutText.grid(row=2, column=0, sticky="nesw")
        ConsoleAboutSpacer2.grid(row=3, column=0, sticky="nesw")
        helper.ajustTitleBars()

Calculator = PraktiCalculator()
WindowHelp = WindowHelper()
Window = MainWindow(WindowHelp, Calculator)
if "--console" in sys.argv:
    cmd = Console()
    CMDWindow = ConsoleWindow(Window, WindowHelp, cmd)
Window.mainloop()
