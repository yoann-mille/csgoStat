import datetime
import json
import copy
from Match import Match
from Round import Round
from enum import Enum
import config


class Frame(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)


class MatchState(Enum):
    WARMUP = 'warmup'
    LIVE = 'live'
    OVER = 'gameover'
    SWAP = 'intermission'


class ParserStat:
    now = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d_%Hh%M')
    match = Match(now, '')

    def __init__(self):
        self.frame = 0
        self.state = MatchState.WARMUP
        self.round_count = 0
        self.mvps = 0
        self.scores = 0

    def parse_round(self):
        player = self.frame.player
        map = self.frame.map
        side = self.frame.player['team'] if 'team' in self.frame.player else 0
        print('SIDE', side)
        t_score = map['team_t']['score']
        ct_score = map['team_ct']['score']
        nbr = map['round']
        kill = player['state']['round_kills'] if 'round_kills' in player['state'] else 0
        killhs = player['state']['round_killhs'] if 'round_killhs' in player['state'] else 0
        assist = player['state']['round_assists'] if 'round_assists' in player['state'] else 0
        death = player['state']['round_death'] if 'round_death' in player['state'] else 0
        score = player['match_stats']['score'] if 'score' in player['match_stats'] else 0
        mvp = player['match_stats']['mvps'] if 'mvps' in player['match_stats'] else 0
        self.match.add_round(copy.copy(Round(side, t_score, ct_score, nbr, kill, killhs, assist, death, score, mvp)))

    def parse_data(self, post_data):
        self.frame = Frame(post_data)
        if not ('previously' in self.frame.__dict__):
            return 0
        if 'map' in self.frame.__dict__:
            if self.state != MatchState.LIVE and self.frame.round['phase'] == MatchState.LIVE.value:
                print('LIVE')
                self.state = MatchState.LIVE
                self.match.update_map(self.frame.map['name'])
            print('[FRAME]')
            print(self.frame.__dict__)
            if self.frame.map['phase'] == MatchState.WARMUP.value:
                print("warmup")
                return 0
            elif self.state == MatchState.LIVE and self.frame.map['phase'] == MatchState.LIVE.value:
                # First round
                if self.frame.player['steamid'] == config.Steam['yupin_id']:
                    if self.frame.round['phase'] == 'over' and not ('phase' in self.frame.previously['map']):
                        print("[ROUND_OVER]")
                        self.parse_round()
            elif self.state == MatchState.LIVE and self.frame.map['phase'] == MatchState.SWAP.value and not ('phase' in self.frame.previously['map']):
                print('SWAP')
                self.parse_round()
            elif self.state != MatchState.WARMUP and self.frame.map['phase'] == MatchState.OVER.value:
                self.state = MatchState.WARMUP
                self.parse_round()
                # Export vers db
                print("[GAME_OVER]")
                print(self.match.__dict__)
                for rnd in self.match.rounds:
                    print(rnd.__dict__)
                print("END")
                print("END")
