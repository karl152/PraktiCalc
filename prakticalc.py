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

# import modules
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
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
import os
# variables
CLIHelp = "--help" in sys.argv
CLIVersion = "--version" in sys.argv
PraktiCalcVersion = "1.3"
BypassWindowsDPIFix = "--nodpiawareness" in sys.argv
if platform.system() == "Windows":
    MsgBoxStyles = ["Tkinter", "Alternative", "VBS"]
    if BypassWindowsDPIFix == False:
        import ctypes
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except:
            pass
    if platform.release() == "Vista" or platform.release() == "7" or platform.release() == "8" or platform.release() == "8.1":
        WingWebDings = True
    else:
        WingWebDings = False
else:
    WingWebDings = False
    MsgBoxStyles = ["Tkinter", "Alternative"]
    AdditionalLinuxMsgBoxStyles = ["xmessage", "yad", "kdialog", "zenity"]
    for MsgBoxStyle in AdditionalLinuxMsgBoxStyles:
        if shutil.which(MsgBoxStyle):
            MsgBoxStyles.append(MsgBoxStyle)
CurrentMsgBoxStyle = 1
if CLIHelp == True:
    if platform.system() == "Windows":
        messagebox.showinfo("PraktiCalc CLI Options", "PraktiCalc " + PraktiCalcVersion + """ CLI Options:
--debug: add a test button for debugging
--nodpiawareness: disable Windows DPI Awareness
--dark: enable dark mode by default
--console: show console for debugging
--equilux: set the dark theme to equilux
--help: display this help text and exit
--version: display version and exit""")
    else:
        print("PraktiCalc " + PraktiCalcVersion + " CLI Options")
        print("--debug   | add a test button for debugging")
        print("--dark    | enable dark mode by default")
        print("--console | show console for debugging")
        print("--breeze  | set the light theme to breeze")
        print("--yaru    | set the light theme to yaru")
        print("--equilux | set the dark theme to equilux")
        print("--help    | display this help text and exit")
        print("--version | display version and exit")
    exit()
if CLIVersion == True:
    if platform.system() == "Windows":
        messagebox.showinfo("PraktiCalc " + PraktiCalcVersion, "PraktiCalc " + PraktiCalcVersion)
    else:
        print("PraktiCalc " + PraktiCalcVersion)
    exit()

def testPyInstallerOneFile():
    try:
        print(sys._MEIPASS)
        return True
    except:
        return False

RunningAsOneFileExe = testPyInstallerOneFile()

# ttkthemes directory workaround for AppImage
if os.path.exists("./usr/share/tcltk/ttkthemes"):
    # Wenn innerhalb des AppImage/AppDir gestartet:
    tcl_dir = os.path.abspath("./usr/share/tcltk/ttkthemes")

if RunningAsOneFileExe == True:
    PraktiCalcIconPath = (sys._MEIPASS + "/PraktiCalculator_icon.png")
    PraktiCalcIconMonoPath = (sys._MEIPASS + "/PraktiCalculator_icon.xbm")
    PraktiCalcIconMonoInvertedPath = (sys._MEIPASS + "/PraktiCalculator_icon_inverted.xbm")
    VBSInfoPath = (sys._MEIPASS + "/info.vbs")
    VBSErrorPath = (sys._MEIPASS + "/error.vbs")
else:
    PraktiCalcIconPath = "PraktiCalculator_icon.png"
    PraktiCalcIconMonoPath = "PraktiCalculator_icon.xbm"
    PraktiCalcIconMonoInvertedPath = "PraktiCalculator_icon_inverted.xbm"
    VBSInfoPath = "info.vbs"
    VBSErrorPath = "error.vbs"

console = "--console" in sys.argv
breeze = "--breeze" in sys.argv
yaru = "--yaru" in sys.argv
equilux = "--equilux" in sys.argv
if breeze == True:
    thettktheme = "breeze"
elif yaru == True:
    thettktheme = "yaru"
else:
    thettktheme = "plastik"
if equilux == True:
    darkttktheme = "equilux"
else:
    darkttktheme = "black"
usedttktheme = thettktheme
Input1 = "0"
Input2 = "0"
Stage = 0
Operator = "op"
StatusBar = False
CustomMsgBox = True
DarkMode = "--dark" in sys.argv
debug = "--debug" in sys.argv
historylist = []
FinalResult = 0
aFinalResult = 0
DecimalNumber = 0
BinaryNumber = 0
HexadecimalNumber = 0

# functions
def changeTheme(WindowName):
    global theming
    if platform.system() == "Windows":
        if DarkMode == True:
            style = ThemedStyle(WindowName)
            style.theme_use(usedttktheme)
        else:
            style = ttk.Style(WindowName)
            style.theme_use("vista")
        if WingWebDings == True:
            style.configure("Webdings.TButton", font=webdingsfont)
            style.configure("Wingdings.TButton", font=wingdingsfont)
    else:
        if theming == 1 or 2:
            try:
                style = ThemedStyle(WindowName)
                style.theme_use(usedttktheme)
            except:
                theming = 2
                theme_base = os.path.join(sys._MEIPASS, "ttkthemes", "themes")
                theme_path = os.path.join(theme_base, usedttktheme)
                WindowName.tk.call("lappend", "auto_path", theme_base)
                try:
                    WindowName.tk.call("package", "require", f"ttk::theme::{usedttktheme}")
                except:
                    theme_tcl = os.path.join(theme_path, usedttktheme + ".tcl")
                    if os.path.exists(theme_tcl):
                        WindowName.tk.call("source", theme_tcl)
                    else:
                        print(f"Couldn't find theme {theme_tcl}")
                try:
                    ttk.Style().theme_use(usedttktheme)
                except:
                    print("Using default ttk theme")
