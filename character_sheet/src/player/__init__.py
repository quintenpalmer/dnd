import json

import util
import specials
from util import name

from . import ability
from . import defense
from . import speed
from . import skill
from . import initiative
from . import sense


class Player:
    def __init__(
            self,
            character_name,
            class_, race,
            STR, CON, DEX, INT, WIS, CHA,
            trained_skills,
            feats,
            level,
            race_spec=None,
            class_spec=None):
        self.name = character_name
        self.level = level
        self.race = util.load_module('races', race, race_spec)
        self.class_  = util.load_module('classes', class_, class_spec)
        self.initiative = initiative.Initiative()
        self.ability_scores = ability.AbilityScores(
            STR, CON, DEX, INT, WIS, CHA)
        self.defenses = defense.Defenses()
        self.skills = skill.Skills(trained_skills, self.race.skills)
        self.speed = speed.Speed(self.race.speed)
        self.feats = list(map(
            lambda feat: util.load_module('feats', feat, None), feats))
        self.senses = sense.Senses()

        if self.class_.spec is not None:
            specials.specials_map[self.class_.spec](self)
        if self.race.spec is not None:
            specials.specials_map[self.race.spec](self)
        list(map(lambda feat: feat.special(self), self.feats))

    def get_raw_abil(self, name):
        return self.ability_scores.get_raw_abil(
            name,
            self.race.ability_scores)

    def get_abil_mod(self, name):
        return self.ability_scores.get_abil_mod(
            name,
            self.race.ability_scores)

    def get_defense(self, name):
        return self.defenses.get_defense(self, name)

    def get_initiative(self):
        return self.initiative.get_initiative(
            self.level,
            self.get_abil_mod(name.DEX))

    def get_skill(self, name):
        return self.skills.get_skill(
            name,
            self.get_abil_mod(util.skill_to_abil_mod_map[name]))

    def get_passive_perception(self):
        return self.senses.get_passive_perception(self.get_skill('perception'))

    def get_passive_insight(self):
        return self.senses.get_passive_insight(self.get_skill('insight'))

    def get_speed(self):
        return self.speed.get_speed()

    def wearing_heavy(self):
        #TODO TODO TODO
        return False

    def serialize(self):
        json_map = {
            'class_': self.class_.__class__.__name__,
            'race': self.race.__class__.__name__,
            'character_name': self.name,
            'level': self.level,
        }
        for sub_name in util.get_names():
            json_map[sub_name] = self.ability_scores.scores[sub_name]
        json_map['trained_skills'] = self.skills.trained.keys()
        json_map['feats'] = list(map(lambda x: x.__class__.__name__, self.feats))
        if self.class_.spec is not None:
            json_map['class_spec'] = self.class_.spec.lstrip('%s_' % self.class_.__class__.__name__)
        return json.dumps(json_map)

    def __repr__(self):
        ret = 'level : %s\n' % self.level
        ret += 'initiative : %s\n' % self.get_initiative()
        ret += 'speed  : %s\n' % self.get_speed()
        for sub_name in util.get_names():
            ret += '%s      : %s\n' % (sub_name, self.get_abil_mod(sub_name))
            ret += '%s(raw) : %s\n' % (sub_name, self.get_raw_abil(sub_name))
        for attr in sorted(util.skill_to_abil_mod_map.keys()):
            ret += '%s : %s\n' % (attr, self.get_skill(attr))
        ret += 'AC : %s\n' % self.get_defense('AC')
        ret += 'FORT: %s\n' % self.get_defense('fort')
        ret += 'REF: %s\n' % self.get_defense('ref')
        ret += 'WILL : %s\n' % self.get_defense('will')
        ret += 'passive insight : %s\n' % self.get_passive_insight()
        ret += 'passive perception : %s\n' % self.get_passive_perception()
        return ret
