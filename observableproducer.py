from producer import Producer

class ObservableProducer:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            pass

    def notify(self, data):
        for observer in self.observers:
            observer.update(data)

    def doWork(self):
        numberProducer = Producer(1, 100)
        numberIterator = iter(numberProducer)
        for number in numberIterator:
            self.notify(number)
