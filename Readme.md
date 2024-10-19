# Publisher/Subscriber System Simulation with Threads

This project is a simulation of an inter-process communication system that implements the *Publisher/Subscriber* model using *Threads* in Python. In the *Publisher/Subscriber* model, publishers send messages to specific topics, while subscribers receive only messages from the topics they are subscribed to. An intermediary, called the *Broker*, is responsible for managing and distributing the messages to the subscribers.

## Objective

The goal of this project is to demonstrate how processes (represented by threads) can communicate efficiently, using topics to organize and filter messages. The system simulates the periodic publishing of messages by publishers and the delivery of these messages to subscribers interested in specific topics.

## System Structure

The system consists of three main types of threads:

1. **Publisher (Producer):** Periodically publishes messages to specific topics.
2. **Subscriber (Client):** Subscribes to one or more topics and receives the messages published to those topics.
3. **Broker:** An intermediary that manages the messages sent to topics and distributes them to the registered subscribers.

## How It Works

- **Publisher:** Randomly generates messages for one of the available topics (e.g., "sports", "news", "technology") and sends them to the *Broker*. Messages are generated at random time intervals.
- **Subscriber:** Each subscriber registers for one or more topics at the start of the execution. The subscriber then waits for messages sent by the *Broker* to the topics they are subscribed to.
- **Broker:** Receives messages from the publishers and checks which subscribers are registered for the topics of those messages. It distributes the messages to the correct subscribers. If there are no subscribers for a topic, the message is discarded.

## Running the Simulation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/LucasMLago/Publisher-Subscriber.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Publisher-Subscriber
   ```

3. **Run the main script:**
   ```bash
   python publisherSubscriber/pubsub.py
   ```

## Expected Output

The simulation will run with multiple publishers and subscribers, demonstrating the message flow between them. You will see messages being published to different topics and received by the corresponding subscribers. The output will include information about the publisher, subscriber, topic, and message content.

![GIF engraçado](gif/pubsub_output_gif.gif)