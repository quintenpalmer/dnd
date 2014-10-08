from . import class_


class Mage(class_.Class):
    def __init__(self, mage_type):
        class_.Class.__init__(self)
        self.defs['will'] = 2
        self.spec = 'mage_%s' % mage_type
