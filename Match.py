import Round
import datetime


class Match:
    def __init__(self, date, map_name):
        self.date = date
        self.rounds = []
        self.rounds_t = []
        self.rounds_ct = []
        self.map = map_name
        self.kill = 0
        self.killHS = 0
        self.assist = 0
        self.death = 0
        self.score = 0

    def write_in_file(self):
        name_file = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d_%Hh%M')
        log = open(name_file, 'a')
        log.write(self)

    def add_round(self, new_round):

        self.rounds.append(new_round)
        self.killHS += new_round.killHS

    def update_map(self, map):
        self.map = map

    def update(self, kill, assist, death, score):
        self.kill = kill
        self.assist = assist
        self.death = death
        self.score = score

    def clear(self):
        self.date = ''
        self.rounds = []
        self.map = ''
        self.kill = 0
        self.killHS = 0
        self.assist = 0
        self.death = 0
        self.score = 0