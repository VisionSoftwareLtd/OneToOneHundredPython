from numbergenerator import NumberGenerator

class Producer:
    def __init__(self, minNum, maxNum):
        self.generator = NumberGenerator(minNum)
        self.maxNum = maxNum

    def __iter__(self):
        return self

    def __next__(self):
        a = self.generator.increment()
        if a < self.maxNum + 1:
            return a
        else:
            raise StopIteration