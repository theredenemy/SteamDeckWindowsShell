import ctypes, os
import sys
try:
    is_admin = os.getuid() == 0
except AttributeError:
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

print(is_admin)

if is_admin == True:
    import setshellkey
    import ctypes
    explorerexe = "explorer.exe"
    setshellkey.SetAsShell(explorerexe)
    ctypes.windll.user32.MessageBoxW(0, "Reverted Shell Back to explorer.exe.", "SteamDeckWindowsShell", 0)
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
