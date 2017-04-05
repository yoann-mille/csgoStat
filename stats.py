import datetime


class ParserStat:

    def __init__(self, data):
        self.data = data

    def write_in_file(self):
        name_file = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d_%Hh%M')
        log = open(name_file, 'aw')
        log.write(str(self.data))
