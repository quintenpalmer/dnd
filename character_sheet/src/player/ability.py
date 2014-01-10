import util


class AbilityScores:
    def __init__(self, STR, CON, DEX, INT, WIS, CHA):
        self.scores = {
            'STR': STR,
            'CON': CON,
            'DEX': DEX,
            'INT': INT,
            'WIS': WIS,
            'CHA': CHA,
        }

    def get_abil_mod(self, name, ability_scores):
        return util.get_abil_mod(self.scores[name] + ability_scores[name])

    def get_raw_abil(self, name, ability_scores):
        return self.scores[name] + ability_scores[name]
