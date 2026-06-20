' PraktiCalc © 2024-2026 Karl "karl152"
' Licensed under the GNU General Public License v3.0.
' See https://www.gnu.org/licenses/gpl-3.0.txt for details.
' SPDX-License-Identifier: GPL-3.0

Option Explicit
Dim PraktiCalcVersion, pyver, TkVersion, theming, ttkthemesText, VBSversionText
PraktiCalcVersion = WScript.Arguments(0)
pyver = WScript.Arguments(1)
TkVersion = WScript.Arguments(2)
theming = WScript.Arguments(3)

VBSversionText = ScriptEngine & " " & ScriptEngineMajorVersion & "." & ScriptEngineMinorVersion & "." & ScriptEngineBuildVersion

If theming <> "0" Then
    ttkthemesText = vbCrLf & "themes provided by the ttkthemes library"
Else
    ttkthemesText = ""
End If

MsgBox "PraktiCalc" & vbCrLf & "Version " & PraktiCalcVersion & vbCrLf & "running on Python " & pyver & " / Tk " & TkVersion & " / " & VBSversionText & vbCrLf & "Licensed under GPLv3" & vbCrLf & "read more at https://www.gnu.org/licenses/" & ttkthemesText, 64, "About PraktiCalc"