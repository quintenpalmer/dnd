from . import race


class Halfling(race.Race):
    def __init__(self, race_spec):
        race.Race.__init__(self)
        assert(race_spec == None)
        self.speed = 6

        self.skills['acrobatics'] = 2
        self.skills['theivery'] = 2

        self.ability_scores['DEX'] = 2
        self.ability_scores['CHA'] = 2
