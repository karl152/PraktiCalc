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
usedttktheme = "default"
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
    if CustomMsgBox == 0 :
        messagebox.showinfo("PraktiCalc 1.3 (in development), licensed under GPLv3", "This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.")
    if CustomMsgBox == 1 :
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
    global historylist, Eingabe1, Stage, Eingabe2, Ausgabe, Operator, EndErgebnis, aEndErgebnis, CustomMsgBox, HistoryWrite, History1, History2, History3, History4, History5, History6, History7, History8, History9, History10, History11, History12, History13, History14, History15
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
                    if CustomMsgBox == 0 :
                        messagebox.showerror("Error", "Division by 0")
                    if CustomMsgBox == 1 :
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
    global Status, SettingsWindow, StatusBar, StatusBarToggle, CustomMsgBox, CustomMsgBoxToggle, DarkMode, DarkModeToggle
    SettingsWindow = tk.Tk()
    SettingsWindow.title("Settings")
    SettingsWindow.config(width=250, height=152)
    style = ThemedStyle(SettingsWindow)
    style.theme_use(usedttktheme)
    SettingsTitle = ttk.Label(SettingsWindow, text="Settings", )
    SettingsTitleDecoration = ttk.Label(SettingsWindow, text="▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀", )
    StatusBarSettingDesc = ttk.Label(SettingsWindow, text="Status Bar")
    if StatusBar == 0 :
        StatusBarToggle = ttk.Button(SettingsWindow, text="☐", command=StatusBarOn)
    if StatusBar == 1 :
        StatusBarToggle = ttk.Button(SettingsWindow, text="🗹", command=StatusBarOff)
    CustomStatusBarDesc = ttk.Label(SettingsWindow, text="Alternative Messageboxes")
    if CustomMsgBox == 0 :
        CustomMsgBoxToggle = ttk.Button(SettingsWindow, text="☐", command=CustomMsgBoxOn)
    if CustomMsgBox == 1 :
        CustomMsgBoxToggle = ttk.Button(SettingsWindow, text="🗹", command=CustomMsgBoxOff)
    DarkModeToggle = ttk.Checkbutton(SettingsWindow, text="Dark Mode", command=ChangeDarkMode)
    DarkModeDesc = ttk.Label(SettingsWindow, text="Dark Mode")
    SettingsTitle.place(x=0, y=0)
    SettingsTitleDecoration.place(x=0, y=24)
    StatusBarSettingDesc.place(x=30, y=45)
    StatusBarToggle.place(x=5, y=45)
    CustomStatusBarDesc.place(x=30, y=72)
    CustomMsgBoxToggle.place(x=5, y=72)
    DarkModeToggle.place(x=5, y=99)
    # DarkModeDesc.place(x=30, y=99)
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
    print(DarkMode)
def StatusBarOn() :
    global Status, StatusBar, StatusBarToggle, StatusDecoration, Fenster
    Fenster.config(width=256, height=330)
    Status.config(text="Ready")
    StatusBar = 1
    StatusBarToggle.config(text="🗹", command=StatusBarOff)
    StatusDecoration.config(text="__________________________________________________")
    SizeReload()
def StatusBarOff() :
    global Status, StatusBar, StatusBarToggle, StatusDecoration, Fenster
    Status.config(text="")
    StatusBar = 0
    StatusBarToggle.config(text="☐", command=StatusBarOn)
    StatusDecoration.config(text="")
    Fenster.config(width=256, height=315)
    SizeReload()
def CustomDiv0() :
    global Div0Error
    Div0Error = tk.Tk()
    Div0Error.title("Error")
    Div0Error.config(width=500, height=250)
    style = ThemedStyle(Div0Error)
    style.theme_use(usedttktheme)
    Div0Desc = ttk.Label(Div0Error, text="Division by 0")
    Div0Symbol = ttk.Label(Div0Error, text="🚫")
    Div0Exit = ttk.Button(Div0Error, text="     OK     ", command=closeCustomDiv0)
    Div0Desc.place(x=150, y=100)
    Div0Symbol.place(x=10, y=10)
    Div0Exit.place(x=400, y=200)
def CustomInfo() :
    global CustomInfox
    CustomInfox = tk.Tk()
    CustomInfox.title("Info")
    infotext = "PraktiCalc\nVersion 1.3 (in development)\ntested in Python 3.11+\nLicensed under GPLv3\nread more at https://www.gnu.org/licenses/"
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
def CustomMsgBoxOn() :
    global CustomMsgBox, CustomMsgBoxToggle
    CustomMsgBox = 1
    CustomMsgBoxToggle.config(text="🗹", command=CustomMsgBoxOff)
def CustomMsgBoxOff() :
    global CustomMsgBox, CustomMsgBoxToggle
    CustomMsgBox = 0
    CustomMsgBoxToggle.config(text="☐", command=CustomMsgBoxOn)
def closeCustomInfo() :
    global CustomInfox
    CustomInfox.destroy()
