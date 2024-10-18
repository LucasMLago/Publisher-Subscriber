import threading
from broker import TOPICS
from colors import bcolors

class Subscriber(threading.Thread):
    def __init__(self, name, broker, topics):
        super().__init__()
        self.name = name
        self.broker = broker
        self.topics= topics

    def run(self):
        for topic in self.topics:
            self.broker.subscribe(self, topic)

    def receive_message(self, message):
        print(f"{bcolors.OKGREEN}[{self.name}]{bcolors.ENDC} received {message}")
