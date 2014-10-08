from . import class_


class Ranger(class_.Class):
    def __init__(self, combat_style):
        class_.Class.__init__(self)
        self.defs['ref'] = 1
        self.defs['fort'] = 1
        self.spec = 'ranger_%s' % combat_style