def info() :
    CustomInfo()
def processNumber(number):
    global Input1, Input2, Output, Stage
    if Stage == 4 or Stage == 5:
        Input2 = str(Input2) + number
        Output.config(text=Input2)
    if Stage == 3 :
        Input2 = number
        Output.config(text=Input2)
        Stage = 4
    if Stage == 1 or Stage == 2:
        Input1 = str(Input1) + number
        Output.config(text=Input1)
    if Stage == 0 :
        Input1 = number
        Output.config(text=Input1)
        Stage = 1
def processOperator(TheOneAndOnlyOperatorThatShouldBeProcessed):
    global Stage, Output, Operator, FinalResult, aFinalResult, Input1, Input2
    if Stage != 0 and Stage != 3 and Stage != 4 and Stage != 5 and Stage != 6 :
        Stage = 3
        Operator = TheOneAndOnlyOperatorThatShouldBeProcessed
        Output.config(text="0")
    if Stage == 4 or Stage == 5 :
        calc()
        Input1 = FinalResult
        Operator = TheOneAndOnlyOperatorThatShouldBeProcessed
        Input2 = "0"
        Stage = 3
    if Stage == 6 :
        Operator = TheOneAndOnlyOperatorThatShouldBeProcessed
        Stage = 3
        Output.config(text="0")
        Input1 = FinalResult
def zero() :
    global Input1, Input2, Output, Stage
    if Stage == 4 or Stage == 5:
        Input2 = str(Input2) + "0"
        Output.config(text=Input2)
    if Stage == 3 :
        Input2 = "0"
        Stage = 4
    if Stage == 1 or Stage == 2:
        Input1 = str(Input1) + "0"
        Output.config(text=Input1)
    if Stage == 0 :
        pass
    SizeReload()
def clear() :
    global Input1, Input2, Output, Stage, Status, StatusBar
    Input1 = "0"
    Input2 = "0"
    Stage = 0
    Output.config(text="0")
    if StatusBar == True :
        Status.config(text="Ready")
    FinalResult = 0
    aFinalResult = 0
    SizeReload()
def comma() :
    global Input1, Input2, Output, Stage
    if Stage == 5 :
        Input2 = str(Input2) + "."
        Output.config(text=Input2)
    if Stage == 4 :
        Input2 = str(Input2) + "."
        Output.config(text=Input2)
        Stage = 5
    if Stage == 3 :
        Input2 = "0."
        Output.config(text=Input2)
        Stage = 5
    if Stage == 2 :
        pass
    if Stage == 1 :
        Input1 = str(Input1) + "."
        Output.config(text=Input1)
        Stage = 2
    if Stage == 0 :
        Input1 = "0."
        Output.config(text=Input1)
        Stage = 2
    SizeReload()
def calc() :
    global historylist, Input1, Stage, Input2, Output, Operator, FinalResult, aFinalResult
    if len(historylist) >= 16:
        historylist.pop(0)
    if Stage == 6 :
        if Operator == "+" :
            aFinalResult = FinalResult
            FinalResult = FinalResult + float(Input2)
            Output.config(text=str(FinalResult))
            historylist.append(str(aFinalResult) + " + " + Input2 + " = " + str(FinalResult))
        if Operator == "-" :
            FinalResult = FinalResult - float(Input2)
            Output.config(text=str(FinalResult))
            historylist.append(str(aFinalResult) + " - " + Input2 + " = " + str(FinalResult))
        if Operator == "*" :
            FinalResult = FinalResult * float(Input2)
            Output.config(text=str(FinalResult))
            historylist.append(str(aFinalResult) + " * " + Input2 + " = " + str(FinalResult))
        if Operator == "/" :
            FinalResult = FinalResult / float(Input2)
            Output.config(text=str(FinalResult))
            historylist.append(str(aFinalResult) + " / " + Input2 + " = " + str(FinalResult))
        if Operator == "sqrt" :
            aFinalResult = FinalResult
            FinalResult = FinalResult ** 0.5
            Output.config(text=str(FinalResult))
            historylist.append("√" + str(aFinalResult) + " = " + str(FinalResult))
    if Stage != 0 and Stage != 1 and Stage != 2 and Stage != 3 and Stage != 6 :
        Stage = 6
        if Operator == "+" :
            FinalResult = (float(Input1) + float(Input2))
            Output.config(text=float(Input1) + float(Input2))
            historylist.append(str(Input1) + " + " + Input2 + " = " + str(FinalResult))
        if Operator == "-" :
            FinalResult = (float(Input1) - float(Input2))
            Output.config(text=float(Input1) - float(Input2))
            historylist.append(str(Input1) + " - " + Input2 + " = " + str(FinalResult))
        if Operator == "*" :
            FinalResult = (float(Input1) * float(Input2))
            Output.config(text=float(Input1) * float(Input2))
            historylist.append(str(Input1) + " * " + Input2 + " = " + str(FinalResult))
        if Operator == "/" :
            if Input2 == "0" :
                if StatusBar == False :
                    CustomDiv0()
                if StatusBar == True :
                    Status.config(text="Error: Division by 0")
                clear()
            else :
                FinalResult = (float(Input1) / float(Input2))
                Output.config(text=float(Input1) / float(Input2))
                historylist.append(str(Input1) + " / " + Input2 + " = " + str(FinalResult))
        if Operator == "sqrt" :
            Input2 = str(float(Input1) ** 0.5)
            Output.config(text=Input2)
    if Operator == "sqrt" :
        if Stage == 3 :
            FinalResult = float(Input1) ** 0.5
            Output.config(text=FinalResult)
            historylist.append("√" + str(Input1) + " = " + str(FinalResult))
            Stage = 6
    SizeReload()
