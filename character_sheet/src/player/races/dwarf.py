from . import race


class Dwarf(race.Race):
    def __init__(self, race_spec):
        race.Race.__init__(self)
        assert(race_spec == None)
        self.speed = 5

        self.skills['exploration'] = 2
        self.skills['endurance'] = 2

        self.ability_scores['CON'] = 2
        self.ability_scores['WIS'] = 2
