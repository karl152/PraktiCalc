# PraktiCalc - a calculator with GUI i started at my student internship in 2024
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

# PraktiCalc
# Version 1.2.1 vom 10.08.2025
# Entstanden als Praktikumsprojekt
# getestet für Python 3.13.6 (Windows)

# Module importieren
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedStyle
import platform
import subprocess
usedttktheme = "default"
if platform.system() == "Windows":
    MsgBoxStyles = ["Tkinter", "Alternative", "VBS"]
else:
    MsgBoxStyles = ["Tkinter", "Alternative", "XMessage", "YAD", "KDialog", "Zenity"]
CurrentMsgBoxStyle = 1
# import win32clipboard
# Variablen definieren
Eingabe1 = "0"
Eingabe2 = "0"
Stage = 0
Operator = "op"
StatusBar = 0
CustomMsgBox = 1
DarkMode = 0
History1 = History2 = History3 = History4 = History5 = History6 = History7 = History8 = History9 = History10 = History11 = History12 = History13 = History14 = History15 = ""
# History1 = ""
# History2 = ""
# History3 = ""
# History4 = ""
# History5 = ""
# History6 = ""
# History7 = ""
# History8 = ""
# History9 = ""
# History10 = ""
# History11 = ""
# History12 = ""
# History13 = ""
# History14 = ""
# History15 = ""
HistoryWrite = 1
EndErgebnis = 0
aEndErgebnis = 0
DezimalZahl = 0
BinaerZahl = 0
HexadezimalZahl = 0

# Funktionen definieren
def info() :
    CustomInfo()
def eins() :
    global Eingabe1, Eingabe2, Ausgabe, Stage
    if Stage == 5 :
        Eingabe2 = str(Eingabe2) + "1"
        Ausgabe.config(text=Eingabe2)
    if Stage == 4 :
        Eingabe2 = str(Eingabe2) + "1"
        Ausgabe.config(text=Eingabe2)
    if Stage == 3 :
        Eingabe2 = "1"
        Ausgabe.config(text=Eingabe2)
        Stage = 4
    if Stage == 2 :
            Eingabe1 = str(Eingabe1) + "1"
            Ausgabe.config(text=Eingabe1)
    if Stage == 1 :
        Eingabe1 = str(Eingabe1) + "1"
        Ausgabe.config(text=Eingabe1)
    if Stage == 0 :
        Eingabe1 = "1"
        Ausgabe.config(text=Eingabe1)
        Stage = 1
    SizeReload()
def zwei() :
    global Eingabe1, Eingabe2, Ausgabe, Stage
    if Stage == 5 :
        Eingabe2 = str(Eingabe2) + "2"
        Ausgabe.config(text=Eingabe2)
    if Stage == 4 :
        Eingabe2 = str(Eingabe2) + "2"
        Ausgabe.config(text=Eingabe2)
    if Stage == 3 :
        Eingabe2 = "2"
        Ausgabe.config(text=Eingabe2)
        Stage = 4
    if Stage == 2 :
        Eingabe1 = str(Eingabe1) + "2"
        Ausgabe.config(text=Eingabe1)
    if Stage == 1 :
        Eingabe1 = str(Eingabe1) + "2"
        Ausgabe.config(text=Eingabe1)
    if Stage == 0 :
        Eingabe1 = "2"
        Ausgabe.config(text=Eingabe1)
        Stage = 1
    SizeReload()
def drei() :
    global Eingabe1, Eingabe2, Ausgabe, Stage
    if Stage == 5 :
        Eingabe2 = str(Eingabe2) + "3"
        Ausgabe.config(text=Eingabe2)
    if Stage == 4 :
        Eingabe2 = str(Eingabe2) + "3"
        Ausgabe.config(text=Eingabe2)
    if Stage == 3 :
        Eingabe2 = "3"
        Ausgabe.config(text=Eingabe2)
        Stage = 4
    if Stage == 2 :
        Eingabe1 = str(Eingabe1) + "3"
        Ausgabe.config(text=Eingabe1)
    if Stage == 1 :
        Eingabe1 = str(Eingabe1) + "3"
        Ausgabe.config(text=Eingabe1)
    if Stage == 0 :
        Eingabe1 = "3"
        Ausgabe.config(text=Eingabe1)
        Stage = 1
    SizeReload()
def vier() :
    global Eingabe1, Eingabe2, Ausgabe, Stage
    if Stage == 5 :
        Eingabe2 = str(Eingabe2) + "4"
        Ausgabe.config(text=Eingabe2)
    if Stage == 4 :
        Eingabe2 = str(Eingabe2) + "4"
        Ausgabe.config(text=Eingabe2)
    if Stage == 3 :
        Eingabe2 = "4"
        Ausgabe.config(text=Eingabe2)
        Stage = 4
    if Stage == 2 :
        Eingabe1 = str(Eingabe1) + "4"
        Ausgabe.config(text=Eingabe1)
    if Stage == 1 :
        Eingabe1 = str(Eingabe1) + "4"
        Ausgabe.config(text=Eingabe1)
    if Stage == 0 :
        Eingabe1 = "4"
        Ausgabe.config(text=Eingabe1)
        Stage = 1
    SizeReload()
def fünf() :
    global Eingabe1, Eingabe2, Ausgabe, Stage
    if Stage == 5 :
        Eingabe2 = str(Eingabe2) + "5"
        Ausgabe.config(text=Eingabe2)
    if Stage == 4 :
        Eingabe2 = str(Eingabe2) + "5"
        Ausgabe.config(text=Eingabe2)
    if Stage == 3 :
        Eingabe2 = "5"
        Ausgabe.config(text=Eingabe2)
        Stage = 4
    if Stage == 2 :
        Eingabe1 = str(Eingabe1) + "5"
        Ausgabe.config(text=Eingabe1)
    if Stage == 1 :
        Eingabe1 = str(Eingabe1) + "5"
        Ausgabe.config(text=Eingabe1)
    if Stage == 0 :
        Eingabe1 = "5"
        Ausgabe.config(text=Eingabe1)
        Stage = 1
    SizeReload()
def sechs() :
    global Eingabe1, Eingabe2, Ausgabe, Stage
    if Stage == 5 :
        Eingabe2 = str(Eingabe2) + "6"
        Ausgabe.config(text=Eingabe2)
    if Stage == 4 :
        Eingabe2 = str(Eingabe2) + "6"
        Ausgabe.config(text=Eingabe2)
    if Stage == 3 :
        Eingabe2 = "6"
        Ausgabe.config(text=Eingabe2)
        Stage = 4
    if Stage == 2 :
        Eingabe1 = str(Eingabe1) + "6"
        Ausgabe.config(text=Eingabe1)
    if Stage == 1 :
        Eingabe1 = str(Eingabe1) + "6"
        Ausgabe.config(text=Eingabe1)
    if Stage == 0 :
        Eingabe1 = "6"
        Ausgabe.config(text=Eingabe1)
        Stage = 1
    SizeReload()
