from kafka import KafkaConsumer
import os
topic = os.environ["TOPIC"]
consumer = KafkaConsumer(topic, bootstrap_servers='kafka-svc-external:9092', auto_offset_reset='latest', group_id = None, enable_auto_commit=False)
for message in consumer:
    message=(message.value).decode("utf-8")
    values = message.split(";")
    if float(values[1])>= 15.0 and float(values[1])<=28.0:
        print("------------Verze 1------------------")
        print("Identifikátor instance:",os.environ["HOSTNAME"])
        print("Senzor:", values[0])
        print("Teplota:", values[1],"°C")
        print("-------------------------------------")
