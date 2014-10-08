from . import class_


class Paladin(class_.Class):
    def __init__(self, channel_divinity):
        class_.Class.__init__(self)
        self.defs['ref'] = 1
        self.defs['will'] = 1
        self.defs['fort'] = 1
        self.spec = 'paladin_%s' % channel_divinity
