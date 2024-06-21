from configparser import ConfigParser

config = ConfigParser()

#config.read('C:/Users/Ashish/PycharmProjects/pythonProject/Python Automation/config.cfg') OR
#config.read('../Python Automation/config.cfg') OR
config.read('config.cfg')

print(config.get('section','username'))