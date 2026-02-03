' PraktiCalc © 2024-2026 Karl "karl152"
' Licensed under the GNU General Public License v3.0.
' See https://www.gnu.org/licenses/gpl-3.0.txt for details.
' SPDX-License-Identifier: GPL-3.0

Option Explicit
Dim PraktiCalcVersion, pyver
PraktiCalcVersion = WScript.Arguments(0)
pyver = WScript.Arguments(1)
MsgBox "PraktiCalc" & vbCrLf & "Version " & PraktiCalcVersion & vbCrLf & "running on Python " & pyver & vbCrLf & "Licensed under GPLv3" & vbCrLf & "read more at https://www.gnu.org/licenses/" & vbCrLf & "themes provided by the ttkthemes library", 64, "About PraktiCalc"
