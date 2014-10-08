from . import class_


class Cleric(class_.Class):
    def __init__(self, channel_divinity):
        class_.Class.__init__(self)
        self.defs['will'] = 2
        self.spec = 'cleric_%s' % channel_divinity