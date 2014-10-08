from . import race


class Dragonborn(race.Race):
    def __init__(self, race_spec):
        race.Race.__init__(self)
        assert(race_spec is None)
        self.speed = 6

        self.skills['history'] = 2
        self.skills['intimidate'] = 2

        self.ability_scores['STR'] = 2
        self.ability_scores['CHA'] = 2
