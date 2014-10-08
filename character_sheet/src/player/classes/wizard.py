from . import class_


class Wizard(class_.Class):
    def __init__(self, wizard_type):
        class_.Class.__init__(self)
        self.defs['ref'] = 1
        self.defs['will'] = 1
        self.spec = 'wizard_%s' % wizard_type
