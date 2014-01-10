class Speed:
    def __init__(self, base_speed):
        self.base_speed = base_speed
        self.misc = []

    def get_speed(self):
        return (
            self.base_speed +
            sum(map(lambda x: x(), self.misc)))
