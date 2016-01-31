from config import *
import importlib


if __name__ == '__main__':
    config = Config().get()
    for obj in config['common']['backup'].split(','):
        module = importlib.import_module('backer.' + obj)
        class_name = getattr(module, obj.capitalize() + 'Backer')
        config[obj]['backup_dir'] = config['common']['backup_dir']
        backer = class_name(config[obj])
        backer.backup()




