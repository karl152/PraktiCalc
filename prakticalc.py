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
from simpleeval import SimpleEval
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
import math

# variables
CLIHelp = "--help" in sys.argv
CLIVersion = "--version" in sys.argv
PraktiCalcVersion = "1.4"
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
--big: start with bigger main window
--debug: add a test button for debugging
--nodpiawareness: disable Windows DPI Awareness
--dark: enable dark mode by default
--console: show console for debugging
--equilux: set the dark theme to equilux
--help: display this help text and exit
--version: display version and exit""")
    else:
        print("PraktiCalc " + PraktiCalcVersion + " CLI Options")
        print("--big     | start with bigger main window")
        print("--debug   | add a test button for debugging")
        print("--dark    | enable dark mode by default")
        print("--console | show console for debugging")
        print("--breeze  | set the light theme to breeze")
        print("--yaru    | set the light theme to yaru")
        print("--equilux | set the dark theme to equilux")
        print("--help    | display this help text and exit")
        print("--version | display version and exit")
    sys.exit(0)
if CLIVersion == True:
    if platform.system() == "Windows":
        messagebox.showinfo("PraktiCalc " + PraktiCalcVersion, "PraktiCalc " + PraktiCalcVersion)
    else:
        print("PraktiCalc " + PraktiCalcVersion)
    sys.exit(0)

calculate = SimpleEval()
calculate.functions["sqrt"] = math.sqrt

def testPyInstallerOneFile():
    try:
        print(sys._MEIPASS)
        return True
    except:
        return False

RunningAsOneFileExe = testPyInstallerOneFile()

# ttkthemes directory workaround for AppImage
if os.path.exists("./usr/share/tcltk/ttkthemes"):
    # If started as AppImage:
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
big = "--big" in sys.argv
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
DarkMode = "--dark" in sys.argv
debug = "--debug" in sys.argv
historylist = []
FinalResult = 0
aFinalResult = 0
DecimalNumber = 0
BinaryNumber = 0
HexadecimalNumber = 0
Calculation = "0"

# functions

# sets the theme for a given window
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
            style.configure("LargeUnicode.TButton", font=LargeUnicodeFont)
    elif theming == 1 or theming == 2:
        try:
            style = ThemedStyle(WindowName)
            style.theme_use(usedttktheme)
            style.configure("LargeUnicode.TButton", font=LargeUnicodeFont)
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
            style = ttk.Style()
            try:
                style.theme_use(usedttktheme)
            except:
                print("Using default ttk theme")
        try:
            style.configure("LargeUnicode.TButton", font=LargeUnicodeFont)
        except:
            print("Unable to increase font size of some buttons")

# processes the number zero, which is a special case and seperate
def zero() :
    global Calculation
    if Calculation == "0":
        pass
    else:
        Calculation += "0"
    updateDisplay()

# resets the calculator main window
def clear() :
    global Calculation
    Calculation = "0"
    updateDisplay()

# does the actual calculation, used to include 171 if-statements
def calc() :
    global Calculation, historylist
    if len(historylist) >= 16:
        historylist.pop(0)
    TheCalc = Calculation.replace("\u221a", "sqrt")
    TheCalc = TheCalc.replace("x", "*")
    try:
        Result = calculate.eval(TheCalc)
    except ZeroDivisionError:
        showError("Division by zero")
    except Exception:
        showError("Error, please check your input for mistakes")
    if str(Result).endswith(".0"):
        Result = str(Result)[:-2]
    else:
        Result = str(Result)
    historylist.append(f"{Calculation}={Result}")
    Output.config(text=Result)

# processes keyboard input
def KeyPress(event):
    Key = event.keysym
    # print(Key)
    Keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "plus", "minus", "asterisk", "slash", "comma", "parenleft", "parenright"]
    if Key in Keys:
        appendToCalculation(Key)
    elif Key == "0":
        zero()
    elif Key == "equal" or Key == "Return":
        calc()
    elif Key == "h" or Key == "H":
        History()
    elif Key == "c" or Key == "C":
        clear()
    elif Key == "i":
        CustomInfo()
    elif Key == "s" or Key == "S":
        Settings()
    elif Key == "BackSpace":
        Backspace()

# append a character to the Calculation string
def appendToCalculation(char):
    global Calculation
    char = char.replace("plus", "+")
    char = char.replace("minus", "-")
    char = char.replace("asterisk", "x")
    char = char.replace("slash", "/")
    char = char.replace("comma", ".")
    char = char.replace("parenleft", "(")
    char = char.replace("parenright", ")")
    if Calculation == "0":
        Calculation = char
    else:
        Calculation += char
    updateDisplay()

# settings window
def Settings() :
    global SettingsWindow, DarkMode, DarkModeToggle, MsgBoxStyles, CurrentMsgBoxStyle, MsgBoxStyleSelect
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
    DarkModeToggle = ttk.Checkbutton(SettingsWindowFrame, text="Dark Mode", command=ChangeDarkMode, variable=DarkModeTkVar)
    MsgBoxStyleFrame = ttk.LabelFrame(SettingsWindowFrame, text="Messagebox Style")
    MsgBoxStyleFrame.columnconfigure(0, weight=1)
    MsgBoxStyleSelect = ttk.Combobox(MsgBoxStyleFrame, values=MsgBoxStyles)
    MsgBoxStyleSelect.current(CurrentMsgBoxStyle)
    SettingsOKButton = ttk.Button(SettingsWindowFrame, text="OK", command=loadTheme)
    SettingsWindowFrame.grid(row=0, column=0, sticky="nesw")
    DarkModeToggle.grid(row=2, column=0, sticky="w", padx=10)
    MsgBoxStyleFrame.grid(row=3, column=0, sticky="ew", padx=10)
    MsgBoxStyleSelect.grid(row=0, column=0, sticky="ew")
    SettingsOKButton.grid(row=4, column=0, sticky="ew", padx=10, pady=10)

# saves the selected theme choice in the settigns window
def loadTheme():
    global SettingsWindow, CurrentMsgBoxStyle, MsgBoxStyleSelect
    CurrentMsgBoxStyle = MsgBoxStyleSelect.current()
    # print(CurrentMsgBoxStyle)
    SettingsWindow.destroy()

# toggled dark mode
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

# info window
def CustomInfo() :
    global CustomInfox
    infotext = "PraktiCalc\nVersion " + PraktiCalcVersion + "\nrunning on Python "+ platform.python_version() + "\nLicensed under GPLv3\nread more at https://www.gnu.org/licenses/"
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
                subprocess.Popen(["wscript", VBSInfoPath, PraktiCalcVersion, pyver])
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

# closes custom info window
def closeCustomInfo() :
    global CustomInfox
    CustomInfox.destroy()

# shows error dialogs
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

# closes custom error dialogs
def closeError():
    global ErrorWindow
    ErrorWindow.destroy()

# help GUI
def helpGUI():
    showError("Not implemented")

# backspace button
def Backspace() :
    global Calculation
    if Calculation == "0":
        pass
    elif len(Calculation) <= 1:
        Calculation = "0"
    else:
        Calculation = Calculation[:-1]
    updateDisplay()

# updates output
def updateDisplay() :
    global Calculation
    Output.config(text=Calculation)

# history window
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

# window for additional calculating stuff, cuttently only with a decimal number converter
def More() :

    # processes the enter key inside the window
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

# converts decimal numbers into binary and hexadecimal
# still called "paste" because it used to take the decimal number from the Windows clipboard
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

# copies the binary output
def copybin() :
    global BinaryNumber, MainWindow
    MainWindow.clipboard_clear()
    MainWindow.clipboard_append(BinaryNumber)
    MainWindow.update()

# copies the hexadecimal output
def copyhex() :
    global HexadecimalNumber, MainWindow
    MainWindow.clipboard_clear()
    MainWindow.clipboard_append(HexadecimalNumber)
    MainWindow.update()

# clears the history
def clearHistory() :
    global HistoryX
    historylist.clear()
    HistoryX.destroy()
    History()

# debug function to print some variables
def xcheck() :
    print("Stage: " + str(Stage))
    print("Input1: " + str(Input1))
    print("Input2: " + str(Input2))
    print("Operator: " + str(Operator))
    print("FinalResult: " + str(FinalResult))
    print("aFinalResult: " + str(aFinalResult))
    print("____________________________")

# quits the program
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
else:
    LargeUnicodeFont = font.Font(family="TkDefaultFont", size=14)
DarkModeTkVar = tk.BooleanVar(value=DarkMode)
MainWindow.config(width=256, height=315)
if console == True:

    # shows console about window
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

    # interpretes and executed a given command in the console
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

    # processes the enter key in the console
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
PlusButton = ttk.Button(WindowFrame, text="+", command=lambda: appendToCalculation("plus"))
MinusButton = ttk.Button(WindowFrame, text="-", command=lambda: appendToCalculation("minus"))
MultiplyButton = ttk.Button(WindowFrame, text="x", command=lambda: appendToCalculation("asterisk"))
DivideButton = ttk.Button(WindowFrame, text="÷", command=lambda: appendToCalculation("slash"))
SevenButton = ttk.Button(WindowFrame, text="7", command=lambda: appendToCalculation("7"))
EightButton = ttk.Button(WindowFrame, text="8", command=lambda: appendToCalculation("8"))
NineButton = ttk.Button(WindowFrame, text="9", command=lambda: appendToCalculation("9"))
CEButton = ttk.Button(WindowFrame, text="CE", command=clear)
FourButton = ttk.Button(WindowFrame, text="4", command=lambda: appendToCalculation("4"))
FiveButton = ttk.Button(WindowFrame, text="5", command=lambda: appendToCalculation("5"))
SixButton = ttk.Button(WindowFrame, text="6", command=lambda: appendToCalculation("6"))
CommaButton = ttk.Button(WindowFrame, text=",", command=lambda: appendToCalculation("comma"))
OneButton = ttk.Button(WindowFrame, text="1", command=lambda: appendToCalculation("1"))
TwoButton = ttk.Button(WindowFrame, text="2", command=lambda: appendToCalculation("2"))
ThreeButton = ttk.Button(WindowFrame, text="3", command=lambda: appendToCalculation("3"))
EqualButton = ttk.Button(WindowFrame, text="=", command=calc)
InfoButton = ttk.Button(WindowFrame, text="i", command=CustomInfo)
ZeroButton = ttk.Button(WindowFrame, text="0", command=zero)
ExitButton = ttk.Button(WindowFrame, text="X", command=xquit)
if WingWebDings == True:
    SettingsButton = ttk.Button(WindowFrame, text="@", command=Settings, style="Webdings.TButton")
    BackspaceButton = ttk.Button(WindowFrame, text="Õ", command=Backspace, style="Wingdings.TButton")
    HistoryButton = ttk.Button(WindowFrame, text="0", command=History, style="Wingdings.TButton")
else:
    SettingsButton = ttk.Button(WindowFrame, text="\u26ed", command=Settings, style="LargeUnicode.TButton")
    BackspaceButton = ttk.Button(WindowFrame, text="\u232b", command=Backspace)
    HistoryButton = ttk.Button(WindowFrame, text="\u23f2", command=History, style="LargeUnicode.TButton")
HelpButton = ttk.Button(WindowFrame, text="?", command=helpGUI)
Checkb = ttk.Button(MainWindow, text="Check", command=xcheck) # some debug thing
sqrtButton = ttk.Button(WindowFrame, text="\u221a", command=lambda: appendToCalculation("\u221a" + "("))
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
HelpButton.grid(row=4, column=4, sticky="nesw")
sqrtButton.grid(row=3, column=4, sticky="nesw")
ExitButton.grid(row=5, column=0, sticky="nesw")
SettingsButton.grid(row=2, column=0, sticky="nesw")
BackspaceButton.grid(row=0, column=4, sticky="nesw")
HistoryButton.grid(row=4, column=0, sticky="nesw")
MainWindow.bind("<Key>", KeyPress)
More.grid(row=3, column=0, sticky="nesw")
if debug == True:
    Checkb.grid(row=1, column=0, sticky="nesw")
if big == False:
    MainWindow.geometry("250x250")
else:
    MainWindow.geometry("400x400")
MainWindow.mainloop()
