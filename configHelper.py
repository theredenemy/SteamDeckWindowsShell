import configparser

# Method to read config file settings
def read_SteamWinShellconfig():
    config = configparser.ConfigParser()
    config.read('SteamWinShellconfig.ini')
    return config