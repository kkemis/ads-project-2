from kafka import KafkaProducer
import os
import random
import time
topic = os.environ["TOPIC"]
locations = ["loznice","koupelna","obyvak","kuchyne","garaz","sklep"]
producer = KafkaProducer(bootstrap_servers='kafka-svc-external:9092')
while True:
    msg = random.choice(locations)+";"+str(round(random.uniform(10.0,30.0),1))
    producer.send(topic, msg.encode())
    producer.flush()
    print("------------------------------")    
    print(msg)
    print("------------------------------")      
    time.sleep(2)