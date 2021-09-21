import configparser

config=configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getAppUrl():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getProdUrl():
        produrl=config.get('common info','AppProdUrl')
        return produrl

    @staticmethod
    def getemail():
        email=config.get('common info','email')
        return email