def KeyPress(event):
    Key = event.keysym
    if Key == "1" or Key == "2" or Key == "3" or Key == "4" or Key == "5" or Key == "6" or Key == "7" or Key == "8" or Key == "9":
        processNumber(Key)
    if Key == "0" :
        zero()
    if Key == "equal" or Key == "Return":
        calc()
    if Key == "add" :
        processOperator("+")
    if Key == "subtract" :
        processOperator("-")
    if Key == "asterisk" :
        processOperator("*")
    if Key == "slash" :
        processOperator("/")
    if Key == "h" or Key == "H":
        History()
    if Key == "c" or Key == "C":
        clear()
    if Key == "i" :
        info()
    if Key == "s" or Key == "S":
        Settings()
    if Key == "comma" :
        comma()
    if Key == "BackSpace" :
        Backspace()
def Settings() :
    global Status, SettingsWindow, StatusBar, StatusBarToggle, CustomMsgBox, CustomMsgBoxToggle, DarkMode, DarkModeToggle, MsgBoxStyles, CurrentMsgBoxStyle, MsgBoxStyleSelect
    SettingsWindow = tk.Toplevel(MainWindow)
    SettingsWindow.title("Settings")
    SettingsWindow.config(width=250, height=152)
    SettingsWindow.rowconfigure(0, weight=1)
    SettingsWindow.columnconfigure(0, weight=1)
    if platform.system() == "Windows":
        SettingsWindow.attributes("-toolwindow", True)
        SettingsWindow.focus_force()
    changeTheme(SettingsWindow)
    SettingsWindowFrame = ttk.Frame(SettingsWindow)
    SettingsWindowFrame.columnconfigure(0, weight=1)
    StatusBarToggle = ttk.Checkbutton(SettingsWindowFrame, text="Status Bar", command=ToggleStatusBar, variable=StatusBarTkVar)
    CustomMsgBoxToggle = ttk.Checkbutton(SettingsWindowFrame, text="Alternative Messageboxes", command=ToggleCustomMsgBoxes)
    if CustomMsgBox == False :
        CustomMsgBoxToggle.state(["!selected"])
    if CustomMsgBox == True :
        CustomMsgBoxToggle.state(["selected"])
    DarkModeToggle = ttk.Checkbutton(SettingsWindowFrame, text="Dark Mode", command=ChangeDarkMode, variable=DarkModeTkVar)
    MsgBoxStyleFrame = ttk.LabelFrame(SettingsWindowFrame, text="Messagebox Style")
    MsgBoxStyleFrame.columnconfigure(0, weight=1)
    MsgBoxStyleSelect = ttk.Combobox(MsgBoxStyleFrame, values=MsgBoxStyles)
    MsgBoxStyleSelect.current(CurrentMsgBoxStyle)
    SettingsOKButton = ttk.Button(SettingsWindowFrame, text="OK", command=loadTheme)
    SettingsWindowFrame.grid(row=0, column=0, sticky="nesw")
    StatusBarToggle.grid(row=0, column=0, sticky="w", padx=10)
    # CustomMsgBoxToggle.grid(row=1, column=0, sticky="w", padx=10)
    DarkModeToggle.grid(row=2, column=0, sticky="w", padx=10)
    MsgBoxStyleFrame.grid(row=3, column=0, sticky="ew", padx=10)
    MsgBoxStyleSelect.grid(row=0, column=0, sticky="ew")
    SettingsOKButton.grid(row=4, column=0, sticky="ew", padx=10, pady=10)
def loadTheme():
    global SettingsWindow, CurrentMsgBoxStyle, MsgBoxStyleSelect
    CurrentMsgBoxStyle = MsgBoxStyleSelect.current()
    # print(CurrentMsgBoxStyle)
    SettingsWindow.destroy()