def sieben() :
    global Eingabe1, Eingabe2, Ausgabe, Stage
    if Stage == 5 :
        Eingabe2 = str(Eingabe2) + "7"
        Ausgabe.config(text=Eingabe2)
    if Stage == 4 :
        Eingabe2 = str(Eingabe2) + "7"
        Ausgabe.config(text=Eingabe2)
    if Stage == 3 :
        Eingabe2 = "7"
        Ausgabe.config(text=Eingabe2)
        Stage = 4
    if Stage == 2 :
        Eingabe1 = str(Eingabe1) + "7"
        Ausgabe.config(text=Eingabe1)
    if Stage == 1 :
        Eingabe1 = str(Eingabe1) + "7"
        Ausgabe.config(text=Eingabe1)
    if Stage == 0 :
        Eingabe1 = "7"
        Ausgabe.config(text=Eingabe1)
        Stage = 1
    SizeReload()
def acht() :
    global Eingabe1, Eingabe2, Ausgabe, Stage
    if Stage == 5 :
        Eingabe2 = str(Eingabe2) + "8"
        Ausgabe.config(text=Eingabe2)
    if Stage == 4 :
        Eingabe2 = str(Eingabe2) + "8"
        Ausgabe.config(text=Eingabe2)
    if Stage == 3 :
        Eingabe2 = "8"
        Ausgabe.config(text=Eingabe2)
        Stage = 4
    if Stage == 2 :
        Eingabe1 = str(Eingabe1) + "8"
        Ausgabe.config(text=Eingabe1)
    if Stage == 1 :
        Eingabe1 = str(Eingabe1) + "8"
        Ausgabe.config(text=Eingabe1)
    if Stage == 0 :
        Eingabe1 = "8"
        Ausgabe.config(text=Eingabe1)
        Stage = 1
    SizeReload()
def neun() :
    global Eingabe1, Eingabe2, Ausgabe, Stage
    if Stage == 5 :
        Eingabe2 = str(Eingabe2) + "9"
        Ausgabe.config(text=Eingabe2)
    if Stage == 4 :
        Eingabe2 = str(Eingabe2) + "9"
        Ausgabe.config(text=Eingabe2)
    if Stage == 3 :
        Eingabe2 = "9"
        Ausgabe.config(text=Eingabe2)
        Stage = 4
    if Stage == 2 :
        Eingabe1 = str(Eingabe1) + "9"
        Ausgabe.config(text=Eingabe1)
    if Stage == 1 :
        Eingabe1 = str(Eingabe1) + "9"
        Ausgabe.config(text=Eingabe1)
    if Stage == 0 :
        Eingabe1 = "9"
        Ausgabe.config(text=Eingabe1)
        Stage = 1
    SizeReload()
def null() :
    global Eingabe1, Eingabe2, Ausgabe, Stage
    if Stage == 5 :
        Eingabe2 = str(Eingabe2) + "0"
        Ausgabe.config(text=Eingabe2)
    if Stage == 4 :
        Eingabe2 = str(Eingabe2) + "0"
        Ausgabe.config(text=Eingabe2)
    if Stage == 3 :
        Stage = 4
    if Stage == 2 :
        Eingabe1 = str(Eingabe1) + "0"
        Ausgabe.config(text=Eingabe1)
    if Stage == 1 :
        Eingabe1 = str(Eingabe1) + "0"
        Ausgabe.config(text=Eingabe1)
    if Stage == 0 :
        pass
    SizeReload()
def plus() :
    global Stage, Ausgabe, Operator, EndErgebnis, aEndErgebnis, Eingabe1, Eingabe2
    if Stage != 0 and Stage != 3 and Stage != 4 and Stage != 5 and Stage != 6 :
        Stage = 3
        Operator = "+"
        Ausgabe.config(text="0")
    if Stage == 4 or Stage == 5 :
        calc()
        Eingabe1 = EndErgebnis
        Operator = "+"
        Ausgabe.config(text="0")
        Stage = 3
    if Stage == 6 :
        Operator = "+"
        Stage = 3
        Ausgabe.config(text="0")
        Eingabe1 = EndErgebnis
    SizeReload()
def minus() :
    global Stage, Ausgabe, Operator, EndErgebnis, aEndErgebnis, Eingabe1, Eingabe2
    if Stage != 0 and Stage != 3 and Stage != 4 and Stage != 5 and Stage != 6 :
        Stage = 3
        Operator = "-"
        Ausgabe.config(text="0")
    if Stage == 4 or Stage == 5 :
        calc()
        Eingabe1 = EndErgebnis
        Operator = "-"
        Ausgabe.config(text="0")
        Stage = 3
    if Stage == 6 :
        Operator = "-"
        Stage = 3
        Ausgabe.config(text="0")
        Eingabe1 = EndErgebnis
    SizeReload()
def mal() :
    global Stage, Ausgabe, Operator, EndErgebnis, aEndErgebnis, Eingabe1, Eingabe2
    if Stage != 0 and Stage != 3 and Stage != 4 and Stage != 5 and Stage != 6 :
        Stage = 3
        Operator = "*"
        Ausgabe.config(text="0")
    if Stage == 4 or Stage == 5 :
        calc()
        Eingabe1 = EndErgebnis
        Operator = "*"
        Ausgabe.config(text="0")
        Stage = 3
    if Stage == 6 :
        Operator = "*"
        Stage = 3
        Ausgabe.config(text="0")
        Eingabe1 = EndErgebnis
    SizeReload()
def geteilt() :
    global Stage, Ausgabe, Operator, EndErgebnis, aEndErgebnis, Eingabe1, Eingabe2
    if Stage != 0 and Stage != 3 and Stage != 4 and Stage != 5 and Stage != 6 :
        Stage = 3
        Operator = "/"
        Ausgabe.config(text="0")
    if Stage == 4 or Stage == 5 :
        calc()
        Eingabe1 = EndErgebnis
        Operator = "/"
        Ausgabe.config(text="0")
        Stage = 3
    if Stage == 6 :
        Operator = "/"
        Stage = 3
        Ausgabe.config(text="0")
        Eingabe1 = EndErgebnis
    SizeReload()
