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
from tkinter import *
from tkinter import messagebox
import win32clipboard
# Variablen definieren
Eingabe1 = "0"
Eingabe2 = "0"
Stage = 0
Operator = "op"
StatusBar = 0
CustomMsgBox = 1
DarkMode = 1
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
        messagebox.showinfo("PraktiCalc 1.2.1 vom 10.08.2025, lizensiert unter GPLv3", "This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.")
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
                        messagebox.showerror("Fehler", "Division durch 0")
                    if CustomMsgBox == 1 :
                        CustomDiv0()
                if StatusBar == 1 :
                    Status.config(text="Fehler: Division durch 0")
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
    SettingsWindow = Tk()
    SettingsWindow.title("Einstellungen")
    if DarkMode == 1 :
        SettingsWindow.config(width=250, height=152, bg="black")
        SettingsTitle = Label(SettingsWindow, text="Einstellungen", font=("Liberation Sans", 12), bg="black", fg="white")
        SettingsTitleDecoration = Label(SettingsWindow, text="▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀", font=("Courier New", 12), bg="black", fg="white")
        StatusBarSettingDesc = Label(SettingsWindow, text="Statusleiste", bg="black", fg="white")
        if StatusBar == 0 :
            StatusBarToggle = Button(SettingsWindow, text="☐", command=StatusBarOn, bg="black", fg="white")
        if StatusBar == 1 :
            StatusBarToggle = Button(SettingsWindow, text="🗹", command=StatusBarOff, bg="black", fg="white")
        CustomStatusBarDesc = Label(SettingsWindow, text="Alternative Messageboxen", bg="black", fg="white")
        if CustomMsgBox == 0 :
            CustomMsgBoxToggle = Button(SettingsWindow, text="☐", command=CustomMsgBoxOn, bg="black", fg="white")
        if CustomMsgBox == 1 :
            CustomMsgBoxToggle = Button(SettingsWindow, text="🗹", command=CustomMsgBoxOff, bg="black", fg="white")
        DarkModeToggle = Button(SettingsWindow, text="🗹", command=DarkModeOff, bg="black", fg="white")
        DarkModeDesc = Label(SettingsWindow, text="Dark Mode", bg="black", fg="white")
    if DarkMode == 0 :
        SettingsWindow.config(width=250, height=152)
        SettingsTitle = Label(SettingsWindow, text="Einstellungen", font=("Liberation Sans", 12))
        SettingsTitleDecoration = Label(SettingsWindow, text="▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀", font=("Courier New", 12))
        StatusBarSettingDesc = Label(SettingsWindow, text="Statusleiste")
        if StatusBar == 0 :
            StatusBarToggle = Button(SettingsWindow, text="☐", command=StatusBarOn)
        if StatusBar == 1 :
            StatusBarToggle = Button(SettingsWindow, text="🗹", command=StatusBarOff)
        CustomStatusBarDesc = Label(SettingsWindow, text="Alternative Messageboxen")
        if CustomMsgBox == 0 :
            CustomMsgBoxToggle = Button(SettingsWindow, text="☐", command=CustomMsgBoxOn)
        if CustomMsgBox == 1 :
            CustomMsgBoxToggle = Button(SettingsWindow, text="🗹", command=CustomMsgBoxOff)
        DarkModeToggle = Button(SettingsWindow, text="☐", command=DarkModeOn)
        DarkModeDesc = Label(SettingsWindow, text="Dark Mode")
    SettingsTitle.place(x=0, y=0)
    SettingsTitleDecoration.place(x=0, y=24)
    StatusBarSettingDesc.place(x=30, y=45)
    StatusBarToggle.place(x=5, y=45)
    CustomStatusBarDesc.place(x=30, y=72)
    CustomMsgBoxToggle.place(x=5, y=72)
    DarkModeToggle.place(x=5, y=99)
    DarkModeDesc.place(x=30, y=99)
