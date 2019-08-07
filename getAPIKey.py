import configparser

inifile = configparser.ConfigParser()
inifile.read('./config/config.ini', 'UTF-8')

def getAPIkey():
    return inifile.get('api_info', 'api_key')

def getAPIsecret():
    return inifile.get('api_info', 'api_secret')