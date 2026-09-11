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
# PraktiCalc modules
from core import PraktiCalculator, Configuration
# other modules
import wx, wx.adv
from tkinter import messagebox, colorchooser
from pathlib import Path
from decimal import Decimal
import platform, subprocess, sys, shutil, math, time, configparser, importlib.util, webbrowser, zipfile, tempfile, hashlib, re, random, threading
if platform.system() == "Windows":
    import winreg, getpass
    from ctypes import wintypes
elif platform.system() == "Darwin":
    import plistlib

# VARIABLES
PraktiCalcVersion = "1.6"
MsgBoxStyles = ["Tkinter", "Alternative", "wxPython"]
if platform.system() == "Windows":
    import ctypes
    if shutil.which("wscript"):
        MsgBoxStyles.append("VBScript")
    if shutil.which("msg"):
        MsgBoxStyles.append("Windows Messaging Service")
    if "--allowShutdownDialog" in sys.argv:
        MsgBoxStyles.append("Windows Shutdown")
    if "--nodpiawareness" not in sys.argv:
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(2)
        except:
            pass
    if platform.release() == "Vista" or platform.release() == "7" or platform.release() == "8" or platform.release() == "8.1":
        WingWebDings = True
    else:
        WingWebDings = False
elif platform.system() == "Darwin":
    WingWebDings = False
    MsgBoxStyles.append("AppleScript")
else:
    WingWebDings = False
    AdditionalLinuxMsgBoxStyles = ["xmessage", "gxmessage", "wmessage", "yad", "kdialog", "zenity", "Xdialog", "notify-send"]
    for MsgBoxStyle in AdditionalLinuxMsgBoxStyles:
        if shutil.which(MsgBoxStyle):
            MsgBoxStyles.append(MsgBoxStyle)
if "--help" in sys.argv:
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
        print("--debug\t\tadd a test button for debugging")
        print("--console\tshow console for debugging")
        print("--help\t\tdisplay this help text and exit")
        print("--version\tdisplay version and exit")
    sys.exit(0)
if "--version" in sys.argv:
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
        PraktiCalcMacIconPath = (sys._MEIPASS + "/PraktiCalc-MacOS.png")
    PraktiCalcIconPath = (sys._MEIPASS + "/PraktiCalculator_icon.png")
    PraktiCalcIconMonoPath = (sys._MEIPASS + "/PraktiCalculator_icon.xbm")
    PraktiCalcIconMonoInvertedPath = (sys._MEIPASS + "/PraktiCalculator_icon_inverted.xbm")
    PythonPowerPath = (sys._MEIPASS + "/python-powered.png")
    WxPowerPath = (sys._MEIPASS + "/powered-by-wxwidgets-88x31.png")
    VBSInfoPath = (sys._MEIPASS + "/info.vbs")
    VBSErrorPath = (sys._MEIPASS + "/error.vbs")
else:
    if platform.system() == "Darwin":
        PraktiCalcMacIconPath = "PraktiCalc-MacOS.png"
    PraktiCalcIconPath = "PraktiCalculator_icon.png"
    PraktiCalcIconMonoPath = "PraktiCalculator_icon.xbm"
    PraktiCalcIconMonoInvertedPath = "PraktiCalculator_icon_inverted.xbm"
    PythonPowerPath = "python-powered.png"
    WxPowerPath = "powered-by-wxwidgets-88x31-blue.png"
    VBSInfoPath = "info.vbs"
    VBSErrorPath = "error.vbs"

debug = "--debug" in sys.argv

# CLASSES

