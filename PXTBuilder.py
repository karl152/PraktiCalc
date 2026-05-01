# PraktiXtension Builder
# Copyright (C) 2026 Karl "karl152"
# SPDX-License-Identifier: GPL-3.0

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
import hashlib, configparser, tempfile, shutil, zipfile

class PXTBuilder(ttk.Frame):
    def __init__(self, tabs, parent, mainWin, helper, calculator, dialog, DarkMode):
        super().__init__(tabs)
        self.file = ""
        self.InternetConnectionTkVar = tk.BooleanVar(value=False)
        self.minPyTkVar = tk.StringVar(value="default")
        self.maxPyTkVar = tk.StringVar(value="default")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(1, weight=1)
        for index, label in enumerate(["Name", "Version", "Description", "Website"]):
            ttk.Label(self, text=label + ":").grid(row=index, column=0, padx=10, sticky="w")
        self.NameEntry = ttk.Entry(self)
        self.VersionEntry = ttk.Entry(self)
        self.DescriptionEntry = ttk.Entry(self)
        self.WebsiteEntry = ttk.Entry(self)
        self.NameEntry.grid(row=0, column=1, padx=10, pady=10, sticky="we")
        self.DescriptionEntry.grid(row=2, column=1, padx=10, pady=10, sticky="we")
        self.WebsiteEntry.grid(row=3, column=1, padx=10, pady=10, sticky="we")
        self.VersionEntry.grid(row=1, column=1, padx=10, pady=10, sticky="we")
        self.PyVerFrame = ttk.LabelFrame(self, text="Python version")
        self.PythonVersions = ["default", "3.7", "3.8", "3.9", "3.10", "3.11", "3.12", "3.13", "3.14", "3.15"]
        self.minPySelect = ttk.OptionMenu(self.PyVerFrame, self.minPyTkVar, self.minPyTkVar.get(), *self.PythonVersions)
        self.maxPySelect = ttk.OptionMenu(self.PyVerFrame, self.maxPyTkVar, self.maxPyTkVar.get(), *self.PythonVersions)
        self.minPySelect.grid(row=0, column=1, pady=10)
        self.maxPySelect.grid(row=0, column=3, pady=10, padx=(0, 10))
        ttk.Label(self.PyVerFrame, text="minimal:").grid(row=0, column=0, padx=10)
        ttk.Label(self.PyVerFrame, text="maximal:").grid(row=0, column=2, padx=10)
        self.PyVerFrame.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        self.InternetConnectionCheckbox = ttk.Checkbutton(self, text="requires internet connection", variable=self.InternetConnectionTkVar)
        self.InternetConnectionCheckbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        self.LongDescriptionFrame = ttk.LabelFrame(self, text="Long Description")
        self.LongDescriptionFrame.rowconfigure(0, weight=1)
        self.LongDescriptionFrame.columnconfigure(0, weight=1)
        self.LongDescriptionText = tk.Text(self.LongDescriptionFrame)
        self.LongDescriptionText.grid(row=0, column=0, padx=10, pady=10, sticky="news")
        if DarkMode == True:
            self.LongDescriptionText.config(bg="black", fg="white")
        self.LongDescriptionFrame.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="news")
        self.ChoosePythonFileButton = ttk.Button(self, text="choose Python file", command=lambda: self.choosePyFile(parent))
        self.ChoosePythonFileButton.grid(row=1, column=2, padx=25)
        self.LicenseLabel = ttk.Label(self, text="License: ")
        self.SizeLabel = ttk.Label(self, text="Size: ")
        self.LicenseLabel.grid(row=2, column=2, sticky="w", padx=(25, 0))
        self.SizeLabel.grid(row=3, column=2, sticky="w", padx=(25, 0))
        self.ExportButton = ttk.Button(self, text="Export PXT", command=lambda: self.EXPORT(parent, helper, dialog))
        self.ExportButton.grid(row=6, column=2)
    def choosePyFile(self, parent):
        self.file = filedialog.askopenfilename(parent=parent, filetypes=[("Python Script", "*.py")])
        if not self.file == "" or self.file == ():
            with open(self.file, "r", encoding="utf-8") as extensionfile:
                content = extensionfile.read()
            if "SPDX-License-Identifier: " in content:
                self.LicenseLabel.config(text="License: " + content.split("SPDX-License-Identifier: ")[1].split()[0])
            else:
                self.LicenseLabel.config(text="License: ")
            self.SizeLabel.config(text="Size: " + str(Path(self.file).stat().st_size) + " Bytes")
        else:
            self.LicenseLabel.config(text="License: ")
            self.SizeLabel.config(text="Size: ")
    def EXPORT(self, parent, helper, dialog):
        if self.file == "" or self.file == ():
            dialog.error("no Python file selected", parent, helper)
            return
        if self.InternetConnectionTkVar.get() == True:
            self.InternetRequired = "true"
        else:
            self.InternetRequired = "false"
        with open(self.file, "rb") as ExtensionFile:
            sha256hash = hashlib.sha256(ExtensionFile.read()).hexdigest()
        ExtensionMetadata = configparser.ConfigParser()
        ExtensionMetadata["PraktiXtension"] = {"name": self.NameEntry.get(),
                                                          "version": self.VersionEntry.get(),
                                                          "filename": Path(self.file).name,
                                                          "description": self.DescriptionEntry.get(),
                                                          "website": self.WebsiteEntry.get(),
                                                          "minpython": self.minPyTkVar.get(),
                                                          "maxpython": self.maxPyTkVar.get(),
                                                          "sha256": sha256hash,
                                                          "requiresinternet": self.InternetRequired,
                                                          "pxtxlink": ""}
        LongDescription = self.LongDescriptionText.get("1.0", tk.END)
        with tempfile.TemporaryDirectory() as tempdir:
            shutil.copy2(self.file, Path(tempdir) / Path(self.file).name)
            with open(Path(tempdir) / "info.ini", "w", encoding="utf-8") as metadata:
                ExtensionMetadata.write(metadata)
            with open(Path(tempdir) / "description.txt", "w", encoding="utf-8") as DescriptionFile:
                DescriptionFile.write(LongDescription)
            TheZip = filedialog.asksaveasfilename(parent=parent, title="Export PraktiXtension >>>", initialdir=self.file[:-len(str(Path(self.file).name))+1], filetypes=[("PraktiXtension", "*.pxt")])
            if not TheZip.endswith(".pxt"):
                TheZip += ".pxt"
            with zipfile.ZipFile(TheZip, "w", compression=zipfile.ZIP_LZMA) as zf:
                for x in ["info.ini", "description.txt", Path(self.file).name]:
                    zf.write(Path(tempdir) / x, arcname=x)
                
