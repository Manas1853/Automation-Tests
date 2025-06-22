import configparser

config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')    #here .\\ represents our current project directory

class ReadConfig:
    @staticmethod                # benefit of static method is that there is no need of creating an object of this class, this particular method we can use by directly class name
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password