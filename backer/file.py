import os
import tarfile
from time import strftime, localtime


class FileBacker:
    def __init__(self, setting):
        self.setting = setting
        tar_name = strftime("%Y-%m-%d-%H%M%S", localtime()) + '.tar.gz'
        tar_file = os.path.join(setting['backup_dir'], tar_name)
        self.tar = tarfile.open(tar_file, 'w|gz')

    def is_exclude(self, name):
        for reg in self.setting['exclude'].split(','):
            if reg == name:
                return True
        return False

    def backup_dir(self, path):
        for item in os.listdir(path):
            file = os.path.join(path, item)
            if not self.is_exclude(item):
                if os.path.isfile(file):
                    self.tar.add(file)
                else:
                    self.backup_dir(file)

    def backup(self):
        for path in self.setting['include'].split(','):
            self.backup_dir(os.path.join(self.setting['root_dir'], path))
        return self.tar.name

    def __del__(self):
        self.tar.close()
