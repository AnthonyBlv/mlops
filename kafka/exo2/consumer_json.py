from aiokafka import AIOKafkaConsumer
import asyncio
import numpy as np
import json


async def func_consumer ():
    consumer = AIOKafkaConsumer('belval', bootstrap_servers='51.38.185.58:9092')
    await consumer.start()
    async for message in consumer:
        value = message.value
        jsn = value.decode('utf-8')
        jsn = json.loads(jsn)
        np_arr = np.array(jsn["data"])
        sum = np_arr.sum()
        print (f"Sum of {np_arr} is {sum}")

asyncio.run(func_consumer())