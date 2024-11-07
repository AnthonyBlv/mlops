import aiokafka
import asyncio
import json

async def produce():
    producer = aiokafka.AIOKafkaProducer(bootstrap_servers='51.38.185.58:9092',value_serializer=lambda v: json.dumps(v).encode())
    await producer.start()
    data = {"size": 250.0, "nb_rooms": 4, "garden": 1}
    await producer.send_and_wait('belval_exo4', data)
    await producer.stop()

asyncio.run(produce())