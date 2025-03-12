def makeConfig():
  import configparser
  config_file = configparser.ConfigParser()


  config_file.add_section("SteamWindowsShell")

  config_file.set("SteamWindowsShell", "ClientDir", "C:/Program Files (x86)/Steam")
  config_file.set("SteamWindowsShell", "ClientExe", "steam.exe")
  config_file.set("SteamWindowsShell", "ClientExeArg", "-noverifyfiles -gamepadui")
  config_file.set("SteamWindowsShell", "waitforpro", "steamwebhelper.exe")

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
    import processchecklib

    explorerexe = "explorer.exe"

    setshellkey.SetAsShell(explorerexe)

    isSteamWinShellConfigEx = os.path.isfile("SteamWinShellconfig.ini")

    if isSteamWinShellConfigEx == False:
     makeConfig()

    config = configHelper.read_SteamWinShellconfig()

    ClientDir = config['SteamWindowsShell']['ClientDir']
    ClientExe = config['SteamWindowsShell']['ClientExe']
    ClientExeArg = config['SteamWindowsShell']['ClientExeArg']
    waitforpro = config['SteamWindowsShell']['waitforpro']
    steamfiledir = f"{ClientDir}/{ClientExe}"
    isSteamInstall = os.path.isfile(steamfiledir)
    maindir = os.path.dirname(os.path.realpath(__file__))
    file_extension = pathlib.Path(__file__).suffix
    filenamemain = sys.executable
    print(filenamemain)

    runcmd = f"start {ClientExe} {ClientExeArg}"
    endtask = f"taskkill /f /im {ClientExe}"
    if isSteamInstall == True:
      print(endtask)
      print(runcmd)
      subprocess.run(endtask)
      os.chdir(ClientDir)
      os.system(runcmd)
      processloop = 0
      while (processloop < 1):
        if processchecklib.process_check(waitforpro) == True:
          processloop = 1
        else:
          time.sleep(3)
      time.sleep(3)
      subprocess.run(explorerexe)
      time.sleep(5)
      setshellkey.SetAsShell(filenamemain)
    else:
      subprocess.run(explorerexe) 