def StatusBarOn() :
    global Status, StatusBar, StatusBarToggle, StatusDecoration, Fenster
    Fenster.config(width=256, height=330)
    Status.config(text="Bereit")
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
    Div0Error = Tk()
    Div0Error.title("Fehler")
    if DarkMode == 1 :
        Div0Error.config(width=500, height=250, bg="black")
        Div0Desc = Label(Div0Error, text="Division durch 0", font=("Liberation Sans", 15), bg="black", fg="white")
        Div0Symbol = Label(Div0Error, text="🚫", font=("Segoe UI Symbol", 52), bg="black", fg="white")
        Div0Exit = Button(Div0Error, text="     OK     ", command=closeCustomDiv0, bg="black", fg="white")
    if DarkMode == 0 :
        Div0Error.config(width=500, height=250)
        Div0Desc = Label(Div0Error, text="Division durch 0", font=("Liberation Sans", 15))
        Div0Symbol = Label(Div0Error, text="🚫", font=("Segoe UI Symbol", 52))
        Div0Exit = Button(Div0Error, text="     OK     ", command=closeCustomDiv0)
    Div0Desc.place(x=150, y=100)
    Div0Symbol.place(x=10, y=10)
    Div0Exit.place(x=400, y=200)
def CustomInfo() :
    global CustomInfox
    CustomInfox = Tk()
    CustomInfox.title("Info")
    if DarkMode == 1 :
        CustomInfox.config(width=500, height=250, bg="black")
        CustomInfoDesc = Label(CustomInfox, text="PraktiCalc", font=("Liberation Sans", 15), bg="black", fg="white")
        CustomInfoSymbol = Label(CustomInfox, text="ℹ", font=("Segoe UI Symbol", 52), bg="black", fg="white")
        CustomInfoExit = Button(CustomInfox, text="     OK     ", command=closeCustomInfo, bg="black", fg="white")
        ExtendedInfoFrame = Frame(CustomInfox, relief="sunken", borderwidth=2, bg="black")
        ExtInfoText1 = Label(ExtendedInfoFrame, text="PraktiCalc", bg="black", fg="white")
        ExtInfoText2 = Label(ExtendedInfoFrame, text="Version 1.2.1 vom 10.08.2025", bg="black", fg="white")
        ExtInfoText3 = Label(ExtendedInfoFrame, text="Entstanden als Praktikumsprojekt", bg="black", fg="white")
        ExtInfoText4 = Label(ExtendedInfoFrame, text="getestet in Python 3.13.6 (Windows)", bg="black", fg="white")
        ExtInfoText5 = Label(ExtendedInfoFrame, text="Lizenz: GPLv3, weitere Infos auf https://www.gnu.org/licenses/", bg="black", fg="white")
    if DarkMode == 0 :
        CustomInfox.config(width=500, height=250)
        CustomInfoDesc = Label(CustomInfox, text="PraktiCalc", font=("Liberation Sans", 15))
        CustomInfoSymbol = Label(CustomInfox, text="ℹ", font=("Segoe UI Symbol", 52))
        CustomInfoExit = Button(CustomInfox, text="     OK     ", command=closeCustomInfo)
        ExtendedInfoFrame = Frame(CustomInfox, relief="sunken", borderwidth=2)
        ExtInfoText1 = Label(ExtendedInfoFrame, text="PraktiCalc")
        ExtInfoText2 = Label(ExtendedInfoFrame, text="Version 1.2.1 vom 10.08.2025")
        ExtInfoText3 = Label(ExtendedInfoFrame, text="Entstanden als Praktikumsprojekt")
        ExtInfoText4 = Label(ExtendedInfoFrame, text="getestet in Python 3.13.6 (Windows)")
        ExtInfoText5 = Label(ExtendedInfoFrame, text="Lizenz: GPLv3, weitere Infos auf https://www.gnu.org/licenses/")
    CustomInfoDesc.place(x=150, y=25)
    CustomInfoSymbol.place(x=10, y=10)
    CustomInfoExit.place(x=400, y=200)
    ExtendedInfoFrame.place(x=100, y=55, height=125, width=357)
    ExtInfoText1.place(x=5, y=5)
    ExtInfoText2.place(x=5, y=25)
    ExtInfoText3.place(x=5, y=45)
    ExtInfoText4.place(x=5, y=65)
    ExtInfoText5.place(x=5, y=85)
def CustomMsgBoxOn() :
    global CustomMsgBox, CustomMsgBoxToggle
    CustomMsgBox = 1
    CustomMsgBoxToggle.config(text="🗹", command=CustomMsgBoxOff)
