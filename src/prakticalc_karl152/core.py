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

from pathlib import Path
import platform, subprocess, sys, shutil, math, configparser
if platform.system() == "Windows":
    import winreg
elif platform.system() == "Darwin":
    import plistlib

class Configuration:
    def __init__(self):
        if platform.system() == "Windows":
            if RunningAsOneFileExe == True:
                if sys.executable == r"C:\Program Files\PraktiCalc\prakticalc.exe":
                    self.backend = WindowsConfig()
                else:
                    self.backend = XDGConfig()
            else:
                self.backend = WindowsConfig()
        elif platform.system() == "Darwin":
            self.backend = MacConfig()
        else:
            self.backend = XDGConfig()
        try:
            detectedConfigVersion = str(self.get("configVersion"))
            if detectedConfigVersion == "None":
                detectedConfigVersion = str(self.get("configVersion"))
            try:
                float(detectedConfigVersion)
            except:
                fail = True
                return
            if detectedConfigVersion == "1.0":
                fail = False
                return
            elif float(detectedConfigVersion) != 1.0:
                fail = True
        except:
            fail = False
        finally:
            if fail == True:
                try:
                    self.reset()
                except:
                    pass
                finally:
                    self.create()
    def get(self, key): # reads a value and returns it
        try:
            return self.backend.get(key)
        except:
            try:
                self.reset()
            except:
                pass
            finally:
                self.create()
    def set(self, key, value): # sets a value and returns it
        try:
            self.backend.set(key, value)
        except:
            try:
                self.reset()
            except:
                pass
            finally:
                self.create()
    def create(self): # creates local configuration storage
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
                                    ("nativeMenuBar", True),
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
    def reset(self): # deletes local configuration storage
        self.backend.reset()
    def remove(self, key): # deletes a value from configuration
        try:
            self.backend.remove(key)
        except:
            pass

# Windows configuration backend
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
                messagebox.showerror("Error writing configuration")
    def create(self):
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\PraktiCalc")
    def reset(self):
        print(subprocess.getoutput(r'reg delete "HKEY_CURRENT_USER\Software\PraktiCalc" /f'))
    def remove(self, key):
        with winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\PraktiCalc", 0, winreg.KEY_SET_VALUE) as PraktiKey:
            winreg.DeleteValue(PraktiKey, key)

# macOS configuration backend
class MacConfig:
    def __init__(self):
        self.folder = Path.home() / "Library" / "Preferences"
        self.filepath = self.folder / "de.karl_52.PraktiCalc.plist"
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

# INI configuration backend
class XDGConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        if platform.system() == "Windows":
            f1 = Path(sys.executable).parent
            self.folder = f1 / "settings"
        else:
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
        self.HistoryList.append(f"{self.CalculationString}\t=\t{Result}")
        self.CalculationString = Result
        self.LastResult = Result
        return Result
    def zero(self): # processes the number zero, which is a special case and seperate
        if self.LastResult != "0":
            self.CalculationString = "0"
        elif self.CalculationString != "0":
            self.CalculationString += "0"
    def clear(self): # resets the calculaton
        self.CalculationString = "0"
        self.LastResult = "0"
    def append(self, char): # append a character to the calculation string
        replacements = {
            "plus": "+",
            "minus": "-",
            "asterisk": "*",
            "slash": "/",
            "period": ".",
            "comma": ".",
            ",": ".",
            "parenleft": "(",
            "parenright": ")",
            "percent": "%",
            "exclam": "fact(",
            "!": "fact("
            }
        for val in replacements:
            char = char.replace(val, replacements.get(val))
        if self.CalculationString == "0" and char != ".":
            self.CalculationString = char
        elif self.LastResult != "0" and char not in "+-*/%":
            self.CalculationString = char
        else:
            self.CalculationString += char
        self.LastResult = "0"
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
    def appendToMemory(self): # appends the calculation string to memory
        if self.CalculationString != "0":
            if self.Memory == "0":
                self.Memory = ""
            self.Memory += self.CalculationString
    def addToMemory(self): # adds the calculation string to memory
        self.Memory = self.quickCalc(f"({self.Memory})+({self.CalculationString})")
    def subtractFromMemory(self): # subtracts the calculation string from memory
        self.Memory = self.quickCalc(f"({self.Memory})-({self.CalculationString})")
    def clearMemory(self):
        self.Memory = "0"
    def clearHistory(self): # clears the history list
        self.HistoryList.clear()
    def xcheck(self): # debug function to return some variables
        return self.CalculationString, self.Memory, self.LastResult, self.HistoryList, self.operators
    def quickCalc(self, expression): # calculates an entire calculation string and returns the result
        PreviousResult = self.LastResult
        PreviousCalculationString = self.CalculationString
        self.clear()
        self.setOperators("rad")
        self.append(expression)
        try:
            result = self.calculate()
        except Exception:
            raise Exception
        finally:
            self.clear()
            self.HistoryList.pop()
            self.LastResult = PreviousResult
            self.CalculationString = PreviousCalculationString
            self.setOperators(self.TrigMode)
        return result
    def setOperators(self, TrigMode): # defines all the additional operators
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
    def updateFromSettings(self, cfg): # applies settings
        self.TrigMode = cfg.get("angleUnit") # rad, deg, gon
        self.setOperators(self.TrigMode)
        self.Rounding = bool(cfg.get("roundResult"))
        self.no0 = bool(cfg.get("showTrailing0"))
