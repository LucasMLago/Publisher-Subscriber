import threading
import random
import time
from broker import TOPICS
from colors import bcolors

class Publisher(threading.Thread):
    def __init__(self, name, broker):
        super().__init__()
        self.name = name
        self.broker = broker

    def run(self):
        while True:
            topic = random.choice(TOPICS)
            message = f"message from {bcolors.OKBLUE}[{self.name}]{bcolors.ENDC} about {bcolors.OKPURPLE}[{topic}]{bcolors.ENDC}"
            self.broker.publish_message(topic, message)
            time.sleep(random.randint(2, 10))
