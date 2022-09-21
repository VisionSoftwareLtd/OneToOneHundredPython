from generator import Generator

class NumberGenerator(Generator):
    def __init__(self, minNum):
        super().__init__()
        self.x = minNum - 1

    def yieldIncrement(self):
        while True:
            self.x += 1
            yield self.x