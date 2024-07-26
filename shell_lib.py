def makeConfig():
  import configparser
  config_file = configparser.ConfigParser()


  config_file.add_section("SteamWindowsShell")

  config_file.set("SteamWindowsShell", "ClientDir", "C:/Program Files (x86)/Steam")
  config_file.set("SteamWindowsShell", "ClientExe", "steam.exe")
  config_file.set("SteamWindowsShell", "ClientExeArg", "-noverifyfiles -gamepadui")

  with open(r"SteamWinShellconfig.ini", 'w') as configfileObj:
     config_file.write(configfileObj)
     configfileObj.flush()
     configfileObj.close()

  print("Config file 'SteamWinShellconfig.ini' created")

def maincode():
    import configparser
    import os
    import configHelper
    import subprocess
    import time
    import pathlib
    import sys
    import setshellkey

    explorerexe = "explorer.exe"

    setshellkey.SetAsShell(explorerexe)

    isSteamWinShellConfigEx = os.path.isfile("SteamWinShellconfig.ini")

    if isSteamWinShellConfigEx == False:
     makeConfig()

    config = configHelper.read_SteamWinShellconfig()

    ClientDir = config['SteamWindowsShell']['ClientDir']
    ClientExe = config['SteamWindowsShell']['ClientExe']
    ClientExeArg = config['SteamWindowsShell']['ClientExeArg']
    steamfiledir = f"{ClientDir}/{ClientExe}"
    isSteamInstall = os.path.isfile(steamfiledir)
    maindir = os.path.dirname(os.path.realpath(__file__))
    file_extension = pathlib.Path(__file__).suffix
    filenamemain = sys.executable
    print(filenamemain)

    runcmd = f"start {ClientExe} {ClientExeArg}"
    endtask = f"taskkill /f /im {ClientExe}"
    if isSteamInstall == False:
     subprocess.run(explorerexe)
    print(endtask)
    print(runcmd)
    subprocess.run(endtask)
    os.chdir(ClientDir)
    os.system(runcmd)
    time.sleep(20)
    subprocess.run(explorerexe)
    time.sleep(30)
    setshellkey.SetAsShell(filenamemain)