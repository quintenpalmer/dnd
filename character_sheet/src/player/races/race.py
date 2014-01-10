import util
from util import name


class Race:
    def __init__(self):
        self.skills = {}
        for skill_name in util.skill_to_abil_mod_map.keys():
            self.skills[skill_name] = 0
        self.ability_scores = {}
        for sub_name in util.get_names():
            self.ability_scores[sub_name] = 0
        self.spec = None