def CustomMsgBoxOff() :
    global CustomMsgBox, CustomMsgBoxToggle
    CustomMsgBox = 0
    CustomMsgBoxToggle.config(text="☐", command=CustomMsgBoxOn)
def DarkModeOn() :
    global DarkMode, DarkModeToggle, SettingsWindow
    DarkMode = 1
    DarkModeToggle.config(text="🗹", command=DarkModeOff)
    SettingsWindow.destroy()
    Fenster.config(bg="black")
    Ausgaberahmen.config(bg="black")
    Ausgabe.config(bg="black", fg="white")
    PlusButton.config(bg="black", fg="white")
    MinusButton.config(bg="black", fg="white")
    MalButton.config(bg="black", fg="white")
    GeteiltButton.config(bg="black", fg="white")
    SiebenButton.config(bg="black", fg="white")
    AchtButton.config(bg="black", fg="white")
    NeunButton.config(bg="black", fg="white")
    CEButton.config(bg="black", fg="white")
    VierButton.config(bg="black", fg="white")
    FünfButton.config(bg="black", fg="white")
    SechsButton.config(bg="black", fg="white")
    KommaButton.config(bg="black", fg="white")
    EinsButton.config(bg="black", fg="white")
    ZweiButton.config(bg="black", fg="white")
    DreiButton.config(bg="black", fg="white")
    GleichButton.config(bg="black", fg="white")
    InfoButton.config(bg="black", fg="white")
    NullButton.config(bg="black", fg="white")
    Status.config(bg="black", fg="white")
    StatusDecoration.config(bg="black", fg="white")
    SettingsButton.config(bg="black", fg="white")
    BackspaceButton.config(bg="black", fg="white")
    HistoryButton.config(bg="black", fg="white")
    MButton.config(bg="black", fg="white")
    WurzelB.config(bg="black", fg="white")
    Mehr.config(bg="black", fg="white")
    Settings()
    # messagebox.showwarning("Problem", "Bitte DarkMode im Code auf 1 stellen")
def DarkModeOff() :
    global DarkMode, DarkModeToggle, SettingsWindow
    DarkMode = 0
    DarkModeToggle.config(text="☐", command=DarkModeOn)
    SettingsWindow.destroy()
    Fenster.config(bg="white")
    Ausgaberahmen.config(bg="white")
    Ausgabe.config(bg="white", fg="black")
    PlusButton.config(bg="white", fg="black")
    MinusButton.config(bg="white", fg="black")
    MalButton.config(bg="white", fg="black")
    GeteiltButton.config(bg="white", fg="black")
    SiebenButton.config(bg="white", fg="black")
    AchtButton.config(bg="white", fg="black")
    NeunButton.config(bg="white", fg="black")
    CEButton.config(bg="white", fg="black")
    VierButton.config(bg="white", fg="black")
    FünfButton.config(bg="white", fg="black")
    SechsButton.config(bg="white", fg="black")
    KommaButton.config(bg="white", fg="black")
    EinsButton.config(bg="white", fg="black")
    ZweiButton.config(bg="white", fg="black")
    DreiButton.config(bg="white", fg="black")
    GleichButton.config(bg="white", fg="black")
    InfoButton.config(bg="white", fg="black")
    NullButton.config(bg="white", fg="black")
    Status.config(bg="white", fg="black")
    StatusDecoration.config(bg="white", fg="black")
    SettingsButton.config(bg="white", fg="black")
    BackspaceButton.config(bg="white", fg="black")
    HistoryButton.config(bg="white", fg="black")
    MButton.config(bg="white", fg="black")
    WurzelB.config(bg="white", fg="black")
    Mehr.config(bg="white", fg="black")
    Settings()
    # messagebox.showwarning("Problem", "Bitte DarkMode im Code auf 0 stellen")
def closeCustomInfo() :
    global CustomInfox
    CustomInfox.destroy()
def closeCustomDiv0() :
    global Div0Error
    Div0Error.destroy()
