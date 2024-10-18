from broker import Broker
from publisher import Publisher
from subscriber import Subscriber

import threading
import random
import time

if __name__ == "__main__":
    broker = Broker()

    publishers = [Publisher(f"Publicador {i+1}", broker) for i in range(3)]
    for pub in publishers:
        pub.start()
    
    time.sleep(0.1)
    print("===" * 30)

    for i in range(5):
        topics = random.sample(list(broker.topic_queues), random.randint(1, 3))
        subscriber = Subscriber(f"Subscriber {i+1}", broker, topics)
        subscriber.start()
    
    time.sleep(0.1)
    print("===" * 30)

    broker_thread = threading.Thread(target=broker.distribute_messages)
    broker_thread.start()
