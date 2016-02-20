class MysqlBacker:
    def __init__(self, setting):
        self.setting = setting

    def backup(self):
        if not self.setting['db_name']:
            pass
        else:
            pass