def clear() :
    global Eingabe1, Eingabe2, Ausgabe, Stage, Status, StatusBar
    Eingabe1 = "0"
    Eingabe2 = "0"
    Stage = 0
    Ausgabe.config(text="0")
    if StatusBar == 1 :
        Status.config(text="Bereit")
    SizeReload()
def komma() :
    global Eingabe1, Eingabe2, Ausgabe, Stage
    if Stage == 5 :
        Eingabe2 = str(Eingabe2) + "."
        Ausgabe.config(text=Eingabe2)
    if Stage == 4 :
        Eingabe2 = str(Eingabe2) + "."
        Ausgabe.config(text=Eingabe2)
        Stage = 5
    if Stage == 3 :
        Eingabe2 = "0."
        Ausgabe.config(text=Eingabe2)
        Stage = 5
    if Stage == 2 :
        pass
    if Stage == 1 :
        Eingabe1 = str(Eingabe1) + "."
        Ausgabe.config(text=Eingabe1)
        Stage = 2
    if Stage == 0 :
        Eingabe1 = "0."
        Ausgabe.config(text=Eingabe1)
        Stage = 2
    SizeReload()
def calc() :
    global historylist, Eingabe1, Stage, Eingabe2, Ausgabe, Operator, EndErgebnis, aEndErgebnis, HistoryWrite, History1, History2, History3, History4, History5, History6, History7, History8, History9, History10, History11, History12, History13, History14, History15
    if HistoryWrite >=16 :
        History1 = History2
        History2 = History3
        History3 = History4
        History4 = History5
        History5 = History6
        History6 = History7
        History7 = History8
        History8 = History9
        History9 = History10
        History10 = History11
        History11 = History12
        History12 = History13
        History13 = History14
        History14 = History15
        HistoryWrite = 15
    if Stage == 6 :
        if Operator == "+" :
            aEndErgebnis = EndErgebnis
            EndErgebnis = EndErgebnis + float(Eingabe2)
            Ausgabe.config(text=str(EndErgebnis))
            if HistoryWrite == 15 :
                History15 = str(aEndErgebnis) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 14 :
                History14 = str(aEndErgebnis) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 13 :
                History13 = str(aEndErgebnis) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 12 :
                History12 = str(aEndErgebnis) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 11 :
                History11 = str(aEndErgebnis) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 10 :
                History10 = str(aEndErgebnis) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 9 :
                History9 = str(aEndErgebnis) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 8 :
                History8 = str(aEndErgebnis) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 7 :
                History7 = str(aEndErgebnis) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 6 :
                History6 = str(aEndErgebnis) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 5 :
                History5 = str(aEndErgebnis) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 4 :
                History4 = str(aEndErgebnis) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 3 :
                History3 = str(aEndErgebnis) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 2 :
                History2 = str(aEndErgebnis) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 1 :
                History1 = str(aEndErgebnis) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            HistoryWrite += 1
        if Operator == "-" :
            EndErgebnis = EndErgebnis - float(Eingabe2)
            Ausgabe.config(text=str(EndErgebnis))
            if HistoryWrite == 15 :
                History15 = str(aEndErgebnis) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 14 :
                History14 = str(aEndErgebnis) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 13 :
                History13 = str(aEndErgebnis) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 12 :
                History12 = str(aEndErgebnis) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 11 :
                History11 = str(aEndErgebnis) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 10 :
                History10 = str(aEndErgebnis) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 9 :
                History9 = str(aEndErgebnis) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 8 :
                History8 = str(aEndErgebnis) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 7 :
                History7 = str(aEndErgebnis) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 6 :
                History6 = str(aEndErgebnis) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 5 :
                History5 = str(aEndErgebnis) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 4 :
                History4 = str(aEndErgebnis) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 3 :
                History3 = str(aEndErgebnis) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 2 :
                History2 = str(aEndErgebnis) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 1 :
                History1 = str(aEndErgebnis) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            HistoryWrite += 1
        if Operator == "*" :
            EndErgebnis = EndErgebnis * float(Eingabe2)
            Ausgabe.config(text=str(EndErgebnis))
            if HistoryWrite == 15 :
                History15 = str(aEndErgebnis) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 14 :
                History14 = str(aEndErgebnis) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 13 :
                History13 = str(aEndErgebnis) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 12 :
                History12 = str(aEndErgebnis) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 11 :
                History11 = str(aEndErgebnis) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 10 :
                History10 = str(aEndErgebnis) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 9 :
                History9 = str(aEndErgebnis) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 8 :
                History8 = str(aEndErgebnis) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 7 :
                History7 = str(aEndErgebnis) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 6 :
                History6 = str(aEndErgebnis) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 5 :
                History5 = str(aEndErgebnis) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 4 :
                History4 = str(aEndErgebnis) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 3 :
                History3 = str(aEndErgebnis) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 2 :
                History2 = str(aEndErgebnis) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 1 :
                History1 = str(aEndErgebnis) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            HistoryWrite += 1
        if Operator == "/" :
            EndErgebnis = EndErgebnis / float(Eingabe2)
            Ausgabe.config(text=str(EndErgebnis))
            if HistoryWrite == 15 :
                History15 = str(aEndErgebnis) + " / " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 14 :
                History14 = str(aEndErgebnis) + " / " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 13 :
                History13 = str(aEndErgebnis) + " / " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 12 :
                History12 = str(aEndErgebnis) + " / " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 11 :
                History11 = str(aEndErgebnis) + " / " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 10 :
                History10 = str(aEndErgebnis) + " / " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 9 :
                History9 = str(aEndErgebnis) + " / " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 8 :
                History8 = str(aEndErgebnis) + " / " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 7 :
                History7 = str(aEndErgebnis) + " / " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 6 :
                History6 = str(aEndErgebnis) + " / " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 5 :
                History5 = str(aEndErgebnis) + " / " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 4 :
                History4 = str(aEndErgebnis) + " / " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 3 :
                History3 = str(aEndErgebnis) + " / " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 2 :
                History2 = str(aEndErgebnis) + " / " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 1 :
                History1 = str(aEndErgebnis) + " / " + Eingabe2 + " = " + str(EndErgebnis)
            HistoryWrite += 1
        if Operator == "sqrt" :
            aEndErgebnis = EndErgebnis
            EndErgebnis = EndErgebnis ** 0.5
            Ausgabe.config(text=str(EndErgebnis))
            if HistoryWrite == 15 :
                History15 = "√" + str(aEndErgebnis) + " = " + str(EndErgebnis)
            if HistoryWrite == 14 :
                History15 = "√" + str(aEndErgebnis) + " = " + str(EndErgebnis)
            if HistoryWrite == 13 :
                History15 = "√" + str(aEndErgebnis) + " = " + str(EndErgebnis)
            if HistoryWrite == 12 :
                History15 = "√" + str(aEndErgebnis) + " = " + str(EndErgebnis)
            if HistoryWrite == 11 :
                History15 = "√" + str(aEndErgebnis) + " = " + str(EndErgebnis)
            if HistoryWrite == 10 :
                History15 = "√" + str(aEndErgebnis) + " = " + str(EndErgebnis)
            if HistoryWrite == 9 :
                History15 = "√" + str(aEndErgebnis) + " = " + str(EndErgebnis)
            if HistoryWrite == 8 :
                History15 = "√" + str(aEndErgebnis) + " = " + str(EndErgebnis)
            if HistoryWrite == 7 :
                History15 = "√" + str(aEndErgebnis) + " = " + str(EndErgebnis)
            if HistoryWrite == 6 :
                History15 = "√" + str(aEndErgebnis) + " = " + str(EndErgebnis)
            if HistoryWrite == 5 :
                History15 = "√" + str(aEndErgebnis) + " = " + str(EndErgebnis)
            if HistoryWrite == 4 :
                History15 = "√" + str(aEndErgebnis) + " = " + str(EndErgebnis)
            if HistoryWrite == 3 :
                History15 = "√" + str(aEndErgebnis) + " = " + str(EndErgebnis)
            if HistoryWrite == 2 :
                History15 = "√" + str(aEndErgebnis) + " = " + str(EndErgebnis)
            if HistoryWrite == 1 :
                History15 = "√" + str(aEndErgebnis) + " = " + str(EndErgebnis)
            HistoryWrite += 1
    if Stage != 0 and Stage != 1 and Stage != 2 and Stage != 3 and Stage != 6 :
        Stage = 6
        if Operator == "+" :
            EndErgebnis = (float(Eingabe1) + float(Eingabe2))
            Ausgabe.config(text=float(Eingabe1) + float(Eingabe2))
            if HistoryWrite == 15 :
                History15 = str(Eingabe1) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 14 :
                History14 = str(Eingabe1) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 13 :
                History13 = str(Eingabe1) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 12 :
                History12 = str(Eingabe1) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 11 :
                History11 = str(Eingabe1) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 10 :
                History10 = str(Eingabe1) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 9 :
                History9 = str(Eingabe1) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 8 :
                History8 = str(Eingabe1) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 7 :
                History7 = str(Eingabe1) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 6 :
                History6 = str(Eingabe1) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 5 :
                History5 = str(Eingabe1) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 4 :
                History4 = str(Eingabe1) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 3 :
                History3 = str(Eingabe1) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 2 :
                History2 = str(Eingabe1) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 1 :
                History1 = str(Eingabe1) + " + " + Eingabe2 + " = " + str(EndErgebnis)
            HistoryWrite += 1
        if Operator == "-" :
            EndErgebnis = (float(Eingabe1) - float(Eingabe2))
            Ausgabe.config(text=float(Eingabe1) - float(Eingabe2))
            if HistoryWrite == 15 :
                History15 = str(Eingabe1) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 14 :
                History14 = str(Eingabe1) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 13 :
                History13 = str(Eingabe1) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 12 :
                History12 = str(Eingabe1) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 11 :
                History11 = str(Eingabe1) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 10 :
                History10 = str(Eingabe1) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 9 :
                History9 = str(Eingabe1) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 8 :
                History8 = str(Eingabe1) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 7 :
                History7 = str(Eingabe1) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 6 :
                History6 = str(Eingabe1) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 5 :
                History5 = str(Eingabe1) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 4 :
                History4 = str(Eingabe1) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 3 :
                History3 = str(Eingabe1) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 2 :
                History2 = str(Eingabe1) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 1 :
                History1 = str(Eingabe1) + " - " + Eingabe2 + " = " + str(EndErgebnis)
            HistoryWrite += 1
        if Operator == "*" :
            EndErgebnis = (float(Eingabe1) * float(Eingabe2))
            Ausgabe.config(text=float(Eingabe1) * float(Eingabe2))
            if HistoryWrite == 15 :
                History15 = str(Eingabe1) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 14 :
                History14 = str(Eingabe1) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 13 :
                History13 = str(Eingabe1) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 12 :
                History12 = str(Eingabe1) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 11 :
                History11 = str(Eingabe1) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 10 :
                History10 = str(Eingabe1) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 9 :
                History9 = str(Eingabe1) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 8 :
                History8 = str(Eingabe1) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 7 :
                History7 = str(Eingabe1) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 6 :
                History6 = str(Eingabe1) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 5 :
                History5 = str(Eingabe1) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 4 :
                History4 = str(Eingabe1) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 3 :
                History3 = str(Eingabe1) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 2 :
                History2 = str(Eingabe1) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            if HistoryWrite == 1 :
                History1 = str(Eingabe1) + " * " + Eingabe2 + " = " + str(EndErgebnis)
            HistoryWrite += 1
        if Operator == "/" :
            if Eingabe2 == "0" :
                if StatusBar == 0 :
                    CustomDiv0()
                if StatusBar == 1 :
                    Status.config(text="Error: Division by 0")
                clear()
            else :
                EndErgebnis = (float(Eingabe1) / float(Eingabe2))
                Ausgabe.config(text=float(Eingabe1) / float(Eingabe2))
                if HistoryWrite == 15 :
                    History15 = str(Eingabe1) + " / " + Eingabe2 + " = " + str(EndErgebnis)
                if HistoryWrite == 14 :
                    History14 = str(Eingabe1) + " / " + Eingabe2 + " = " + str(EndErgebnis)
                if HistoryWrite == 13 :
                    History13 = str(Eingabe1) + " / " + Eingabe2 + " = " + str(EndErgebnis)
                if HistoryWrite == 12 :
                    History12 = str(Eingabe1) + " / " + Eingabe2 + " = " + str(EndErgebnis)
                if HistoryWrite == 11 :
                    History11 = str(Eingabe1) + " / " + Eingabe2 + " = " + str(EndErgebnis)
                if HistoryWrite == 10 :
                    History10 = str(Eingabe1) + " / " + Eingabe2 + " = " + str(EndErgebnis)
                if HistoryWrite == 9 :
                    History9 = str(Eingabe1) + " / " + Eingabe2 + " = " + str(EndErgebnis)
                if HistoryWrite == 8 :
                    History8 = str(Eingabe1) + " / " + Eingabe2 + " = " + str(EndErgebnis)
                if HistoryWrite == 7 :
                    History7 = str(Eingabe1) + " / " + Eingabe2 + " = " + str(EndErgebnis)
                if HistoryWrite == 6 :
                    History6 = str(Eingabe1) + " / " + Eingabe2 + " = " + str(EndErgebnis)
                if HistoryWrite == 5 :
                    History5 = str(Eingabe1) + " / " + Eingabe2 + " = " + str(EndErgebnis)
                if HistoryWrite == 4 :
                    History4 = str(Eingabe1) + " / " + Eingabe2 + " = " + str(EndErgebnis)
                if HistoryWrite == 3 :
                    History3 = str(Eingabe1) + " / " + Eingabe2 + " = " + str(EndErgebnis)
                if HistoryWrite == 2 :
                    History2 = str(Eingabe1) + " / " + Eingabe2 + " = " + str(EndErgebnis)
                if HistoryWrite == 1 :
                    History1 = str(Eingabe1) + " / " + Eingabe2 + " = " + str(EndErgebnis)
                HistoryWrite += 1
        if Operator == "sqrt" :
            Eingabe2 = str(float(Eingabe1) ** 0.5)
            Ausgabe.config(text=Eingabe2)
    if Operator == "sqrt" :
        if Stage == 3 :
            EndErgebnis = float(Eingabe1) ** 0.5
            Ausgabe.config(text=EndErgebnis)
            if HistoryWrite == 15 :
                History15 = "√" + str(Eingabe1) + " = " + str(EndErgebnis)
            if HistoryWrite == 14 :
                History14 = "√" + str(Eingabe1) + " = " + str(EndErgebnis)
            if HistoryWrite == 13 :
                History13 = "√" + str(Eingabe1) + " = " + str(EndErgebnis)
            if HistoryWrite == 12 :
                History12 = "√" + str(Eingabe1) + " = " + str(EndErgebnis)
            if HistoryWrite == 11 :
                History11 = "√" + str(Eingabe1) + " = " + str(EndErgebnis)
            if HistoryWrite == 10 :
                History10 = "√" + str(Eingabe1) + " = " + str(EndErgebnis)
            if HistoryWrite == 9 :
                History9 = "√" + str(Eingabe1) + " = " + str(EndErgebnis)
            if HistoryWrite == 8 :
                History8 = "√" + str(Eingabe1) + " = " + str(EndErgebnis)
            if HistoryWrite == 7 :
                History7 = "√" + str(Eingabe1) + " = " + str(EndErgebnis)
            if HistoryWrite == 6 :
                History6 = "√" + str(Eingabe1) + " = " + str(EndErgebnis)
            if HistoryWrite == 5 :
                History5 = "√" + str(Eingabe1) + " = " + str(EndErgebnis)
            if HistoryWrite == 4 :
                History4 = "√" + str(Eingabe1) + " = " + str(EndErgebnis)
            if HistoryWrite == 3 :
                History3 = "√" + str(Eingabe1) + " = " + str(EndErgebnis)
            if HistoryWrite == 2 :
                History2 = "√" + str(Eingabe1) + " = " + str(EndErgebnis)
            if HistoryWrite == 1 :
                History1 = "√" + str(Eingabe1) + " = " + str(EndErgebnis)
            HistoryWrite += 1
            Stage = 6
    SizeReload()