def SizeReload() :
    if Stage == 0 :
        Ausgabe.config(font=("Courier New", 25))
    if Stage == 1 :
        if len(str(Eingabe1)) == 9 :
            Ausgabe.config(font=("Courier New", 22))
        if len(str(Eingabe1)) == 10 :
            Ausgabe.config(font=("Courier New", 20))
        if len(str(Eingabe1)) == 11 :
            Ausgabe.config(font=("Courier New", 18))
        if len(str(Eingabe1)) == 12 :
            Ausgabe.config(font=("Courier New", 17))
        if len(str(Eingabe1)) == 13 :
            Ausgabe.config(font=("Courier New", 15))
        if len(str(Eingabe1)) == 14 :
            Ausgabe.config(font=("Courier New", 14))
        if len(str(Eingabe1)) == 15 :
            Ausgabe.config(font=("Courier New", 13))
        if len(str(Eingabe1)) >= 16 :
            Ausgabe.config(font=("Courier New", 13))
            ZeichenStatus()
    if Stage == 2 :
        if len(str(Eingabe1)) == 9 :
            Ausgabe.config(font=("Courier New", 22))
        if len(str(Eingabe1)) == 10 :
            Ausgabe.config(font=("Courier New", 20))
        if len(str(Eingabe1)) == 11 :
            Ausgabe.config(font=("Courier New", 18))
        if len(str(Eingabe1)) == 12 :
            Ausgabe.config(font=("Courier New", 17))
        if len(str(Eingabe1)) == 13 :
            Ausgabe.config(font=("Courier New", 15))
        if len(str(Eingabe1)) == 14 :
            Ausgabe.config(font=("Courier New", 14))
        if len(str(Eingabe1)) == 15 :
            Ausgabe.config(font=("Courier New", 13))
        if len(str(Eingabe1)) >= 16 :
            ZeichenStatus()
    if Stage == 3 :
        Ausgabe.config(font=("Courier New", 25))
    if Stage == 4 :
        if len(str(Eingabe2)) == 9 :
            Ausgabe.config(font=("Courier New", 22))
        if len(str(Eingabe2)) == 10 :
            Ausgabe.config(font=("Courier New", 20))
        if len(str(Eingabe2)) == 11 :
            Ausgabe.config(font=("Courier New", 18))
        if len(str(Eingabe2)) == 12 :
            Ausgabe.config(font=("Courier New", 17))
        if len(str(Eingabe2)) == 13 :
            Ausgabe.config(font=("Courier New", 15))
        if len(str(Eingabe2)) == 14 :
            Ausgabe.config(font=("Courier New", 14))
        if len(str(Eingabe2)) == 15 :
            Ausgabe.config(font=("Courier New", 13))
        if len(str(Eingabe2)) >= 16 :
            ZeichenStatus()
    if Stage == 5 :
        if len(str(Eingabe2)) == 9 :
            Ausgabe.config(font=("Courier New", 22))
        if len(str(Eingabe2)) == 10 :
            Ausgabe.config(font=("Courier New", 20))
        if len(str(Eingabe2)) == 11 :
            Ausgabe.config(font=("Courier New", 18))
        if len(str(Eingabe2)) == 12 :
            Ausgabe.config(font=("Courier New", 17))
        if len(str(Eingabe2)) == 13 :
            Ausgabe.config(font=("Courier New", 15))
        if len(str(Eingabe2)) == 14 :
            Ausgabe.config(font=("Courier New", 14))
        if len(str(Eingabe2)) == 15 :
            Ausgabe.config(font=("Courier New", 13))
        if len(str(Eingabe2)) >= 16 :
            ZeichenStatus()
    if Stage == 6 :
        if len(str(EndErgebnis)) == 9 :
            Ausgabe.config(font=("Courier New", 22))
        if len(str(EndErgebnis)) == 10 :
            Ausgabe.config(font=("Courier New", 20))
        if len(str(EndErgebnis)) == 11 :
            Ausgabe.config(font=("Courier New", 18))
        if len(str(EndErgebnis)) == 12 :
            Ausgabe.config(font=("Courier New", 17))
        if len(str(EndErgebnis)) == 13 :
            Ausgabe.config(font=("Courier New", 15))
        if len(str(EndErgebnis)) == 14 :
            Ausgabe.config(font=("Courier New", 14))
        if len(str(EndErgebnis)) == 15 :
            Ausgabe.config(font=("Courier New", 13))
        if len(str(EndErgebnis)) >= 16 :
            ZeichenStatus()
