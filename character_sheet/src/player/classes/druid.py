from . import class_


class Druid(class_.Class):
    def __init__(self, primal_aspect):
        class_.Class.__init__(self)
        self.defs['ref'] = 1
        self.defs['will'] = 1
        self.spec = 'druid_%s' % primal_aspect