def Tastendruck(event):
    Taste = event.keysym
    if Taste == "1" :
        eins()
    if Taste == "2" :
        zwei()
    if Taste == "3" :
        drei()
    if Taste == "4" :
        vier()
    if Taste == "5" :
        fünf()
    if Taste == "6" :
        sechs()
    if Taste == "7" :
        sieben()
    if Taste == "8" :
        acht()
    if Taste == "9" :
        neun()
    if Taste == "0" :
        null()
    if Taste == "equal" :
        calc()
    if Taste == "plus" :
        plus()
    if Taste == "minus" :
        minus()
    if Taste == "asterisk" :
        mal()
    if Taste == "slash" :
        geteilt()
    if Taste == "h" :
        History()
    if Taste == "H" :
        History()
    if Taste == "c" :
        clear()
    if Taste == "C" :
        clear()
    if Taste == "i" :
        info()
    if Taste == "s" :
        Settings()
    if Taste == "S" :
        Settings()
    if Taste == "comma" :
        komma()
    if Taste == "Return" :
        calc()
    if Taste == "BackSpace" :
        Backspace()
def Settings() :
    global Status, SettingsWindow, StatusBar, StatusBarToggle, CustomMsgBox, CustomMsgBoxToggle, DarkMode, DarkModeToggle, MsgBoxStyles, CurrentMsgBoxStyle, MsgBoxStyleSelect
    SettingsWindow = tk.Tk()
    SettingsWindow.title("Settings")
    SettingsWindow.config(width=250, height=152)
    SettingsWindow.rowconfigure(0, weight=1)
    SettingsWindow.columnconfigure(0, weight=1)
    style = ThemedStyle(SettingsWindow)
    style.theme_use(usedttktheme)
    SettingsWindowFrame = ttk.Frame(SettingsWindow)
    SettingsWindowFrame.columnconfigure(0, weight=1)
    StatusBarToggle = ttk.Checkbutton(SettingsWindowFrame, text="Status Bar", command=ToggleStatusBar)
    CustomMsgBoxToggle = ttk.Checkbutton(SettingsWindowFrame, text="Alternative Messageboxes", command=ToggleCustomMsgBoxes)
    if CustomMsgBox == 0 :
        CustomMsgBoxToggle.state(["!selected"])
    if CustomMsgBox == 1 :
        CustomMsgBoxToggle.state(["selected"])
    DarkModeToggle = ttk.Checkbutton(SettingsWindowFrame, text="Dark Mode", command=ChangeDarkMode)
    if StatusBar == 1:
        StatusBarToggle.state(["selected"])
    elif StatusBar == 0:
        StatusBarToggle.state(["!selected"])
    if DarkMode == 1:
        DarkModeToggle.state(["selected"])
    elif DarkMode == 0:
        DarkModeToggle.state(["!selected"])
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
    print(CurrentMsgBoxStyle)
    SettingsWindow.destroy()
