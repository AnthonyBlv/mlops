from aiokafka import AIOKafkaConsumer
import asyncio


async def func_consumer ():
    consumer = AIOKafkaConsumer('exo1', bootstrap_servers='51.38.185.58:9092')
    await consumer.start()
    async for message in consumer:
        print (message.value)




asyncio.run(func_consumer())