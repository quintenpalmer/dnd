from . import class_


class Fighter(class_.Class):
    def __init__(self, fighter_type):
        class_.Class.__init__(self)
        self.defs['for'] = 2
        self.spec = 'fighter_%s' % fighter_type
