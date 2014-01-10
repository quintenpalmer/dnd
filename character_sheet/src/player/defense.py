import util
from util import name


class Defenses:
    def __init__(self):
        self.misc = []
        self.abil_mod_mapping = {
            'AC': [name.DEX, name.INT],
            'fort': [name.STR, name.CON],
            'ref': [name.DEX, name.INT],
            'will': [name.WIS, name.CHA],
        }


    #TODO don't pass the whole player
    def get_defense(self, player, name):
        return (
            10 +
            util.get_half_level(player.level) +
            max(map(
                lambda x: player.get_abil_mod(x),
                self.abil_mod_mapping[name])) +
            player.class_.defs[name]
            ) # TODO add armor feat enh misc misc
