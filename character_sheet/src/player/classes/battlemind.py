from . import class_


class Battlemind(class_.Class):
    def __init__(self, psionic_type):
        class_.Class.__init__(self)
        self.defs['will'] = 2
        self.spec = 'psionic_%s' % psionic_type