def ToggleCustomMsgBoxes():
    global CustomMsgBox, CustomMsgBoxToggle
    if CustomMsgBox == 0:
        CustomMsgBox = 1
    elif CustomMsgBox == 1:
        CustomMsgBox = 0
def ToggleStatusBar():
    global Status, StatusBar, StatusBarToggle, StatusDecoration, Fenster
    if StatusBar == 1:
        Status.config(text="")
        StatusBar = 0
        StatusDecoration.config(text="")
        Fenster.config(width=256, height=315)
    elif StatusBar == 0:
        Fenster.config(width=256, height=330)
        Status.config(text="Ready")
        StatusBar = 1
        StatusDecoration.config(text="__________________________________________________")
def ChangeDarkMode() :
    global DarkMode, usedttktheme, SettingsWindow, style, HistoryX, MehrX
    if DarkMode == 0 :
        DarkMode = 1
        usedttktheme = "black"
        style = ThemedStyle(Fenster)
        style.theme_use(usedttktheme)
        style = ThemedStyle(SettingsWindow)
        style.theme_use(usedttktheme)
        style = ThemedStyle(HistoryX)
        style.theme_use(usedttktheme)
        style = ThemedStyle(MehrX)
        style.theme_use(usedttktheme)
        style = ThemedStyle(Div0Error)
        style.theme_use(usedttktheme)
        style = ThemedStyle(CustomInfox)
        style.theme_use(usedttktheme)
    elif DarkMode == 1 :
        DarkMode = 0
        usedttktheme = "default"
        style = ThemedStyle(Fenster)
        style.theme_use(usedttktheme)
        style = ThemedStyle(SettingsWindow)
        style.theme_use(usedttktheme)
        style = ThemedStyle(HistoryX)
        style.theme_use(usedttktheme)
        style = ThemedStyle(MehrX)
        style.theme_use(usedttktheme)
        style = ThemedStyle(Div0Error)
        style.theme_use(usedttktheme)
        style = ThemedStyle(CustomInfox)
        style.theme_use(usedttktheme)
