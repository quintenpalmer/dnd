from . import race


class HalfElf(race.Race):
    def __init__(self, race_spec):
        race.Race.__init__(self)
        assert(race_spec is None)
        self.speed = 7

        self.skills['diplomacy'] = 2
        self.skills['insight'] = 2

        self.ability_scores['CON'] = 2
        self.ability_scores['CHA'] = 2