# main window
class MainWindow(wx.Frame):
    def __init__(self, calculator, dialog, cfg):
        super().__init__(None, title="PraktiCalc")
        self.Menubar = wx.MenuBar()
        self.CalculatorMenu = wx.Menu()
        self.CalculatorMenuQuitItem = self.CalculatorMenu.Append(wx.NewIdRef(), "Quit\tQ")
        self.Bind(wx.EVT_MENU, lambda _: self.Close(), self.CalculatorMenuQuitItem)
        self.ToolMenu = wx.Menu()
        self.ToolMenuHistoryItem = self.ToolMenu.Append(wx.NewIdRef(), "History\tH")
        self.ToolMenuSettingsItem = self.ToolMenu.Append(wx.NewIdRef(), "Settings\tS")
        self.ToolMenu.AppendSeparator()
        self.ToolMenuExtensionsItem = self.ToolMenu.Append(wx.NewIdRef(), "Extensions\tX")
        self.Bind(wx.EVT_MENU, lambda _: HistoryWindow(self, calculator), self.ToolMenuHistoryItem)
        self.Bind(wx.EVT_MENU, lambda _: SettingsWindow(self, calculator, cfg), self.ToolMenuSettingsItem)
        self.Bind(wx.EVT_MENU, lambda _: ExtensionWindow(self, calculator, dialog, cfg), self.ToolMenuExtensionsItem)
        self.HelpMenu = wx.Menu()
        self.HelpMenuAboutItem = self.HelpMenu.Append(wx.NewIdRef(), "About\tI")
        self.Bind(wx.EVT_MENU, lambda _: dialog.info(self), self.HelpMenuAboutItem)
        self.MemoryDisplay = wx.Menu()
        self.FloatingMemoryDisplay = wx.Menu()
        self.MemoryDisplayCommands = {
            "Set memory": lambda _: self.setMemory(calculator),
            "Get memory": lambda _: self.getMemory(calculator, cfg),
            "Add to memory": lambda _: self.addToMemory(calculator, dialog),
            "Subtract from memory": lambda _: self.subtractFromMemory(calculator),
            "Append to memory": lambda _: self.appendToMemory(calculator),
            "Clear memory": lambda _: self.clearMemory(calculator)
            }
        self.MemoryItems = []
        for cmd in self.MemoryDisplayCommands:
            for menu in (self.MemoryDisplay, self.FloatingMemoryDisplay):
                CurrentItem = menu.Append(wx.NewIdRef(), cmd)
                self.Bind(wx.EVT_MENU, self.MemoryDisplayCommands.get(cmd), CurrentItem)
        MenubarLabels = ("Calculator", "Tools", "Help", "M: 0")
        for i, menu in enumerate((self.CalculatorMenu, self.ToolMenu, self.HelpMenu, self.MemoryDisplay)):
            self.Menubar.Append(menu, MenubarLabels[i])
        self.SetMenuBar(self.Menubar)
        self.panel = wx.Panel(self)
        # WIDGETS
        self.Output = wx.TextCtrl(self.panel, style=wx.TE_READONLY)
        self.Output.SetValue("0")
        AppendButtons = ["+", "-", "(", ")", ".", "%"] # 5-10
        for i in range(1, 10):
            AppendButtons.append(str(i)) # 11-19
        FurtherAppendButtons = {
            "x": "*", # 20
            "\u00f7": "/", # 21
            "\u221a": "\u221a(", # 22
            "x^y": "^", # 23
            "!": "fact(" # 24
            }
        ButtonSpecs = {
            "CE": lambda _: self.clear(calculator, cfg), # 0
            "=": lambda _: self.calculate(self, calculator, dialog, cfg), # 1
            "\u2398": lambda _: self.copyResult(), # 2
            "\u232b": lambda _: self.backspace(calculator, cfg), # 3
            "0": lambda _: self.zero(calculator, cfg) # 4
            }
        for btn in AppendButtons:
            ButtonSpecs[btn] = lambda _, b=btn: self.append(b, calculator, cfg)
        for btn in FurtherAppendButtons:
            ButtonSpecs[btn] = lambda _, b=btn: self.append(FurtherAppendButtons.get(b), calculator, cfg)
        self.Buttons = []
        for i, item in enumerate(ButtonSpecs):
            self.Buttons.append(wx.Button(self.panel, label=item))
            self.Buttons[i].Bind(wx.EVT_BUTTON, ButtonSpecs.get(item))
        SinLogs = [[], [], [], ["ld", "ln", "lg"]]
        for i, sl in enumerate(("sin", "cos", "tan")):
            SinLogs[i].append(sl)
            SinLogs[i].append("a"+sl)
            SinLogs[i].append(sl+"h")
            SinLogs[i].append("a"+sl+"h")
        SinLogTanMenus = []
        for i in range(4):
            SinLogTanMenus.append(wx.Menu())
        for i, menu in enumerate(SinLogTanMenus):
            for label in SinLogs[i]:
                self.Bind(wx.EVT_MENU, lambda _, l=label: self.append(l+"(", calculator, cfg), menu.Append(wx.NewIdRef(), label))
        for i, label in enumerate(("sin", "cos", "tan", "log")):
            self.Buttons.append(Menubutton(self.panel, label, SinLogTanMenus[i])) # 25-28
        self.MemoryMenu = wx.Menu()
        for cmd in self.MemoryDisplayCommands:
            self.Bind(wx.EVT_MENU, self.MemoryDisplayCommands.get(cmd), self.MemoryMenu.Append(wx.NewIdRef(), cmd.split()[0]))
        self.Buttons.append(Menubutton(self.panel, "M", self.MemoryMenu)) # 29
        self.KonstantMenu = wx.Menu()
        for cmd in ("\u03c0", "e"):
            self.Bind(wx.EVT_MENU, lambda _, c=cmd: self.append(c, calculator, cfg), self.KonstantMenu.Append(wx.NewIdRef(), cmd))
        self.Buttons.append(Menubutton(self.panel, "\u03c0", self.KonstantMenu)) # 30
        # Sizer
        self.sizer = wx.GridBagSizer()
        self.sizer.Add(self.Output, pos=(0, 0), span=(1, 3), flag=wx.EXPAND)
        for i in range(3, 5):
            self.sizer.Add(self.Buttons[i-1], pos=(0, i), flag=wx.EXPAND)
        buttons = (
            (29, 7, 8, 5, 0),
            (17, 18, 19, 6, 23),
            (14, 15, 16, 20, 22),
            (11, 12, 13, 21, 10),
            (None, None, 9, 1, 24),
            (25, 26, 27, 28, 30)
            )
        for row, buttonrow in enumerate(buttons):
            for col, button in enumerate(buttonrow):
                if button != None:
                    self.sizer.Add(self.Buttons[button], pos=(row+1, col), flag=wx.EXPAND)
        self.sizer.Add(self.Buttons[4], pos=(5, 0), span=(1, 2), flag=wx.EXPAND)
        for colrow in range(5):
            self.sizer.AddGrowableCol(colrow)
            self.sizer.AddGrowableRow(colrow)
        for i in range(2):
            self.sizer.AddGrowableRow(i+5)
        self.panel.SetSizerAndFit(self.sizer)
        self.Fit()
        self.Output.Bind(wx.EVT_KEY_DOWN, lambda event: self.KeyPress(event, calculator, dialog))
        self.updateDisplay(calculator, cfg)
    def KeyPress(self, event, calculator, dialog): # processes keyboard input
        Key = event.GetKeyCode()
        if chr(Key) in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "e", "+", "-", "*", "/", "(", ")", ".", ",", "%", "!"]:
            self.append(chr(Key), calculator, cfg)
        else:
            Keys = {
                48: lambda: self.zero(calculator, cfg), # 0
                61: lambda: self.calculate(self, helper, calculator, dialog, cfg), # =
                13: lambda: self.calculate(self, calculator, dialog, cfg), # Return
                104: lambda: HistoryWindow(self, calculator), # h
                72: lambda: HistoryWindow(self, calculator),# H
                105: lambda: dialog.info(self), # i
                73: lambda: dialog.info(self), # I
                115: lambda: SettingsWindow(self, calculator, cfg), # s
                83: lambda: SettingsWindow(self, calculator, cfg), # S
                120: lambda: ExtensionWindow(self, calculator, dialog, cfg), # x
                88: lambda: ExtensionWindow(self, calculator, dialog, cfg), # X
                99: lambda: self.clear(calculator, cfg), # c
                67: lambda: self.clear(calculator, cfg), # C
                8: lambda: self.backspace(calculator, cfg), # Backspace
                109: self.toggleMemoryMenu, # m
                77: self.toggleMemoryMenu, # M
                113: self.Close, # q
                81: self.Close # Q
                }
            if "--debug" in sys.argv:
                Keys[68] = lambda: print(calculator.xcheck())
            run = Keys.get(Key)
            if run:
                run()
        event.Skip()
    def toggleMemoryMenu(self): # toggles the floating memory menu
        self.PopupMenu(self.FloatingMemoryDisplay, self.Buttons[18].GetPosition())
    def copyResult(self): # copies the result
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(wx.TextDataObject(self.Output.GetValue()))
            wx.TheClipboard.Close()
    def updateDisplay(self, calculator, cfg): # updates output
        if cfg.get("borderDisplay") == True:
            self.SetTitle(calculator.CalculationString)
        else:
            self.SetTitle("PraktiCalc")
        self.Output.SetValue(calculator.CalculationString)
        self.Output.SetFocus()
        self.Output.ShowPosition(self.Output.GetLastPosition())
    #  -#- the following methods call the calculator methods and update the display -#-
    def append(self, value, calculator, cfg):
        calculator.append(value)
        self.updateDisplay(calculator, cfg)
    def zero(self, calculator, cfg):
        calculator.zero()
        self.updateDisplay(calculator, cfg)
    def calculate(self, parent, calculator, dialog, cfg):
        try:
            calculator.calculate()
        except Exception as e:
            dialog.error(str(e), self)
        self.updateDisplay(calculator, cfg)
    def clear(self, calculator, cfg):
        calculator.clear()
        self.updateDisplay(calculator, cfg)
    def backspace(self, calculator, cfg):
        calculator.backspace()
        self.updateDisplay(calculator, cfg)
    def setMemory(self, calculator):
        calculator.setMemory()
        self.refreshMemoryDisplay(calculator)
    def getMemory(self, calculator, cfg):
        calculator.getMemory()
        self.updateDisplay(calculator, cfg)
    def appendToMemory(self, calculator):
        calculator.appendToMemory()
        self.refreshMemoryDisplay(calculator)
    def addToMemory(self, calculator, dialog):
        try:
            calculator.addToMemory()
        except Exception as e:
            dialog.error(str(e), self)
        self.refreshMemoryDisplay(calculator)
    def subtractFromMemory(self, calculator):
        calculator.subtractFromMemory()
        self.refreshMemoryDisplay(calculator)
    def clearMemory(self, calculator):
        calculator.clearMemory()
        self.refreshMemoryDisplay(calculator)
    def refreshMemoryDisplay(self, calculator):
        NewLabel = "M: " + calculator.Memory
        self.Menubar.SetMenuLabel(3, NewLabel)