def CustomDiv0() :
    showError("Division by 0")
def CustomInfo() :
    global CustomInfox
    infotext = "PraktiCalc\nVersion 1.3 (in development)\nrunning on Python "+ platform.python_version() + "\nLicensed under GPLv3\nread more at https://www.gnu.org/licenses/"
    if CurrentMsgBoxStyle == 0:
        messagebox.showinfo("About PraktiCalc", infotext)
    elif CurrentMsgBoxStyle == 1:
        CustomInfox = tk.Tk()
        CustomInfox.title("About PraktiCalc")
        CustomInfox.config(width=500, height=250)
        style = ThemedStyle(CustomInfox)
        style.theme_use(usedttktheme)
        CustomInfoDesc = ttk.Label(CustomInfox, text="PraktiCalc")
        CustomInfoSymbol = ttk.Label(CustomInfox, text="ℹ")
        CustomInfoExit = ttk.Button(CustomInfox, text="     OK     ", command=closeCustomInfo)
        ExtendedInfoFrame = ttk.Frame(CustomInfox, relief="sunken", borderwidth=2)
        ExtInfoText1 = ttk.Label(ExtendedInfoFrame, text=infotext, justify="left")
        CustomInfoDesc.place(x=150, y=25)
        CustomInfoSymbol.place(x=10, y=10)
        CustomInfoExit.place(x=400, y=200)
        ExtendedInfoFrame.place(x=100, y=55, height=125, width=357)
        ExtInfoText1.place(x=5, y=0)
    else:
        if platform.system() == "Windows":
            if CurrentMsgBoxStyle == 2:
                subprocess.getoutput('cmd /C echo(MsgBox "PraktiCalc                                                                              Version 1.3                                                                                      a Python Project                                                                 Licensed under GPLv3                                                               read more at https://www.gnu.org/licenses/", 64, "About PraktiCalc"> test.vbs && cscript test.vbs && del test.vbs')
            else:
                print("ERROR: Unknown Message Box Style")
        else:
            if CurrentMsgBoxStyle == 2:
                subprocess.Popen(["xmessage", "-title", "About PraktiCalc", infotext])
            elif CurrentMsgBoxStyle == 3:
                subprocess.Popen(["yad", "--title=About PraktiCalc", "--info", "--image=dialog-information", "--button=OK", "--text=" + infotext])
            elif CurrentMsgBoxStyle == 4:
                subprocess.Popen(["kdialog", "--title=About PraktiCalc", "--msgbox", infotext])
            elif CurrentMsgBoxStyle == 5:
                subprocess.Popen(["zenity", "--title=About PraktiCalc", "--info", "--text=" + infotext])
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
        ErrorWindow = tk.Tk()
        ErrorWindow.title("Error")
        ErrorWindow.config(width=500, height=250)
        style = ThemedStyle(ErrorWindow)
        style.theme_use(usedttktheme)
        ErrorDesc = ttk.Label(ErrorWindow, text=message)
        ErrorSymbol = ttk.Label(ErrorWindow, text="🚫")
        ErrorExitButton = ttk.Button(ErrorWindow, text="     OK     ", command=closeError)
        ErrorDesc.place(x=150, y=100)
        ErrorSymbol.place(x=10, y=10)
        ErrorExitButton.place(x=400, y=200)
    else:
        if platform.system() == "Windows":
            if CurrentMsgBoxStyle == 2:
                subprocess.getoutput('cmd /C echo(MsgBox "' + message + '", 16, "Error"> test.vbs && cscript test.vbs && del test.vbs')
            else:
                print("ERROR: Unknown Message Box Style")
        else:
            if CurrentMsgBoxStyle == 2:
                subprocess.Popen(["xmessage", "-title", "Error", "[X] " + message])
            elif CurrentMsgBoxStyle == 3:
                subprocess.Popen(["yad", "--title=Error", "--error", "--image=dialog-error", "--button=OK", "--text=" + message])
            elif CurrentMsgBoxStyle == 4:
                subprocess.Popen(["kdialog", "--title=Error", "--error", message])
            elif CurrentMsgBoxStyle == 5:
                subprocess.Popen(["zenity", "--title=Error", "--error", "--text=" + message])
            else:
                print("ERROR: Unknown Message Box Style")
def closeError():
    global ErrorWindow
    ErrorWindow.destroy()
def SizeReload() :
    pass
def ZeichenStatus() :
    global Status, StatusBar
    if StatusBar == 1 :
        Status.config(text="PraktiCalc only supports up to 15 characters!")
def Backspace() :
    global Eingabe1, Eingabe2
    if Stage == 1 :
        Eingabe1 = Eingabe1[:len(Eingabe1) - 1]
    if Stage == 2 :
        Eingabe1 = Eingabe1[:len(Eingabe1) - 1]
    if Stage == 4 :
        Eingabe2 = Eingabe2[:len(Eingabe2) - 1]
    if Stage == 5 :
        Eingabe2 = Eingabe2[:len(Eingabe2) - 1]
    updateDisplay()
