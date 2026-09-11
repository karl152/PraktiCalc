' PraktiCalc © 2024-2026 Karl Wesseler
' Licensed under the GNU General Public License v3.0.
' See https://www.gnu.org/licenses/gpl-3.0.txt for details.
' SPDX-License-Identifier: GPL-3.0-only

Option Explicit
Dim PraktiCalcVersion, pyver, ToolkitVersion, PLEL, VBSversionText
PraktiCalcVersion = WScript.Arguments(0)
pyver = WScript.Arguments(1)
ToolkitVersion = WScript.Arguments(2)
PLEL = WScript.Arguments(3)

VBSversionText = ScriptEngineMajorVersion & "." & ScriptEngineMinorVersion & "." & ScriptEngineBuildVersion

If PLEL <> "0" Then
    MsgBox "PraktiCalc Legacy Extension Loader" & vbCrLf & "Powered by PraktiCalc " & PraktiCalcVersion & vbCrLf & "Copyright (C) 2024-2026 Karl Wesseler" & vbCrLf & "Running on Python " & pyver & " / Tk " & ToolkitVersion & " / " & ScriptEngine & " " & VBSversionText & vbCrLf & "Licensed under the GPLv3", 64, "About PLEL"
Else
    MsgBox "PraktiCalc - a practical calculator" & vbCrLf & "Version " & PraktiCalcVersion & vbCrLf & "Copyright (C) 2024-2026 Karl Wesseler" & vbCrLf & "Running on Python " & pyver & " / wxPython " & ToolkitVersion & " / VBS " & VBSversionText & vbCrLf & "Licensed under the GPLv3", 64, "About PraktiCalc"
End If