def ZeichenStatus() :
    global Status, StatusBar
    if StatusBar == 1 :
        Status.config(text="Der Rechner unterstützt maximal 15 Zeichen!")
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
    HistoryX = Tk()
    HistoryX.title("Verlauf")
    if DarkMode == 1 :
        HistoryX.config(height=400, width=256, bg="black")
        HistoryLabel = Label(HistoryX, text="Verlauf", font=("Liberation Sans", 12), bg="black", fg="white")
        Hostory1 = Label(HistoryX, text=History1, bg="black", fg="white")
        Hostory2 = Label(HistoryX, text=History2, bg="black", fg="white")
        Hostory3 = Label(HistoryX, text=History3, bg="black", fg="white")
        Hostory4 = Label(HistoryX, text=History4, bg="black", fg="white")
        Hostory5 = Label(HistoryX, text=History5, bg="black", fg="white")
        Hostory6 = Label(HistoryX, text=History6, bg="black", fg="white")
        Hostory7 = Label(HistoryX, text=History7, bg="black", fg="white")
        Hostory8 = Label(HistoryX, text=History8, bg="black", fg="white")
        Hostory9 = Label(HistoryX, text=History9, bg="black", fg="white")
        Hostory10 = Label(HistoryX, text=History10, bg="black", fg="white")
        Hostory11 = Label(HistoryX, text=History11, bg="black", fg="white")
        Hostory12 = Label(HistoryX, text=History12, bg="black", fg="white")
        Hostory13 = Label(HistoryX, text=History13, bg="black", fg="white")
        Hostory14 = Label(HistoryX, text=History14, bg="black", fg="white")
        Hostory15 = Label(HistoryX, text=History15, bg="black", fg="white")
        ClearButton = Button(HistoryX, text="🗑", font=("Liberation Sans", 12), command=clearHistory, bg="black", fg="white")
    if DarkMode == 0 :
        HistoryX.config(height=400, width=256)
        HistoryLabel = Label(HistoryX, text="Verlauf", font=("Liberation Sans", 12))
        Hostory1 = Label(HistoryX, text=History1)
        Hostory2 = Label(HistoryX, text=History2)
        Hostory3 = Label(HistoryX, text=History3)
        Hostory4 = Label(HistoryX, text=History4)
        Hostory5 = Label(HistoryX, text=History5)
        Hostory6 = Label(HistoryX, text=History6)
        Hostory7 = Label(HistoryX, text=History7)
        Hostory8 = Label(HistoryX, text=History8)
        Hostory9 = Label(HistoryX, text=History9)
        Hostory10 = Label(HistoryX, text=History10)
        Hostory11 = Label(HistoryX, text=History11)
        Hostory12 = Label(HistoryX, text=History12)
        Hostory13 = Label(HistoryX, text=History13)
        Hostory14 = Label(HistoryX, text=History14)
        Hostory15 = Label(HistoryX, text=History15)
        ClearButton = Button(HistoryX, text="🗑", font=("Liberation Sans", 12), command=clearHistory)
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
    global DarkMode, MehrX, DezimalFrame, DezimalAnzeige, DezimalZahl, BinaerLabel, HexLabel
    MehrX = Tk()
    MehrX.title("Mehr")
    if DarkMode == 1 :
        MehrX.config(height=200, width=500, bg="black")
        DezimalFrame = Frame(MehrX, height=50, width=435, bg="black", relief="sunken", borderwidth=2)
        DezimalAnzeige = Label(DezimalFrame, text="0", font=("Courier New", 24), bg="black", fg="white")
        InsertButton = Button(MehrX, text="Einfügen", command=paste, bg="black", fg="white")
        binFrame = Frame(MehrX, bg="black", relief="sunken", borderwidth=2)
        hexFrame = Frame(MehrX, bg="black", relief="sunken", borderwidth=2)
        binDesc = Label(binFrame, text="Binär", font=("Courier", 15), bg="black", fg="white")
        hexDesc = Label(hexFrame, text="Hexadezimal", font=("Courier", 15), bg="black", fg="white")
        BinaerLabel = Label(binFrame, text="", font=("Courier", 15), bg="black", fg="white")
        HexLabel = Label(hexFrame, text="", font=("Courier", 15), bg="black", fg="white")
        BinCopy = Button(binFrame, text="Kopieren", command=copybin, bg="black", fg="white")
        HexCopy = Button(hexFrame, text="Kopieren", command=copyhex, bg="black", fg="white")
    if DarkMode == 0 :
        MehrX.config(height=200, width=500)
        DezimalFrame = Frame(MehrX, height=50, width=435, relief="sunken", borderwidth=2)
        DezimalAnzeige = Label(DezimalFrame, text="0", font=("Courier New", 24))
        InsertButton = Button(MehrX, text="Einfügen", command=paste)
        binFrame = Frame(MehrX, relief="sunken", borderwidth=2)
        hexFrame = Frame(MehrX, relief="sunken", borderwidth=2)
        binDesc = Label(binFrame, text="Binär", font=("Courier", 15))
        hexDesc = Label(hexFrame, text="Hexadezimal", font=("Courier", 15))
        BinaerLabel = Label(binFrame, text="", font=("Courier", 15))
        HexLabel = Label(hexFrame, text="", font=("Courier", 15))
        BinCopy = Button(binFrame, text="Kopieren", command=copybin)
        HexCopy = Button(hexFrame, text="Kopieren", command=copyhex)
    DezimalFrame.place(x=5, y=5)
    DezimalAnzeige.place(x=0, y=0)
    InsertButton.place(x=444, y=5, height=50, width=52)
    binFrame.place(x=5, y=60, height=135, width=240)
    hexFrame.place(x=250, y=60, height=135, width=245)
    binDesc.place(x=5, y=5)
    hexDesc.place(x=5, y=5)
    BinaerLabel.place(x=5, y=50)
    HexLabel.place(x=5, y=50)
    BinCopy.place(x=5, y=100, width=225)
    HexCopy.place(x=5, y=100, width=230)