def updateDisplay() :
    global Eingabe1, Ausgabe, Eingabe2, Stage
    if Stage == 5 :
        Ausgabe.config(text=Eingabe2)
        if not "." in Eingabe2 :
            Stage = 4
    if Stage == 4 :
        Ausgabe.config(text=Eingabe2)
        if len(Eingabe2) == 0 :
            Stage = 3
    if Stage == 3 :
        Ausgabe.config(text=Eingabe2)
    if Stage == 2 :
        Ausgabe.config(text=Eingabe1)
        if not "." in Eingabe1 :
            Stage = 1
    if Stage == 1 :
        Ausgabe.config(text=Eingabe1)
        if len(Eingabe1) == 0 :
            Stage= 0
    if Stage == 0 :
        Ausgabe.config(text="0")
    SizeReload()
def History() :
    global HistoryX, History1, History2, History3, History4, History5, History6, History7, History8, History9, History10, History11, History12, History13, History14, History15
    HistoryX = tk.Tk()
    HistoryX.title("History")
    HistoryX.config(height=400, width=256)
    style = ThemedStyle(HistoryX)
    style.theme_use(usedttktheme)
    HistoryLabel = ttk.Label(HistoryX, text="History")
    Hostory1 = ttk.Label(HistoryX, text=History1)
    Hostory2 = ttk.Label(HistoryX, text=History2)
    Hostory3 = ttk.Label(HistoryX, text=History3)
    Hostory4 = ttk.Label(HistoryX, text=History4)
    Hostory5 = ttk.Label(HistoryX, text=History5)
    Hostory6 = ttk.Label(HistoryX, text=History6)
    Hostory7 = ttk.Label(HistoryX, text=History7)
    Hostory8 = ttk.Label(HistoryX, text=History8)
    Hostory9 = ttk.Label(HistoryX, text=History9)
    Hostory10 = ttk.Label(HistoryX, text=History10)
    Hostory11 = ttk.Label(HistoryX, text=History11)
    Hostory12 = ttk.Label(HistoryX, text=History12)
    Hostory13 = ttk.Label(HistoryX, text=History13)
    Hostory14 = ttk.Label(HistoryX, text=History14)
    Hostory15 = ttk.Label(HistoryX, text=History15)
    ClearButton = ttk.Button(HistoryX, text="🗑", command=clearHistory)
    HistoryLabel.place(x=0, y=0)
    Hostory1.place(x=0, y=25)
    Hostory2.place(x=0, y=50)
    Hostory3.place(x=0, y=75)
    Hostory4.place(x=0, y=100)
    Hostory5.place(x=0, y=125)
    Hostory6.place(x=0, y=150)
    Hostory7.place(x=0, y=175)
    Hostory8.place(x=0, y=200)
    Hostory9.place(x=0, y=225)
    Hostory10.place(x=0, y=250)
    Hostory11.place(x=0, y=275)
    Hostory12.place(x=0, y=300)
    Hostory13.place(x=0, y=325)
    Hostory14.place(x=0, y=350)
    Hostory15.place(x=0, y=375)
    ClearButton.place(x=220, y=360)
    SizeReload()
def mnus() :
    global Eingabe1, Eingabe2, Ausgabe, Stage
    if Stage == 5 :
        if Eingabe2[0] != "-" :
            Eingabe2 = "-" + str(Eingabe2)
            Ausgabe.config(text=Eingabe2)
    if Stage == 4 :
        if Eingabe2[0] != "-" :
            Eingabe2 = "-" + str(Eingabe2)
            Ausgabe.config(text=Eingabe2)
    if Stage == 3 :
        if Eingabe2[0] != "-" :
            Eingabe2 = "-"
            Ausgabe.config(text=Eingabe2)
            Stage = 4
    if Stage == 2 :
        if Eingabe1[0] != "-" :
            Eingabe1 = "-" + str(Eingabe1)
            Ausgabe.config(text=Eingabe1)
    if Stage == 1 :
        if Eingabe1[0] != "-" :
            Eingabe1 = "-" + str(Eingabe1)
            Ausgabe.config(text=Eingabe1)
    if Stage == 0 :
        if Eingabe1[0] != "-" :
            Eingabe1 = "-"
            Ausgabe.config(text=Eingabe1)
            Stage = 1
    SizeReload()
def wurzelig() :
    global Operator, Stage
    Operator = "sqrt"
    if Stage == 1 :
        Stage = 3
    if Stage == 2 :
        Stage = 3
    calc()
def Meehr() :
    global DarkMode, MehrX, DezimalFrame, DezimalAnzeige, DezimalZahl, BinaerLabel, HexLabel, usedttktheme
    MehrX = tk.Tk()
    MehrX.title("Decimal Converter")
    MehrX.config(height=200, width=500)
    MehrX.rowconfigure(0, weight=1)
    MehrX.columnconfigure(0, weight=1)
    style = ThemedStyle(MehrX)
    style.theme_use(usedttktheme)
    ConverterWindowFrame = ttk.Frame(MehrX)
    DezimalFrame = ttk.LabelFrame(ConverterWindowFrame, text="Decimal")
    DezimalAnzeige = ttk.Entry(DezimalFrame, width=70)
    DezimalFrame.columnconfigure(0, weight=1)
    ConverterWindowFrame.columnconfigure(0, weight=1)
    ConverterWindowFrame.columnconfigure(1, weight=1)
    ConverterWindowFrame.rowconfigure(1, weight=1)
    InsertButton = ttk.Button(DezimalFrame, text="OK", command=paste)
    binFrame = ttk.LabelFrame(ConverterWindowFrame, text="Binary")
    hexFrame = ttk.LabelFrame(ConverterWindowFrame, text="Hexadecimal")
    binFrame.rowconfigure(0, weight=1)
    binFrame.columnconfigure(0, weight=1)
    hexFrame.rowconfigure(0, weight=1)
    hexFrame.columnconfigure(0, weight=1)
    BinaerLabel = ttk.Label(binFrame, text="")
    HexLabel = ttk.Label(hexFrame, text="")
    ConverterWindowFrame.grid(row=0, column=0, sticky="nesw")
    DezimalFrame.grid(row=0, column=0, columnspan=2, sticky="nesw", padx=5)
    DezimalAnzeige.grid(row=0, column=0, pady=5, padx=5, sticky="nesw")
    InsertButton.grid(row=0, column=1, padx=5, pady=5)
    binFrame.grid(row=1, column=0, sticky="nesw", padx=5)
    hexFrame.grid(row=1, column=1, sticky="nesw", padx=5)
    BinaerLabel.grid(row=0, column=0)
    HexLabel.grid(row=0, column=0)
