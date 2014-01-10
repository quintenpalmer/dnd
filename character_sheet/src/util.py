import importlib

class Name:
    def __init__(self):
        self.STR = 'STR'
        self.CON = 'CON'
        self.DEX = 'DEX'
        self.INT = 'INT'
        self.WIS = 'WIS'
        self.CHA = 'CHA'

name = Name()

skill_to_abil_mod_map = {
    'acrobatics': name.DEX,
    'arcana': name.INT,
    'athletics': name.STR,
    'bluff': name.CHA,
    'diplomacy': name.CHA,
    'dungeoneering': name.WIS,
    'endurance': name.CON,
    'heal': name.WIS,
    'history': name.INT,
    'insight': name.WIS,
    'intimidate': name.CHA,
    'nature': name.WIS,
    'perception': name.WIS,
    'religion': name.INT,
    'stealth': name.DEX,
    'streetwise': name.CHA,
    'theivery': name.DEX,
}


def get_names():
    return filter(lambda x: not x.startswith('__'), dir(name))


def load_module(super_name, sub_name, spec):
    return getattr(
        importlib.import_module('player.%s.%s' % (super_name, sub_name.lower())), sub_name)(spec)


def get_half_level(level):
    return int(rounded_lower_even(level) / 2)


def get_abil_mod(raw_ability):
    return int((rounded_lower_even(raw_ability) - 10) / 2)


def is_even(number):
    return (number % 2) == 0


def rounded_lower_even(number):
    if not is_even(number):
        return number - 1
    else:
        return number
