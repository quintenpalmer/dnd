from . import race


class Tiefling(race.Race):
    def __init__(self, race_spec):
        race.Race.__init__(self)
        assert(race_spec is None)
        self.speed = 6

        self.skills['bluff'] = 2
        self.skills['stealth'] = 2

        self.ability_scores['INT'] = 2
        self.ability_scores['CHA'] = 2