def ToggleCustomMsgBoxes():
    global CustomMsgBox, CustomMsgBoxToggle
    if CustomMsgBox == False:
        CustomMsgBox = True
    elif CustomMsgBox == True:
        CustomMsgBox = False
def ToggleStatusBar():
    global Status, StatusBar, StatusBarToggle, StatusDecoration, MainWindow
    if StatusBar == True:
        Status.config(text="")
        StatusBar = False
        StatusDecoration.config(text="")
        MainWindow.config(width=256, height=315)
    elif StatusBar == False:
        MainWindow.config(width=256, height=330)
        Status.config(text="Ready")
        StatusBar = True
        StatusDecoration.config(text="__________________________________________________")
def ChangeDarkMode() :
    global DarkMode, usedttktheme, SettingsWindow, style, HistoryX, MoreWindow
    if DarkMode == False :
        DarkMode = True
        usedttktheme = darkttktheme
        changeTheme(MainWindow)
        changeTheme(SettingsWindow)
        changeTheme(HistoryX)
        changeTheme(MoreWindow)
        changeTheme(ErrorWindow)
        changeTheme(CustomInfox)
    elif DarkMode == True :
        DarkMode = False
        usedttktheme = thettktheme
        changeTheme(MainWindow)
        changeTheme(SettingsWindow)
        changeTheme(HistoryX)
        changeTheme(MoreWindow)
        changeTheme(ErrorWindow)
        changeTheme(CustomInfox)
def CustomDiv0() :
    showError("Division by 0")
def CustomInfo() :
    global CustomInfox
    infotext = "PraktiCalc\nVersion " + PraktiCalcVersion + " (in development)\nrunning on Python "+ platform.python_version() + "\nLicensed under GPLv3\nread more at https://www.gnu.org/licenses/"
    if CurrentMsgBoxStyle == 0:
        messagebox.showinfo("About PraktiCalc", infotext)
    elif CurrentMsgBoxStyle == 1:
        CustomInfox = tk.Toplevel(MainWindow)
        CustomInfox.title("About PraktiCalc")
        CustomInfox.rowconfigure(0, weight=1)
        CustomInfox.columnconfigure(0, weight=1)
        if platform.system() == "Windows":
            CustomInfox.attributes("-toolwindow", True)
            CustomInfox.focus_force()
        changeTheme(CustomInfox)
        CustomInfoFrame = ttk.Frame(CustomInfox)
        CustomInfoFrame.rowconfigure(0, weight=1)
        CustomInfoFrame.columnconfigure(0, weight=1)
        CustomInfoExit = ttk.Button(CustomInfoFrame, text="OK", command=closeCustomInfo)
        ExtendedInfoFrame = ttk.LabelFrame(CustomInfoFrame, relief="sunken", text="[i]")
        ExtendedInfoFrame.rowconfigure(0, weight=1)
        ExtendedInfoFrame.rowconfigure(1, weight=1)
        ExtendedInfoFrame.columnconfigure(0, weight=1)
        ExtInfoIcon = ttk.Label(ExtendedInfoFrame, image=MainWindow.icon)
        ExtInfoText1 = ttk.Label(ExtendedInfoFrame, text=infotext, justify="left")
        CustomInfoFrame.grid(row=0, column=0, sticky="nesw")
        CustomInfoExit.grid(row=1, column=1, padx=10, pady=10)
        ExtendedInfoFrame.grid(row=0, column=0, padx=20, pady=10, sticky="nesw")
        ExtInfoIcon.grid(row=0, column=0)
        ExtInfoText1.grid(row=1, column=0)
    else:
        if platform.system() == "Windows":
            if CurrentMsgBoxStyle == 2:
                pyver = platform.python_version()
                subprocess.run(["wscript", VBSInfoPath, PraktiCalcVersion, pyver])
            else:
                print("ERROR: Unknown Message Box Style")
        else:
            if MsgBoxStyles[CurrentMsgBoxStyle] == "xmessage":
                subprocess.Popen(["xmessage", "-title", "About PraktiCalc", infotext])
            elif MsgBoxStyles[CurrentMsgBoxStyle] == "yad":
                subprocess.Popen(["yad", "--title=About PraktiCalc", "--info", "--image=" + PraktiCalcIconPath, "--button=OK", "--text=" + infotext])
            elif MsgBoxStyles[CurrentMsgBoxStyle] == "kdialog":
                subprocess.Popen(["kdialog", "--title=About PraktiCalc", "--msgbox", infotext])
            elif MsgBoxStyles[CurrentMsgBoxStyle] == "zenity":
                subprocess.Popen(["zenity", "--title=About PraktiCalc", "--info", "--icon=" + PraktiCalcIconPath, "--text=" + infotext])
            else:
                print("ERROR: Unknown Message Box Style")
def closeCustomInfo() :
    global CustomInfox
    CustomInfox.destroy()
def closeCustomDiv0() :
    global Div0Error
    Div0Error.destroy()
