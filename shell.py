import ctypes, os
import sys
try:
 is_admin = os.getuid() == 0
except AttributeError:
 is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

print(is_admin)

if is_admin == True:
 import shell_lib
 shell_lib.maincode()
else:
 ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


