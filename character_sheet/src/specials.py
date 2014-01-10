def improve_initiative():
    return 4

def new_ac_selector(player):
    def _get_ac_abil_mod(self):
        if not self.wearing_heavy():
            return max(map(
                lambda x: player.get_abil_mod,
                name.DEX, name.INT, name.CON))
        else:
            return max(map(
                lambda x: player.get_abil_mod,
                name.DEX, name.INT))
    player.defenses._get_ac_abil_mod = _get_ac_abil_mod

def new_speed_improver(player):
    def primal_predator_speed():
        if not player.wearing_heavy():
            return 1
        else:
            return 0
    player.speed.misc.append(primal_predator_speed)

specials_map = {
    '4_init': improve_initiative,
    'druid_guardian': new_ac_selector,
    'druid_predator': new_speed_improver,
}