def showError(message):
    global ErrorWindow
    if CurrentMsgBoxStyle == 0:
        messagebox.showerror("Error", message)
    elif CurrentMsgBoxStyle == 1:
        ErrorWindow = tk.Toplevel(MainWindow)
        ErrorWindow.title("Error")
        ErrorWindow.rowconfigure(0, weight=1)
        ErrorWindow.columnconfigure(0, weight=1)
        if platform.system() == "Windows":
            ErrorWindow.attributes("-toolwindow", True)
            ErrorWindow.focus_force()
        changeTheme(ErrorWindow)
        ErrorWindowFrame = ttk.Frame(ErrorWindow)
        ErrorWindowFrame.rowconfigure(0, weight=1)
        ErrorWindowFrame.columnconfigure(0, weight=1)
        ErrorExitButton = ttk.Button(ErrorWindowFrame, text="OK", command=closeError)
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
            if CurrentMsgBoxStyle == 2:
                subprocess.Popen(["wscript", VBSErrorPath, message])
            else:
                print("ERROR: Unknown Message Box Style")
        else:
            if MsgBoxStyles[CurrentMsgBoxStyle] == "xmessage":
                subprocess.Popen(["xmessage", "-title", "Error", "[X] " + message])
            elif MsgBoxStyles[CurrentMsgBoxStyle] == "yad":
                subprocess.Popen(["yad", "--title=Error", "--error", "--image=dialog-error", "--button=OK", "--text=" + message])
            elif MsgBoxStyles[CurrentMsgBoxStyle] == "kdialog":
                subprocess.Popen(["kdialog", "--title=Error", "--error", message])
            elif MsgBoxStyles[CurrentMsgBoxStyle] == "zenity":
                subprocess.Popen(["zenity", "--title=Error", "--error", "--text=" + message])
            else:
                print("ERROR: Unknown Message Box Style")
def closeError():
    global ErrorWindow
    ErrorWindow.destroy()
def SizeReload() :
    pass
def CharacterStatus() :
    global Status, StatusBar
    if StatusBar == True :
        Status.config(text="PraktiCalc only supports up to 15 characters!")
def Backspace() :
    global Input1, Input2
    if Stage == 1 :
        Input1 = Input1[:len(Input1) - 1]
    if Stage == 2 :
        Input1 = Input1[:len(Input1) - 1]
    if Stage == 4 :
        Input2 = Input2[:len(Input2) - 1]
    if Stage == 5 :
        Input2 = Input2[:len(Input2) - 1]
    updateDisplay()
def updateDisplay() :
    global Input1, Output, Input2, Stage
    if Stage == 5 :
        Output.config(text=Input2)
        if not "." in Input2 :
            Stage = 4
    if Stage == 4 :
        Output.config(text=Input2)
        if len(Input2) == 0 :
            Stage = 3
            Input2 = "0"
    if Stage == 3 :
        Output.config(text=Input2)
    if Stage == 2 :
        Output.config(text=Input1)
        if not "." in Input1 :
            Stage = 1
    if Stage == 1 :
        Output.config(text=Input1)
        if len(Input1) == 0 :
            Stage= 0
    if Stage == 0 :
        Output.config(text="0")
    SizeReload()
def History() :
    global HistoryX
    HistoryX = tk.Toplevel(MainWindow)
    HistoryX.rowconfigure(0, weight=1)
    HistoryX.columnconfigure(0, weight=1)
    HistoryX.title("History")
    # HistoryX.config(height=400, width=256)
    if platform.system() == "Windows":
        HistoryX.attributes("-toolwindow", True)
        HistoryX.focus_force()
    changeTheme(HistoryX)
    HistoryWindowFrame = ttk.Frame(HistoryX)
    HistoryWindowFrame.columnconfigure(0, weight=1)
    for i in range(31):
        HistoryWindowFrame.rowconfigure(i, weight=1)
    HistoryWindowFrame.grid(row=0, column=0, sticky="nesw")
    labelrow = -2
    separatorrow = -1
    for widgetnumber in range(15):
        labelrow += 2
        separatorrow += 2
        try:
            ttk.Label(HistoryWindowFrame, text=historylist[widgetnumber]).grid(row=labelrow, column=0, sticky="nesw")
            ttk.Separator(HistoryWindowFrame, orient="horizontal").grid(row=separatorrow, column=0, sticky="nesw")
        except:
            break
    HistoryClearButton = ttk.Button(HistoryWindowFrame, text="Clear History", command=clearHistory)
    HistoryClearButton.grid(row=30, column=0, sticky="nesw", padx=5, pady=5)
def minus() :
    global Input1, Input2, Output, Stage
    if Stage == 4 or Stage == 5:
        if Input2[0] != "-" :
            Input2 = "-" + str(Input2)
            Output.config(text=Input2)
        else:
            Input2 = Input2[1:]
            Output.config(text=Input2)
    if Stage == 3 :
        if Input2[0] != "-" :
            Input2 = "-"
            Output.config(text=Input2)
            Stage = 4
    if Stage == 1 or Stage == 2:
        if Input1[0] != "-" :
            Input1 = "-" + str(Input1)
            Output.config(text=Input1)
        else:
            Input1 = Input1[1:]
            Output.config(text=Input1)
    if Stage == 0 :
        if Input1[0] != "-" :
            Input1 = "-"
            Output.config(text=Input1)
            Stage = 1
    SizeReload()
