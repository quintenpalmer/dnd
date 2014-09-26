from . import race


class Elven(race.Race):
    def __init__(self, race_spec):
        race.Race.__init__(self)
        assert(race_spec == None)
        self.speed = 7

        self.skills['nature'] = 2
        self.skills['perception'] = 2

        self.ability_scores['DEX'] = 2
        self.ability_scores['WIS'] = 2
