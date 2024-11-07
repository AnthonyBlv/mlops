from aiokafka import AIOKafkaConsumer
import asyncio
import numpy as np
import json


async def func_consumer ():
    consumer = AIOKafkaConsumer('processed_belval', bootstrap_servers='51.38.185.58:9092')
    await consumer.start()
    async for message in consumer:
        value = message.value
        print (value)

asyncio.run(func_consumer())