def rooty() :
    global Operator, Stage
    Operator = "sqrt"
    if Stage == 1 or Stage == 2:
        Stage = 3
    calc()
def More() :
    def MoreWindowEnterKey(event):
        MoreWindowKey = event.keysym
        if MoreWindowKey == "Return":
            paste()
    global DarkMode, MoreWindow, DecimalFrame, DecimalInput, DecimalNumber, BinaryLabel, HexLabel, usedttktheme
    MoreWindow = tk.Toplevel(MainWindow)
    MoreWindow.title("Decimal Converter")
    MoreWindow.config(height=200, width=500)
    MoreWindow.bind("<Key>", MoreWindowEnterKey)
    MoreWindow.rowconfigure(0, weight=1)
    MoreWindow.columnconfigure(0, weight=1)
    if platform.system() == "Windows":
        MoreWindow.attributes("-toolwindow", True)
        MoreWindow.focus_force()
    changeTheme(MoreWindow)
    ConverterWindowFrame = ttk.Frame(MoreWindow)
    DecimalFrame = ttk.LabelFrame(ConverterWindowFrame, text="Decimal")
    DecimalInput = ttk.Entry(DecimalFrame, width=70)
    DecimalFrame.columnconfigure(0, weight=1)
    ConverterWindowFrame.columnconfigure(0, weight=1)
    ConverterWindowFrame.columnconfigure(1, weight=1)
    ConverterWindowFrame.rowconfigure(1, weight=1)
    InsertButton = ttk.Button(DecimalFrame, text="OK", command=paste)
    binFrame = ttk.LabelFrame(ConverterWindowFrame, text="Binary")
    hexFrame = ttk.LabelFrame(ConverterWindowFrame, text="Hexadecimal")
    binFrame.rowconfigure(0, weight=1)
    binFrame.columnconfigure(0, weight=1)
    hexFrame.rowconfigure(0, weight=1)
    hexFrame.columnconfigure(0, weight=1)
    BinaryLabel = ttk.Label(binFrame, text="")
    HexLabel = ttk.Label(hexFrame, text="")
    BinCopyButton = ttk.Button(binFrame, text="Copy", command=copybin)
    HexCopyButton = ttk.Button(hexFrame, text="Copy", command=copyhex)
    ConverterWindowFrame.grid(row=0, column=0, sticky="nesw")
    DecimalFrame.grid(row=0, column=0, columnspan=2, sticky="nesw", padx=5)
    DecimalInput.grid(row=0, column=0, pady=5, padx=5, sticky="nesw")
    InsertButton.grid(row=0, column=1, padx=5, pady=5)
    binFrame.grid(row=1, column=0, sticky="nesw", padx=5)
    hexFrame.grid(row=1, column=1, sticky="nesw", padx=5)
    BinaryLabel.grid(row=0, column=0)
    HexLabel.grid(row=0, column=0)
    BinCopyButton.grid(row=1, column=0)
    HexCopyButton.grid(row=1, column=0)
    if platform.system() != "Windows":
        DecimalInput.focus_set()
def paste() :
    global DecimalNumber, DecimalInput, BinaryNumber, HexadecimalNumber, BinaryLabel, HexLabel
    cp = str(DecimalInput.get())
    try:
        DecimalNumber = int(cp)
    except:
        showError("Please enter a real number!")
    DecimalInput.config(text=str(DecimalNumber))
    BinaryNumber = bin(DecimalNumber)[2:]
    HexadecimalNumber = hex(DecimalNumber)
    BinaryLabel.config(text=str(BinaryNumber))
    HexLabel.config(text=str(HexadecimalNumber))
def copybin() :
    global BinaryNumber, MainWindow
    MainWindow.clipboard_clear()
    MainWindow.clipboard_append(BinaryNumber)
    MainWindow.update()
def copyhex() :
    global HexadecimalNumber, MainWindow
    MainWindow.clipboard_clear()
    MainWindow.clipboard_append(HexadecimalNumber)
    MainWindow.update()
def clearHistory() :
    global HistoryX
    historylist.clear()
    HistoryX.destroy()
    History()
def xcheck() :
    print("Stage: " + str(Stage))
    print("Input1: " + str(Input1))
    print("Input2: " + str(Input2))
    print("Operator: " + str(Operator))
    print("FinalResult: " + str(FinalResult))
    print("aFinalResult: " + str(aFinalResult))
    print("____________________________")
def xquit() :
    MainWindow.destroy()
if DarkMode == True :
    usedttktheme = darkttktheme

# main window
MainWindow = tk.Tk()
MainWindow.title("PraktiCalc")
MainWindow.icon_mono = tk.BitmapImage(file=PraktiCalcIconMonoPath)
MainWindow.icon = tk.PhotoImage(file=PraktiCalcIconPath)
MainWindow.icon_mono_inverted = tk.BitmapImage(file=PraktiCalcIconMonoInvertedPath)
MainWindow.iconphoto(True, MainWindow.icon)
if WingWebDings == True:
    wingdingsfont = font.Font(family="Wingdings")
    webdingsfont = font.Font(family="Webdings")