# something that's a bit like ttk.Menubutton
class Menubutton(wx.Button):
    def __init__(self, parent, label, menu):
        super().__init__(parent, label=label)
        self.Bind(wx.EVT_BUTTON, lambda _: parent.PopupMenu(menu, self.GetPosition()))

# wx.StaticBox with wx.Choice
class ChoiceBox(wx.StaticBox):
    def __init__(self, parent, label, choices):
        super().__init__(parent, label=label)
        self.choice = wx.Choice(self, choices=choices)
        self.sizer = wx.GridBagSizer()
        self.sizer.AddGrowableCol(0)
        self.sizer.AddGrowableRow(0)
        self.sizer.Add(self.choice, pos=(0, 0), flag=wx.EXPAND | wx.RIGHT | wx.LEFT, border=5)
        self.sizer.Add(wx.StaticText(self), pos=(1, 0), flag=wx.BOTTOM, border=10)
        self.SetSizerAndFit(self.sizer)

# settings window
class SettingsWindow(wx.Frame):
    def __init__(self, parent, calculator, cfg):
        global MsgBoxStyles
        super().__init__(parent, title="Settings")
        self.panel = wx.Panel(self)
        self.Tabs = wx.Notebook(self.panel)
        self.AppearancePanel = wx.Panel(self.Tabs)
        self.BehaviorPanel = wx.Panel(self.Tabs)
        self.ConstantsPanel = wx.Panel(self.Tabs)
        # ---
        # Appearance
        self.BorderDisplayCheck = wx.CheckBox(self.AppearancePanel, label="Border display")
        self.BorderDisplayCheck.SetValue(bool(cfg.get("borderDisplay")))
        ColorBackendChoices = ["Tkinter", "wxPython (ColourDialog)", "wxPython (PyColourChooser)", "wxPython (CubeColourDialog)", "KDialog", "YAD", "Zenity"]
        self.ColorDialogBox = ChoiceBox(self.AppearancePanel, "Color dialog backend (WIP)", ColorBackendChoices)
        self.DialogBox = ChoiceBox(self.AppearancePanel, "Message dialog backend", MsgBoxStyles)
        self.DialogBox.choice.SetStringSelection(cfg.get("dialogStyle"))
        self.AppearanceSizer = wx.GridBagSizer(5)
        self.AppearanceSizer.AddGrowableCol(0)
        self.AppearanceSizer.Add(self.BorderDisplayCheck, pos=(0, 0), flag=wx.EXPAND)
        self.AppearanceSizer.Add(self.ColorDialogBox, pos=(1, 0), flag=wx.EXPAND)
        self.AppearanceSizer.Add(self.DialogBox, pos=(2, 0), flag=wx.EXPAND)
        self.AppearancePanel.SetSizerAndFit(self.AppearanceSizer)
        # Behavior
        self.AngleUnitBox = wx.RadioBox(self.BehaviorPanel, label="Angle unit", choices=["Degrees", "Radians", "Gradians"], majorDimension=1, style=wx.RA_SPECIFY_COLS)
        AngleUnits = {
            "deg": 0,
            "rad": 1,
            "grad": 2
            }
        self.RoundResultCheck = wx.CheckBox(self.BehaviorPanel, label="Round result")
        self.ShowTrailingDotZeroCheck = wx.CheckBox(self.BehaviorPanel, label="Show trailing .0")
        self.AngleUnitBox.SetSelection(AngleUnits.get(cfg.get("angleUnit")))
        self.RoundResultCheck.SetValue(bool(cfg.get("roundResult")))
        self.ShowTrailingDotZeroCheck.SetValue(bool(cfg.get("showTrailing0")))
        self.BehaviorSizer = wx.GridBagSizer(5)
        self.BehaviorSizer.AddGrowableCol(0)
        self.BehaviorSizer.Add(self.AngleUnitBox, pos=(0, 0), flag=wx.EXPAND)
        self.BehaviorSizer.Add(self.RoundResultCheck, pos=(1, 0), flag=wx.EXPAND)
        self.BehaviorSizer.Add(self.ShowTrailingDotZeroCheck, pos=(2, 0), flag=wx.EXPAND)
        if platform.system() == "Windows":
            self.ExtensionLocationBox = wx.RadioBox(self.BehaviorPanel, label="Extension location", choices=["AppData/Local", "AppData/Roaming"], majorDimension=1, style=wx.RA_SPECIFY_COLS)
            self.ExtensionLocationBox.SetSelection(1)
            self.BehaviorSizer.Add(self.ExtensionLocationBox, pos=(3, 0), flag=wx.EXPAND)
        self.BehaviorPanel.SetSizerAndFit(self.BehaviorSizer)
        # Constants
        self.ConstantsList = wx.adv.EditableListBox(self.ConstantsPanel, label="Constants")
        self.ConstantsList.SetStrings(["pi\t" + str(math.pi), "e\t" + str(math.e)])
        self.ConstantsSizer = wx.GridBagSizer()
        self.ConstantsSizer.AddGrowableCol(0)
        self.ConstantsSizer.AddGrowableRow(0)
        self.ConstantsSizer.Add(self.ConstantsList, pos=(0, 0), flag=wx.EXPAND)
        self.ConstantsPanel.SetSizerAndFit(self.ConstantsSizer)
        # ---
        self.Tabs.AddPage(self.AppearancePanel, "Appearance")
        self.Tabs.AddPage(self.BehaviorPanel, "Behavior")
        self.Tabs.AddPage(self.ConstantsPanel, "Constants")
        self.OKButton = wx.Button(self.panel, label="OK")
        self.OKButton.SetBitmapLabel(wx.ArtProvider.GetBitmap(wx.ART_FLOPPY, wx.ART_BUTTON, (16, 16)))
        self.OKButton.Bind(wx.EVT_BUTTON, lambda _: self.applySettings(parent, cfg, calculator))
        self.ResetButton = wx.Button(self.panel, label="Reset")
        self.ResetButton.SetBitmapLabel(wx.ArtProvider.GetBitmap(wx.ART_DELETE, wx.ART_BUTTON, (16, 16)))
        self.ResetButton.Bind(wx.EVT_BUTTON, lambda _: self.reset(parent, cfg))
        self.sizer = wx.GridBagSizer()
        self.sizer.AddGrowableRow(0)
        self.sizer.Add(self.Tabs, pos=(0, 0), span=(1, 2), flag=wx.EXPAND)
        self.sizer.Add(self.OKButton, pos=(1, 0), flag=wx.ALL, border=5)
        self.sizer.Add(self.ResetButton, pos=(1, 1), flag=wx.ALIGN_LEFT | wx.ALL, border=5)
        self.sizer.AddGrowableCol(1)
        self.panel.SetSizerAndFit(self.sizer)
        self.Fit()
        self.Show()
    def applySettings(self, parent, cfg, calculator): # saves the selected theme choice in the settigns window
        AngleUnits = {
            0: "deg",
            1: "rad",
            2: "grad"
            }
        cfg.set("borderDisplay", self.BorderDisplayCheck.GetValue())
        cfg.set("roundResult", self.RoundResultCheck.GetValue())
        cfg.set("showTrailing0", self.ShowTrailingDotZeroCheck.GetValue())
        cfg.set("angleUnit", AngleUnits.get(self.AngleUnitBox.GetSelection()))
        cfg.set("dialogStyle", self.DialogBox.choice.GetStringSelection())
        calculator.updateFromSettings(cfg)
        parent.updateDisplay(calculator, cfg)
        self.Close()
    def reset(self, parent, cfg): # resets the settings
        cfg.reset()
        messagebox.showinfo(title="Resetting settings", message="The settings have been reset and PraktiCalc will now close.\nDefault settings will be loaded when opening it again.")
        parent.Close()

