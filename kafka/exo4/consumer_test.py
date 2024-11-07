import aiokafka
import asyncio


async def process_and_resend():
    consumer = aiokafka.AIOKafkaConsumer('predict_belval', bootstrap_servers='51.38.185.58:9092')
    await consumer.start()
    producer = aiokafka.AIOKafkaProducer(bootstrap_servers='51.38.185.58:9092')
    await producer.start()
    async for message in consumer:
        value = message.value
        print(value)
        

asyncio.run(process_and_resend())