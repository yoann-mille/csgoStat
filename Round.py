class Round:

    def __init__(self, side, t_score, ct_score, nbr, kill, killHS, assist, death, score, mvp):
        self.side = side
        self.t_score = t_score
        self.ct_score = ct_score
        self.nbr = nbr
        self.kill = kill
        self.killHS = killHS
        self.assist = assist
        self.death = death
        self.score = score
        self.mvp = mvp

    def update(self, kill, killHS, assist, death, score, mvp):
        self.kill = kill
        self.killHS = killHS
        self.assist += assist
        self.death += death
        self.score += score
        self.mvp += mvp

    def reset(self, team, team_ct, team_t, round):
        self.side = team
        self.t_score = team_ct
        self.ct_score = team_t
        self.nbr = round
        self.kill = 0
        self.killHS = 0
        self.assist = 0
        self.death = 0
        self.score = 0
        self.mvp = 0
