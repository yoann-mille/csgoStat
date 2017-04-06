import datetime
from Match import Match
from enum import Enum


class MatchState(Enum):
    WARMUP = 'warmup'
    LIVE = 'live'
    OVER = 'gameover'

class ParserStat:

    def __init__(self):
        self.state = MatchState.WARMUP
        self.match = Match(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d_%Hh%M'))

    def parse_data(self, data):
        for key, val in data.items():
            if key == 'map':
                for key_map, val_map in val.items():
                    if key_map == 'mode' and val_map == 'competitive':
                        if key_map == 'phase' and val_map == MatchState.LIVE and self.state == MatchState.WARMUP:
                            self.state = MatchState.LIVE

                    if key_map == 'phase' and val_map == 'gameover' and self.is_warmup:
                        self.write_in_file(data)