def paste() :
    global DezimalZahl, DezimalAnzeige, BinaerZahl, HexadezimalZahl, BinaerLabel, HexLabel
    # win32clipboard.OpenClipboard()
    # cp = win32clipboard.GetClipboardData()
    # win32clipboard.CloseClipboard()
    cp = str(DezimalAnzeige.get())
    try:
        DezimalZahl = int(cp)
    except:
        showError("Please enter a real number!")
    DezimalAnzeige.config(text=str(DezimalZahl))
    BinaerZahl = bin(DezimalZahl)[2:]
    HexadezimalZahl = hex(DezimalZahl)
    BinaerLabel.config(text=str(BinaerZahl))
    HexLabel.config(text=str(HexadezimalZahl))
def copybin() :
    global BinaerZahl
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(BinaerZahl)
    win32clipboard.CloseClipboard()
def copyhex() :
    global HexadezimalZahl
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(HexadezimalZahl)
    win32clipboard.CloseClipboard()
def clearHistory() :
    global HistoryX, HistoryWrite, History1, History2, History3, History4, History5, History6, History7, History8, History9, History10, History11, History12, History13, History14, History15
    History1 = History2 = History3 = History4 = History5 = History6 = History7 = History8 = History9 = History10 = History11 = History12 = History13 = History14 = History15 = ""
    HistoryWrite = 1
    HistoryX.destroy()
    History()
def xcheck() :
    global Stage, Eingabe1, Eingabe2, HistoryWrite, EndErgebnis, Operator
    print("Stage: " + str(Stage))
    print("Eingabe1: " + Eingabe1)
    print("Eingabe2: " + Eingabe2)
    print("Operator: " + Operator)
    print("EndErgebnis: " + str(EndErgebnis))
    print("HistoryWrite: " + str(HistoryWrite))
    print("____________________________")
def xquit() :
    Fenster.destroy()
# if DarkMode == 1 :
#     usedttktheme = "black"
# Hauptfenster
Fenster = tk.Tk()
Fenster.title("PraktiCalc")
Fenster.config(width=256, height=315)
Fenster.rowconfigure(0, weight=1)
Fenster.columnconfigure(0, weight=1)
style = ThemedStyle(Fenster)
style.theme_use(usedttktheme)
WindowFrame = ttk.Frame(Fenster)
for colrow in range(5):
    WindowFrame.rowconfigure(colrow, weight=1)
    WindowFrame.columnconfigure(colrow, weight=1)
WindowFrame.rowconfigure(5, weight=1)
Ausgaberahmen = ttk.Frame(WindowFrame, borderwidth=1, relief="sunken")
Ausgabe = ttk.Label(Ausgaberahmen, text="0")
# Buttons
PlusButton = ttk.Button(WindowFrame, text="+", command=plus)
MinusButton = ttk.Button(WindowFrame, text="-", command=minus)
MalButton = ttk.Button(WindowFrame, text="x", command=mal)
GeteiltButton = ttk.Button(WindowFrame, text="÷", command=geteilt)
SiebenButton = ttk.Button(WindowFrame, text="7", command=sieben)
AchtButton = ttk.Button(WindowFrame, text="8", command=acht)
NeunButton = ttk.Button(WindowFrame, text="9", command=neun)
CEButton = ttk.Button(WindowFrame, text="CE", command=clear)
VierButton = ttk.Button(WindowFrame, text="4", command=vier)
FünfButton = ttk.Button(WindowFrame, text="5", command=fünf)
SechsButton = ttk.Button(WindowFrame, text="6", command=sechs)
KommaButton = ttk.Button(WindowFrame, text=",", command=komma)
EinsButton = ttk.Button(WindowFrame, text="1", command=eins)
ZweiButton = ttk.Button(WindowFrame, text="2", command=zwei)
DreiButton = ttk.Button(WindowFrame, text="3", command=drei)
GleichButton = ttk.Button(WindowFrame, text="=", command=calc)
InfoButton = ttk.Button(WindowFrame, text="i", command=info)
NullButton = ttk.Button(WindowFrame, text="0", command=null)
ExitButton = ttk.Button(WindowFrame, text="X", command=xquit)
Status = ttk.Label(WindowFrame, text="")
StatusDecoration = ttk.Label(WindowFrame, text="")
SettingsButton = ttk.Button(WindowFrame, text="🔧", command=Settings)
BackspaceButton = ttk.Button(WindowFrame, text="<", command=Backspace)
HistoryButton = ttk.Button(WindowFrame, text="📜", command=History)
MButton = ttk.Button(WindowFrame, text="±", command=mnus)
Checkb = ttk.Button(Fenster, text="Check", command=xcheck) # some debug thing
WurzelB = ttk.Button(WindowFrame, text="√", command=wurzelig)
Mehr = ttk.Button(WindowFrame, text="...", command=Meehr)
WindowFrame.grid(row=0, column=0, sticky="nesw")
Ausgaberahmen.grid(row=0, column=0, columnspan=4, sticky="nesw")
Ausgabe.pack()
PlusButton.grid(row=1, column=1, sticky="nesw")
MinusButton.grid(row=1, column=2, sticky="nesw")
MalButton.grid(row=1, column=3, sticky="nesw")
GeteiltButton.grid(row=1, column=4, sticky="nesw")
SiebenButton.grid(row=2, column=1, sticky="nesw")
AchtButton.grid(row=2, column=2, sticky="nesw")
NeunButton.grid(row=2, column=3, sticky="nesw")
CEButton.grid(row=2, column=4, sticky="nesw")
VierButton.grid(row=3, column=1, sticky="nesw")
FünfButton.grid(row=3, column=2, sticky="nesw")
SechsButton.grid(row=3, column=3, sticky="nesw")
KommaButton.grid(row=5, column=3, sticky="nesw")
EinsButton.grid(row=4, column=1, sticky="nesw")
ZweiButton.grid(row=4, column=2, sticky="nesw")
DreiButton.grid(row=4, column=3, sticky="nesw")
GleichButton.grid(row=5, column=4, sticky="nesw")
InfoButton.grid(row=1, column=0, sticky="nesw")
NullButton.grid(row=5, column=1, columnspan=2, sticky="nesw")
MButton.grid(row=4, column=4, sticky="nesw")
WurzelB.grid(row=3, column=4, sticky="nesw")
ExitButton.grid(row=5, column=0, sticky="nesw")
Status.grid(row=7, column=0, columnspan=5, sticky="nesw")
StatusDecoration.grid(row=6, column=0, columnspan=5, sticky="nesw")
SettingsButton.grid(row=2, column=0, sticky="nesw")
BackspaceButton.grid(row=0, column=4, sticky="nesw")
HistoryButton.grid(row=4, column=0, sticky="nesw")
Fenster.bind("<Key>", Tastendruck)
Mehr.grid(row=3, column=0, sticky="nesw")
# Checkb.grid(row=1, column=0, sticky="nesw")
Fenster.mainloop()
