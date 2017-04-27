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

class ParserStat:
    now = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d_%Hh%M')
    match = Match(now, '')

    def __init__(self):
        self.frame = 0
        self.state = MatchState.WARMUP
        self.round_count = 0
        self.mvps = 0
        self.scores = 0

    def parse_data(self, post_data):
        self.frame = Frame(post_data)

        if 'map' in self.frame.__dict__:
            if self.frame.map['phase'] == MatchState.WARMUP.value:
                print("warmup")
                return 0
            elif self.frame.map['phase'] == MatchState.LIVE.value:
                print("LIVE")
                # First round

                if self.state.value != MatchState.LIVE.value:
                    self.state = MatchState.LIVE
                    print(self.frame.map['name'])
                    self.match.update_map(self.frame.map['name'])
                    #self.match.map = self.frame.map['name']

                    """
                    self.round_count = self.frame.map['round']
                    
                    team = 'T'
                    if 'team' in self.frame.player:
                        team = self.frame.player['team']
                    self.round = Round(team,
                                       self.frame.map['team_ct']['score'],
                                       self.frame.map['team_t']['score'],
                                       self.frame.map['round'])
                    """
                if self.frame.player['steamid'] == config.Steam['yupin_id']:
                    print("[YUPIN]")
                    #print(self.frame.__dict__)
                    if self.frame.round['phase'] == 'over':
                        print("[ROUND_OVER]")
                        print(self.frame.__dict__)
                        player = self.frame.player
                        map = self.frame.map
                        side = self.frame.player['team']
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
                """       
                 #  All round for a specific player id

                    player = self.frame.player

                    #   New Round

                    if self.round.nbr != self.frame.map['round']:
                        self.match.add_round(copy.copy(self.round))
                        self.round.reset(self.frame.player['team'],
                                       self.frame.map['team_ct']['score'],
                                       self.frame.map['team_t']['score'],
                                       self.frame.map['round'])
                    else:

                        #  Same round
                        print("SAME ROUND")
                        stats = player['match_stats']
                        assist = stats.assists - self.round.assist
                        death = stats.deaths - self.round.death
                        score = stats.score - self.scores
                        mvp = stats.mvp - self.mvps
                        self.round.update(player['team'], player.state.round_kill, player.state.round_killhs, assist, death, score, mvp)
                        self.mvps = stats.mvp
                        self.scores = stats.score
                """
            elif self.frame.map['phase'] == MatchState.OVER.value:

                # Export vers db
                print("[GAME_OVER]")
                #print("match json")
                #print(json.dumps(self.match))
                print("match self")
                print(self.match.__dict__)
                print("Match")
                print(Match.__dict__)
                print("END")
                print("END")