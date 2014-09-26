from . import class_


class Rogue(class_.Class):
    def __init__(self, rogue_type):
        class_.Class.__init__(self)
        self.defs['ref'] = 2
        self.spec = 'rogue_%s' % rogue_type
