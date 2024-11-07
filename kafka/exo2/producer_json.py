import aiokafka
import asyncio
import json

async def produce():
    producer = aiokafka.AIOKafkaProducer(bootstrap_servers='51.38.185.58:9092',value_serializer=lambda v: json.dumps(v).encode())
    await producer.start()
    data = {"data": [[1, 2,], [3, 4]]}
    await producer.send_and_wait('belval', data)
    await producer.stop()

asyncio.run(produce())