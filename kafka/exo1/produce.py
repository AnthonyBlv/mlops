import aiokafka
import asyncio

async def produce():
    producer = aiokafka.AIOKafkaProducer(bootstrap_servers='51.38.185.58:9092')
    await producer.start()
    await producer.send_and_wait('exo1', b'Meme pas un peu ?!')
    await producer.stop()

asyncio.run(produce())