def paste() :
    global DezimalZahl, DezimalAnzeige, BinaerZahl, HexadezimalZahl, BinaerLabel, HexLabel
    win32clipboard.OpenClipboard()
    cp = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    DezimalZahl = int(cp)
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
# Hauptfenster
Fenster = Tk()
Fenster.title("PraktiCalc")
if DarkMode == 1 :
    Fenster.config(width=256, height=315, bg="black")
    Ausgaberahmen = Frame(Fenster, borderwidth=2, relief="sunken", bg="black")
    Ausgabe = Label(Ausgaberahmen, text="0", font=("Courier New", 25), bg="black", fg="white")
    # Buttons
    PlusButton = Button(Fenster, text="➕", font=("Courier New", 12), command=plus, bg="black", fg="white")
    MinusButton = Button(Fenster, text="➖", font=("Courier New", 12), command=minus, bg="black", fg="white")
    MalButton = Button(Fenster, text="✖", font=("Courier New", 12), command=mal, bg="black", fg="white")
    GeteiltButton = Button(Fenster, text="➗", font=("Courier New", 12), command=geteilt, bg="black", fg="white")
    SiebenButton = Button(Fenster, text="7", font=("Courier New", 12), command=sieben, bg="black", fg="white")
    AchtButton = Button(Fenster, text="8", font=("Courier New", 12), command=acht, bg="black", fg="white")
    NeunButton = Button(Fenster, text="9", font=("Courier New", 12), command=neun, bg="black", fg="white")
    CEButton = Button(Fenster, text="CE", font=("Courier New", 12), command=clear, bg="black", fg="white")
    VierButton = Button(Fenster, text="4", font=("Courier New", 12), command=vier, bg="black", fg="white")
    FünfButton = Button(Fenster, text="5", font=("Courier New", 12), command=fünf, bg="black", fg="white")
    SechsButton = Button(Fenster, text="6", font=("Courier New", 12), command=sechs, bg="black", fg="white")
    KommaButton = Button(Fenster, text=",", font=("Courier New", 12), command=komma, bg="black", fg="white")
    EinsButton = Button(Fenster, text="1", font=("Courier New", 12), command=eins, bg="black", fg="white")
    ZweiButton = Button(Fenster, text="2", font=("Courier New", 12), command=zwei, bg="black", fg="white")
    DreiButton = Button(Fenster, text="3", font=("Courier New", 12), command=drei, bg="black", fg="white")
    GleichButton = Button(Fenster, text="=", font=("Courier New", 12), command=calc, bg="black", fg="white")
    InfoButton = Button(Fenster, text="i", font=("Courier New", 12), command=info, bg="black", fg="white")
    NullButton = Button(Fenster, text="0", font=("Courier New", 12), command=null, bg="black", fg="white")
    ExitButton = Button(Fenster, text="X",font=("Courier New", 12), bg="red", fg="white", command=xquit)
    Status = Label(Fenster, text="", bg="black", fg="white")
    StatusDecoration = Label(Fenster, text="", bg="black", fg="white")
    SettingsButton = Button(Fenster, text="🔧", font=("Courier New", 10), command=Settings, bg="black", fg="white")
    BackspaceButton = Button(Fenster, text="<", font=("Courier New", 7), command=Backspace, bg="black", fg="white")
    HistoryButton = Button(Fenster, text="📜", font=("Courier New", 12), command=History, bg="black", fg="white")
    Checkb = Button(Fenster, text="Check", command=xcheck)
    MButton = Button(Fenster, text="±", font=("Courier New", 12), command=mnus, bg="black", fg="white")
    WurzelB = Button(Fenster, text="√", font=("Courier New", 12), command=wurzelig, bg="black", fg="white")
    Mehr = Button(Fenster, text="...", font=("Courier New", 12), command=Meehr, bg="black", fg="white")
