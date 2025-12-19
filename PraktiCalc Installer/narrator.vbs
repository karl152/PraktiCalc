' PraktiCalc © 2024-2025 Karl "karl152"
' Licensed under the GNU General Public License v3.0.
' See https://www.gnu.org/licenses/gpl-3.0.txt for details.

Option Explicit
Dim sapi
set sapi = CreateObject("sapi.spvoice")
sapi.Speak WScript.Arguments(0)