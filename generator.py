class Generator:
    def increment(self):
        return next(self.yieldIncrement())

    def yieldIncrement(self):
        raise NotImplementedError