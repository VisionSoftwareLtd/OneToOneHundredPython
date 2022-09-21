from dataprinter import DataPrinter
from observableproducer import ObservableProducer

def printNumbers():
    dataPrinter = DataPrinter()
    producer = ObservableProducer()
    producer.subscribe(dataPrinter)
    producer.doWork()

if __name__ == '__main__':
    printNumbers()