# custom info dialog
class CustomInfoDialog(wx.Dialog):
    def __init__(self, parent, infotext):
        super().__init__(parent, title="About PraktiCalc")
        self.panel = wx.Panel(self)
        self.InfoBox = wx.StaticBox(self.panel, label="[i]")
        if "--debug" in sys.argv:
            self.InfoBox.SetLabel("[i] <-> RUNNING IN DEBUG MODE")
        self.LogoBitmap = wx.StaticBitmap(self.InfoBox, bitmap=wx.Bitmap(PraktiCalcIconPath))
        self.StaticInfoText = wx.StaticText(self.InfoBox, label=infotext + "\n")
        self.InfoBoxSizer = wx.GridBagSizer()
        self.InfoBoxSizer.Add(self.LogoBitmap, pos=(0, 0), flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        self.InfoBoxSizer.Add(self.StaticInfoText, pos=(1, 0), flag=wx.ALL, border=5)
        self.InfoBox.SetSizerAndFit(self.InfoBoxSizer)
        self.PythonPoweredBitmap = wx.Bitmap(PythonPowerPath, wx.BITMAP_TYPE_PNG)
        self.PythonPoweredButton = wx.BitmapButton(self.panel, bitmap=self.PythonPoweredBitmap)
        self.PythonPoweredButton.Bind(wx.EVT_BUTTON, lambda _: webbrowser.open_new_tab("https://www.python.org/"))
        self.WxPoweredBitmap = wx.Bitmap(WxPowerPath, wx.BITMAP_TYPE_PNG)
        self.WxPoweredButton = wx.BitmapButton(self.panel, bitmap=self.WxPoweredBitmap)
        self.WxLinkMenu = wx.Menu()
        self.Bind(wx.EVT_MENU, lambda _: webbrowser.open_new_tab("https://wxpython.org/"), self.WxLinkMenu.Append(wx.NewIdRef(), "wxPython"))
        self.Bind(wx.EVT_MENU, lambda _: webbrowser.open_new_tab("https://wxwidgets.org/"), self.WxLinkMenu.Append(wx.NewIdRef(), "wxWidgets"))
        self.WxPoweredButton.Bind(wx.EVT_BUTTON, lambda _: self.PopupMenu(self.WxLinkMenu, self.WxPoweredButton.GetPosition()))
        self.OKButton = wx.Button(self.panel, label="OK")
        self.OKButton.Bind(wx.EVT_BUTTON, lambda _: self.Close())
        self.OKButton.SetFocus()
        self.sizer = wx.GridBagSizer(5)
        self.sizer.Add(self.InfoBox, pos=(0, 0), span=(1, 2), flag=wx.EXPAND | wx.ALL, border=5)
        self.sizer.Add(self.PythonPoweredButton, pos=(1, 0), flag=wx.ALL, border=5)
        self.sizer.Add(self.WxPoweredButton, pos=(1, 1), flag=wx.ALL, border=5)
        self.sizer.Add(self.OKButton, pos=(1, 2), flag=wx.ALIGN_BOTTOM | wx.ALL, border=5)
        self.panel.SetSizerAndFit(self.sizer)
        self.Fit()

# info and error dialogs
class Dialog:
    def __init__(self, cfg):
        self.ConfigurationStorage = cfg
    def info(self, parent): # shows info dialogs
        infotext = f"""PraktiCalc - a practical calculator
Version {PraktiCalcVersion}
Copyright \u00a9 2024-2026 Karl Wesseler
Running on Python {platform.python_version()} / wxPython {wx.VERSION_STRING}
Licensed under the GPLv3"""
        dlgStyle = self.ConfigurationStorage.get("dialogStyle")
        if dlgStyle == "Tkinter":
            messagebox.showinfo("About PraktiCalc", infotext)
        elif dlgStyle == "Alternative":
            CustomInfoDialog(parent, infotext).Show()
        elif dlgStyle == "wxPython":
            InfoData = wx.adv.AboutDialogInfo()
            InfoData.Name = "PraktiCalc"
            InfoData.SetIcon(wx.Icon(PraktiCalcIconPath, wx.BITMAP_TYPE_PNG))
            InfoData.Version = PraktiCalcVersion
            InfoData.Description = "A practical calculator"
            InfoData.Copyright = "\u00a9 2024-2026 Karl Wesseler"
            #InfoData.Developers = ["Karl Wesseler"]
            wx.adv.AboutBox(InfoData)
        else:
            if platform.system() == "Windows":
                pyver = platform.python_version()
                styles = {
                    "VBScript": lambda: subprocess.Popen(["wscript", VBSInfoPath, PraktiCalcVersion, pyver, str(wx.VERSION_STRING), str(0)]),
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
                    "xmessage": lambda: subprocess.Popen(["xmessage", "-title", "About PraktiCalc", "-buttons", "OK", "-default", "OK", infotext.replace("\u00a9", "(C)")]),
                    "gxmessage": lambda: subprocess.Popen(["gxmessage", "-title", "About PraktiCalc", "-buttons", "OK", "-default", "OK", infotext]),
                    "wmessage": lambda: subprocess.Popen(["wmessage", "-title", "About PraktiCalc", "-buttons", "OK", "-default", "OK", infotext]),
                    "yad": lambda: subprocess.Popen(["yad", "--title=About PraktiCalc", "--info", "--image=" + PraktiCalcIconPath, "--button=OK", "--text=" + infotext]),
                    "kdialog": lambda: subprocess.Popen(["kdialog", "--title=About PraktiCalc", "--msgbox", infotext]),
                    "zenity": lambda: subprocess.Popen(["zenity", "--title=About PraktiCalc", "--info", "--icon=" + PraktiCalcIconPath, "--text=" + infotext]),
                    "AppleScript": lambda: subprocess.run(["osascript", "-e", f'display dialog "{infotext}" with icon POSIX file "{PraktiCalcIconPath}" with title "About PraktiCalc"']),
                    "Xdialog": lambda: subprocess.Popen(["Xdialog", "--title=About PraktiCalc", "--msgbox", infotext.replace("\u00a9", "(C)"), "10", "40"]),
                    "notify-send": lambda: subprocess.Popen(["notify-send", "About PraktiCalc", "--icon=de.karl_52.PraktiCalc", "--action=OK", infotext]),
                    }
                opendialog = styles.get(self.ConfigurationStorage.get("dialogStyle"))
                if opendialog:
                    opendialog()
                else:
                    print("ERROR: Unknown Message Box Style")
    def error(self, message, parent): # shows error dialogs
        dlgStyle = self.ConfigurationStorage.get("dialogStyle")
        if dlgStyle == "Tkinter":
            messagebox.showerror("Error", message)
        elif dlgStyle == "Alternative":
            ErrorWindow = wx.Dialog(parent, title="Error")
            ErrorWindow.panel = wx.Panel(ErrorWindow)
            ErrorWindow.ErrorBox = wx.StaticBox(ErrorWindow.panel, label="[X]")
            ErrorWindow.ErrorText = wx.StaticText(ErrorWindow.ErrorBox, label=message+"\n")
            ErrorWindow.BoxSizer = wx.GridBagSizer()
            ErrorWindow.BoxSizer.Add(ErrorWindow.ErrorText, pos=(0, 0), flag=wx.ALL, border=5)
            ErrorWindow.ErrorBox.SetSizerAndFit(ErrorWindow.BoxSizer)
            ErrorWindow.OKButton = wx.Button(ErrorWindow.panel, label="OK")
            ErrorWindow.OKButton.Bind(wx.EVT_BUTTON, lambda _: ErrorWindow.Close())
            ErrorWindow.OKButton.SetFocus()
            ErrorWindow.sizer = wx.GridBagSizer(5)
            ErrorWindow.sizer.Add(ErrorWindow.ErrorBox, pos=(0, 0), flag=wx.EXPAND | wx.ALL, border=5)
            ErrorWindow.sizer.Add(ErrorWindow.OKButton, pos=(1, 1), flag=wx.ALL, border=5)
            ErrorWindow.panel.SetSizerAndFit(ErrorWindow.sizer)
            ErrorWindow.Fit()
            ErrorWindow.Show()
            return
        elif dlgStyle == "wxPython":
            wx.MessageDialog(parent, message, caption="Error", style=wx.OK | wx.ICON_ERROR).ShowModal()
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
                    print("ERROR: Unknown Message Box Style")

# history window
class HistoryWindow(wx.Frame):
    def __init__(self, parent, calculator):
        super().__init__(parent, title="History")
        self.panel = wx.Panel(self)
        self.HistoryList = wx.ListBox(self.panel, choices=calculator.HistoryList)
        self.ClearButton = wx.Button(self.panel, label="Clear history")
        self.ClearButton.SetBitmapLabel(wx.ArtProvider.GetBitmap(wx.ART_DELETE, wx.ART_BUTTON, (16, 16)))
        self.ClearButton.Bind(wx.EVT_BUTTON, lambda _: self.clear(calculator))
        self.sizer = wx.GridBagSizer()
        self.sizer.AddGrowableCol(0)
        self.sizer.AddGrowableRow(0)
        self.sizer.Add(self.HistoryList, pos=(0, 0), flag=wx.EXPAND)
        self.sizer.Add(self.ClearButton, pos=(1, 0), flag=wx.EXPAND | wx.ALL, border=5)
        self.panel.SetSizerAndFit(self.sizer)
        self.Fit()
        self.Show()
    def clear(self, calculator): # clears the history
        calculator.clearHistory()
        self.HistoryList.Clear()

# extension window
class ExtensionWindow(wx.Dialog):
    def __init__(self, parent, calculator, dialog, cfg):
        super().__init__(parent, title="Extensions")
        self.font = wx.Font(10, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.panel = wx.Panel(self)
        self.sThing = wx.StaticText(self.panel, label=r""" _   ___   _
|   |   |   |
|   |   |   |
|   \   /   |
|    \_/    |
|     _     |
|    / \    |
|_   \_/   _|""")
        self.sThing.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))
        self.TextPartII = wx.StaticText(self.panel, label="""\nThe new PraktiCalc Extension system is far from done.
As the Legacy Extension System relies on Tkinter, I
couldn't just port it to wxPython, also because
PraktiXtensions themselves depend on Tkinter.
PraktiCalc 1.6 will support both PraktiXtensions and
new PraktiCalc Extensions. Stay tuned!
  ~Karl""")
        self.sThing.SetFont(self.font)
        self.TextPartII.SetFont(self.font)
        self.sizer = wx.GridBagSizer(5)
        self.sizer.Add(self.sThing, pos=(0, 0))
        self.sizer.Add(self.TextPartII, pos=(0, 1))
        self.panel.SetSizerAndFit(self.sizer)
        self.Fit()
        self.Show()

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
info: shows version numbers

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
        elif command.startswith("info"):
            output = f"PraktiCalc Console\t\t>_^\nCopyright (C) 2025-2026 Karl Wesseler\n*************************************\nPraktiCalc {PraktiCalcVersion}\nPython {platform.python_version()}\nwxPython {wx.VERSION_STRING}"
        else:
            output = "[X] Unknown command"
        return output

# console text interface
def ConsoleTextInterface(console, window):
    print(console.execute("info") + "\n")
    while True:
        print(" -> ", end="")
        nc = str(input())
        if nc == "quit":
            window.Close()
            break
        else:
            print(console.execute(nc))

if __name__ == "__main__":
    cfg = Configuration()
    Calculator = PraktiCalculator(cfg)
    WindowDialog = Dialog(cfg)
    app = wx.App()
    frame = MainWindow(Calculator, WindowDialog, cfg)
    if "--console" in sys.argv:
        cmd = Console(cfg)
        threading.Thread(target=lambda: ConsoleTextInterface(cmd, frame), daemon=True).start()
    frame.Show()
    app.MainLoop()