def closeCustomDiv0() :
    global Div0Error
    Div0Error.destroy()
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
    style = ThemedStyle(MehrX)
    style.theme_use(usedttktheme)
    DezimalFrame = ttk.Frame(MehrX, height=50, width=435, relief="sunken", borderwidth=2)
    DezimalAnzeige = ttk.Entry(DezimalFrame, text="0")
    InsertButton = ttk.Button(MehrX, text="OK", command=paste)
    binFrame = ttk.Frame(MehrX, relief="sunken", borderwidth=2)
    hexFrame = ttk.Frame(MehrX, relief="sunken", borderwidth=2)
    binDesc = ttk.Label(binFrame, text="Binary")
    hexDesc = ttk.Label(hexFrame, text="Hexadecimal")
    BinaerLabel = ttk.Label(binFrame, text="")
    HexLabel = ttk.Label(hexFrame, text="")
    BinCopy = ttk.Button(binFrame, text="Copy", command=copybin)
    HexCopy = ttk.Button(hexFrame, text="Copy", command=copyhex)
    DezimalFrame.place(x=5, y=5)
    DezimalAnzeige.place(x=0, y=0)
    InsertButton.place(x=444, y=5, height=50, width=52)
    binFrame.place(x=5, y=60, height=135, width=240)
    hexFrame.place(x=250, y=60, height=135, width=245)
    binDesc.place(x=5, y=5)
    hexDesc.place(x=5, y=5)
    BinaerLabel.place(x=5, y=50)
    HexLabel.place(x=5, y=50)
    # BinCopy.place(x=5, y=100, width=225)
    # HexCopy.place(x=5, y=100, width=230)
def paste() :
    global DezimalZahl, DezimalAnzeige, BinaerZahl, HexadezimalZahl, BinaerLabel, HexLabel
    # win32clipboard.OpenClipboard()
    # cp = win32clipboard.GetClipboardData()
    # win32clipboard.CloseClipboard()
    cp = str(DezimalAnzeige.get())
    try:
        DezimalZahl = int(cp)
    except:
        messagebox.showerror("Error", "Please enter a real number!")
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
style = ThemedStyle(Fenster)
style.theme_use(usedttktheme)
Ausgaberahmen = ttk.Frame(Fenster, borderwidth=2, relief="sunken")
Ausgabe = ttk.Label(Ausgaberahmen, text="0")
# Buttons
PlusButton = ttk.Button(Fenster, text="➕", command=plus)
MinusButton = ttk.Button(Fenster, text="➖", command=minus)
MalButton = ttk.Button(Fenster, text="✖", command=mal)
GeteiltButton = ttk.Button(Fenster, text="➗", command=geteilt)
SiebenButton = ttk.Button(Fenster, text="7", command=sieben)
AchtButton = ttk.Button(Fenster, text="8", command=acht)
NeunButton = ttk.Button(Fenster, text="9", command=neun)
CEButton = ttk.Button(Fenster, text="CE", command=clear)
VierButton = ttk.Button(Fenster, text="4", command=vier)
FünfButton = ttk.Button(Fenster, text="5", command=fünf)
SechsButton = ttk.Button(Fenster, text="6", command=sechs)
KommaButton = ttk.Button(Fenster, text=",", command=komma)
EinsButton = ttk.Button(Fenster, text="1", command=eins)
ZweiButton = ttk.Button(Fenster, text="2", command=zwei)
DreiButton = ttk.Button(Fenster, text="3", command=drei)
GleichButton = ttk.Button(Fenster, text="=", command=calc)
InfoButton = ttk.Button(Fenster, text="i", command=info)
NullButton = ttk.Button(Fenster, text="0", command=null)
ExitButton = ttk.Button(Fenster, text="X", command=xquit)
Status = ttk.Label(Fenster, text="")
StatusDecoration = ttk.Label(Fenster, text="")
SettingsButton = ttk.Button(Fenster, text="🔧", command=Settings)
BackspaceButton = ttk.Button(Fenster, text="<", command=Backspace)
HistoryButton = ttk.Button(Fenster, text="📜", command=History)
MButton = ttk.Button(Fenster, text="±", command=mnus)
Checkb = ttk.Button(Fenster, text="Check", command=xcheck) # some debug thing
WurzelB = ttk.Button(Fenster, text="√", command=wurzelig)
Mehr = ttk.Button(Fenster, text="...", command=Meehr)
Ausgaberahmen.place(x=45, y=8, height=40, width=185)
Ausgabe.pack()
PlusButton.place(x=50, y=59, height=30, width=40)
MinusButton.place(x=100, y=59, height=30, width=40)
MalButton.place(x=150, y=59, height=30, width=40)
GeteiltButton.place(x=200, y=59, height=30, width=40)
SiebenButton.place(x=50, y=109, height=30, width=40)
AchtButton.place(x=100, y=109, height=30, width=40)
NeunButton.place(x=150, y=109, height=30, width=40)
CEButton.place(x=200, y=109, height=30, width=40)
VierButton.place(x=50, y=159, height=30, width=40)
FünfButton.place(x=100, y=159, height=30, width=40)
SechsButton.place(x=150, y=159, height=30, width=40)
KommaButton.place(x=200, y=159, height=30, width=40)
EinsButton.place(x=50, y=209, height=30, width=40)
ZweiButton.place(x=100, y=209, height=30, width=40)
DreiButton.place(x=150, y=209, height=30, width=40)
GleichButton.place(x=200, y=209, height=30, width=40)
InfoButton.place(x=0, y=0, height=30, width=40)
NullButton.place(x=50, y=259, height=30, width=90)
MButton.place(x=200, y=259, height=30, width=40)
WurzelB.place(x=150, y=259, height=30, width=40)
ExitButton.place(x=235, y=7, height=20, width=20)
Status.place(x=0, y=310)
StatusDecoration.place(x=0, y=295)
SettingsButton.place(x=0, y=32, height=30, width=40)
BackspaceButton.place(x=235, y=28, height=20, width=20)
HistoryButton.place(x=0, y=259, height=30, width=40)
Fenster.bind("<Key>", Tastendruck)
Mehr.place(x=0, y=225, height=30, width=40)
# Checkb.place(x=200, y=200)
Fenster.mainloop()
