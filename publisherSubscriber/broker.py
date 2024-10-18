import queue
import threading
import time
import random
from colors import bcolors

TOPICS = ["sports", "news", "technology"]

class Broker:
    def __init__(self):
        self.topic_queues = {topic: queue.Queue() for topic in TOPICS}
        self.subscribers = {topic: [] for topic in TOPICS}
        self.lock = threading.Lock()

    def subscribe(self, subscriber, topic):
        with self.lock:
            self.subscribers[topic].append(subscriber)
            print(f"{subscriber.name} subscribed to topic ---> {topic}")

    def publish_message(self, topic, message):
        with self.lock:
            if len(self.subscribers[topic]) == 0:
                warning = f"{bcolors.WARNING}[Message discarded]{bcolors.ENDC} {message}. No subscribers for topic: {bcolors.OKPURPLE}[{topic}]{bcolors.ENDC}"
                print(f"{warning}")
            else:
                self.topic_queues[topic].put(message)
                print(f"Message published to topic {topic}, {message}")

    def distribute_messages(self):
        while True:
            for topic, queue_ in self.topic_queues.items():
                if not queue_.empty():
                    message = queue_.get()
                    with self.lock:
                        for subscriber in self.subscribers[topic]:
                            subscriber.receive_message(message)
            time.sleep(1)