DarkModeTkVar = tk.BooleanVar(value=DarkMode)
StatusBarTkVar = tk.BooleanVar(value=StatusBar)
MainWindow.config(width=256, height=315)
if console == True:
    def ConsoleAbout():
        ConsoleAboutWindow = tk.Toplevel(MainWindow)
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
        ConsoleAboutIcon = tk.Label(ConsoleIconFrame, image=MainWindow.icon_mono_inverted, fg="white")
        ConsoleAboutText = tk.Label(ConsoleAboutWindow, bg="black", text="PraktiCalc Console\nrunning on PraktiCalc " + PraktiCalcVersion + "\npowered by Python " + platform.python_version(), fg="white")
        ConsoleAboutSpacer1.grid(row=0, column=0, sticky="nesw")
        ConsoleIconFrame.grid(row=1, column=0, sticky="nesw")
        ConsoleAboutIcon.grid(row=0, column=0, padx=152, pady=20)
        ConsoleAboutText.grid(row=2, column=0, sticky="nesw")
        ConsoleAboutSpacer2.grid(row=3, column=0, sticky="nesw")
    def executeTheCommand(cominput):
        ConsoleInput.delete(0, tk.END)
        if cominput == "version":
            comoutput = "PraktiCalc Console on PraktiCalc " + PraktiCalcVersion
        elif cominput == "help":
            comoutput = """PraktiCalc Console Help
***********************
This console was mainly created for debugging purposes.
Available Commands:
exit: exits the program
clear: clears the output
function(<function>: executes a function in the program
system(<command>: executes a system command and prints the output
varget(<variable>: shows the value of the given variable
aboutwindow: opens console about window

Useful Tips:
- don't close brackets
- use the system command with caution
- don't use sudo with the system command, use run0 instead
- the console is not interactive, it prints the output after processing
- there is a Minecraft reference hidden in the console
"""
        elif cominput == "/toggledownfall":
            comoutput = "Toggled downfall"
        elif cominput.startswith("function("):
            cominput = cominput[9:]
            if cominput in globals() and callable(globals()[cominput]):
                globals()[cominput]()
                comoutput = "Function executed"
            else:
                comoutput = "[!] Unknown function"
        elif cominput.startswith("system("):
            cominput = cominput[7:]
            comoutput = subprocess.getoutput(cominput)
        elif cominput.startswith("varget("):
            cominput = cominput[7:]
            if cominput in globals():
                comoutput = globals()[cominput]
            else:
                comoutput = "[!] Unknown variable"
        elif cominput == "clear":
            ConsoleOutput.delete("1.0", tk.END)
            comoutput = ""
        elif cominput == "aboutwindow":
            comoutput = "opening console about window"
            ConsoleAbout()
        elif cominput == "exit":
            MainWindow.destroy()
        else:
            comoutput = "[X] Unknown command"
        ConsoleOutput.insert(tk.END, str(comoutput) + "\n")
    def ConsoleEnterKey(event):
        global cominput
        ConsoleKey = event.keysym
        if ConsoleKey == "Return":
            executeTheCommand(ConsoleInput.get())
    ConsoleWindow = tk.Toplevel(MainWindow)
    ConsoleWindow.title("PraktiCalc Console")
    ConsoleWindow.config(bg="black")
    ConsoleWindow.rowconfigure(0, weight=1)
    ConsoleWindow.columnconfigure(0, weight=1)
    ConsoleWindow.columnconfigure(1, weight=1)
    ConsoleWindow.columnconfigure(2, weight=1)
    ConsoleWindow.bind("<Key>", ConsoleEnterKey)
    ConsoleOutput = tk.Text(ConsoleWindow, bg="black", fg="white")
    ConsoleInputLabel = tk.Label(ConsoleWindow, text="INPUT: ", bg="black", fg="white")
    ConsoleInput = tk.Entry(ConsoleWindow, bg="black", fg="white")
    ConsoleExecuteButton = tk.Button(ConsoleWindow, text="--^", bg="black", fg="white", command=lambda: executeTheCommand(ConsoleInput.get()))
    ConsoleOutput.grid(row=0, column=0, columnspan=3, sticky="nesw")
    ConsoleInputLabel.grid(row=1, column=0, sticky="ew")
    ConsoleInput.grid(row=1, column=1, sticky="ew")
    ConsoleExecuteButton.grid(row=1, column=2, sticky="ew", pady=2, padx=2)
    ConsoleInput.focus_set()
MainWindow.rowconfigure(0, weight=1)
MainWindow.columnconfigure(0, weight=1)
changeTheme(MainWindow)
WindowFrame = ttk.Frame(MainWindow)
for colrow in range(5):
    WindowFrame.rowconfigure(colrow, weight=1, uniform="buttons")
    WindowFrame.columnconfigure(colrow, weight=1, uniform="buttons")
