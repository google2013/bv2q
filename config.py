import configparser


class Config:
    def __init__(self, config_file='config.ini'):
        config = configparser.ConfigParser()
        config.read(config_file)
        self.config = {}
        for section in config.sections():
            tmp = {}
            for option in config.options(section):
                tmp[option] = config.get(section, option)
            self.config[section] = tmp

    def get(self):
        return self.config