if DarkMode == 0 :
    Fenster.config(width=256, height=315)
    Ausgaberahmen = Frame(Fenster, borderwidth=2, relief="sunken")
    Ausgabe = Label(Ausgaberahmen, text="0", font=("Courier New", 25))
    # Buttons
    PlusButton = Button(Fenster, text="➕", font=("Courier New", 12), command=plus)
    MinusButton = Button(Fenster, text="➖", font=("Courier New", 12), command=minus)
    MalButton = Button(Fenster, text="✖", font=("Courier New", 12), command=mal)
    GeteiltButton = Button(Fenster, text="➗", font=("Courier New", 12), command=geteilt)
    SiebenButton = Button(Fenster, text="7", font=("Courier New", 12), command=sieben)
    AchtButton = Button(Fenster, text="8", font=("Courier New", 12), command=acht)
    NeunButton = Button(Fenster, text="9", font=("Courier New", 12), command=neun)
    CEButton = Button(Fenster, text="CE", font=("Courier New", 12), command=clear)
    VierButton = Button(Fenster, text="4", font=("Courier New", 12), command=vier)
    FünfButton = Button(Fenster, text="5", font=("Courier New", 12), command=fünf)
    SechsButton = Button(Fenster, text="6", font=("Courier New", 12), command=sechs)
    KommaButton = Button(Fenster, text=",", font=("Courier New", 12), command=komma)
    EinsButton = Button(Fenster, text="1", font=("Courier New", 12), command=eins)
    ZweiButton = Button(Fenster, text="2", font=("Courier New", 12), command=zwei)
    DreiButton = Button(Fenster, text="3", font=("Courier New", 12), command=drei)
    GleichButton = Button(Fenster, text="=", font=("Courier New", 12), command=calc)
    InfoButton = Button(Fenster, text="i", font=("Courier New", 12), command=info)
    NullButton = Button(Fenster, text="0", font=("Courier New", 12), command=null)
    ExitButton = Button(Fenster, text="X",font=("Courier New", 12), bg="red", fg="white", command=xquit)
    Status = Label(Fenster, text="")
    StatusDecoration = Label(Fenster, text="")
    SettingsButton = Button(Fenster, text="🔧", font=("Courier New", 10), command=Settings)
    BackspaceButton = Button(Fenster, text="<", font=("Courier New", 7), command=Backspace)
    HistoryButton = Button(Fenster, text="📜", font=("Courier New", 12), command=History)
    MButton = Button(Fenster, text="±", font=("Courier New", 12), command=mnus)
    Checkb = Button(Fenster, text="Check", command=xcheck) # some debug thing
    WurzelB = Button(Fenster, text="√", font=("Courier New", 12), command=wurzelig)
    Mehr = Button(Fenster, text="...", font=("Courier New", 12), command=Meehr)
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