WindowFrame.rowconfigure(5, weight=1)
Outputframe = ttk.Frame(WindowFrame, borderwidth=1, relief="sunken")
Output = ttk.Label(Outputframe, text="0")
# Buttons
PlusButton = ttk.Button(WindowFrame, text="+", command=lambda: processOperator("+"))
MinusButton = ttk.Button(WindowFrame, text="-", command=lambda: processOperator("-"))
MultiplyButton = ttk.Button(WindowFrame, text="x", command=lambda: processOperator("*"))
DivideButton = ttk.Button(WindowFrame, text="÷", command=lambda: processOperator("/"))
SevenButton = ttk.Button(WindowFrame, text="7", command=lambda: processNumber("7"))
EightButton = ttk.Button(WindowFrame, text="8", command=lambda: processNumber("8"))
NineButton = ttk.Button(WindowFrame, text="9", command=lambda: processNumber("9"))
CEButton = ttk.Button(WindowFrame, text="CE", command=clear)
FourButton = ttk.Button(WindowFrame, text="4", command=lambda: processNumber("4"))
FiveButton = ttk.Button(WindowFrame, text="5", command=lambda: processNumber("5"))
SixButton = ttk.Button(WindowFrame, text="6", command=lambda: processNumber("6"))
CommaButton = ttk.Button(WindowFrame, text=",", command=comma)
OneButton = ttk.Button(WindowFrame, text="1", command=lambda: processNumber("1"))
TwoButton = ttk.Button(WindowFrame, text="2", command=lambda: processNumber("2"))
ThreeButton = ttk.Button(WindowFrame, text="3", command=lambda: processNumber("3"))
EqualButton = ttk.Button(WindowFrame, text="=", command=calc)
InfoButton = ttk.Button(WindowFrame, text="i", command=info)
ZeroButton = ttk.Button(WindowFrame, text="0", command=zero)
ExitButton = ttk.Button(WindowFrame, text="X", command=xquit)
Status = ttk.Label(WindowFrame, text="")
StatusDecoration = ttk.Label(WindowFrame, text="")
NewStatusDecoration = ttk.Separator(WindowFrame, orient="horizontal")
if WingWebDings == True:
    SettingsButton = ttk.Button(WindowFrame, text="@", command=Settings, style="Webdings.TButton")
    BackspaceButton = ttk.Button(WindowFrame, text="Õ", command=Backspace, style="Wingdings.TButton")
    HistoryButton = ttk.Button(WindowFrame, text="0", command=History, style="Wingdings.TButton")
else:
    SettingsButton = ttk.Button(WindowFrame, text="🔧", command=Settings)
    BackspaceButton = ttk.Button(WindowFrame, text="<", command=Backspace)
    HistoryButton = ttk.Button(WindowFrame, text="📜", command=History)
MButton = ttk.Button(WindowFrame, text="±", command=minus)
Checkb = ttk.Button(MainWindow, text="Check", command=xcheck) # some debug thing
sqrtButton = ttk.Button(WindowFrame, text="√", command=rooty)
More = ttk.Button(WindowFrame, text="...", command=More)
WindowFrame.grid(row=0, column=0, sticky="nesw")
Outputframe.grid(row=0, column=0, columnspan=4, sticky="nesw")
Output.pack(pady=1)
PlusButton.grid(row=1, column=1, sticky="nesw")
MinusButton.grid(row=1, column=2, sticky="nesw")
MultiplyButton.grid(row=1, column=3, sticky="nesw")
DivideButton.grid(row=1, column=4, sticky="nesw")
SevenButton.grid(row=2, column=1, sticky="nesw")
EightButton.grid(row=2, column=2, sticky="nesw")
NineButton.grid(row=2, column=3, sticky="nesw")
CEButton.grid(row=2, column=4, sticky="nesw")
FourButton.grid(row=3, column=1, sticky="nesw")
FiveButton.grid(row=3, column=2, sticky="nesw")
SixButton.grid(row=3, column=3, sticky="nesw")
CommaButton.grid(row=5, column=3, sticky="nesw")
OneButton.grid(row=4, column=1, sticky="nesw")
TwoButton.grid(row=4, column=2, sticky="nesw")
ThreeButton.grid(row=4, column=3, sticky="nesw")
EqualButton.grid(row=5, column=4, sticky="nesw")
InfoButton.grid(row=1, column=0, sticky="nesw")
ZeroButton.grid(row=5, column=1, columnspan=2, sticky="nesw")
MButton.grid(row=4, column=4, sticky="nesw")
sqrtButton.grid(row=3, column=4, sticky="nesw")
ExitButton.grid(row=5, column=0, sticky="nesw")
Status.grid(row=7, column=0, columnspan=5, sticky="nesw")
# StatusDecoration.grid(row=6, column=0, columnspan=5, sticky="nesw")
NewStatusDecoration.grid(row=6, column=0, columnspan=5, sticky="nesw", pady=2)
SettingsButton.grid(row=2, column=0, sticky="nesw")
BackspaceButton.grid(row=0, column=4, sticky="nesw")
HistoryButton.grid(row=4, column=0, sticky="nesw")
MainWindow.bind("<Key>", KeyPress)
More.grid(row=3, column=0, sticky="nesw")
if debug == True:
    Checkb.grid(row=1, column=0, sticky="nesw")
MainWindow.geometry("250x250")
MainWindow.mainloop()
