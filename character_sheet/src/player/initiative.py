import util
import specials


class Initiative:
    def __init__(self):
        self.misc = []

    def get_initiative(self, level, DEX):
        return (
            DEX +
            util.get_half_level(level) +
            sum(map(lambda x: specials.specials_map[x](), self.misc)))
