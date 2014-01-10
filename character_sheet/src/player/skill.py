class Skills:
    def __init__(self, trained_skills, misc_bonuses):
        self.trained = {}
        self.misc = {}
        for skill_name in trained_skills:
            self.trained[skill_name] = 5

        for skill_name, amount in misc_bonuses.items():
            self.misc[skill_name] = amount

    def get_skill(self, name, abil_mod):
        return (
            abil_mod +
            self._get_trained_amount(name) +
            self._get_misc_amount(name)
        )

    def _get_trained_amount(self, name):
        if name in self.trained:
            return self.trained[name]
        else:
            return 0

    def _get_misc_amount(self, name):
        if name in self.misc:
            return self.misc[name]
        else:
            return 0

