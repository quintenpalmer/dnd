from . import race


class Eladrin(race.Race):
    def __init__(self, race_spec):
        race.Race.__init__(self)
        assert(race_spec is None)
        self.speed = 6

        self.skills['arcana'] = 2
        self.skills['history'] = 2

        self.ability_scores['DEX'] = 2
        self.ability_scores['INT'] = 2