import pykka

__author__ = 'mBAR'


class Messenger(pykka.ThreadingActor):
    amount = 0
    print("Messenger")
    def write(self, message):
        print(message)
