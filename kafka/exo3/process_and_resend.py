import aiokafka
import asyncio
import json
import numpy as np

async def process_and_resend():
    consumer = aiokafka.AIOKafkaConsumer('belval', bootstrap_servers='51.38.185.58:9092')
    await consumer.start()
    producer = aiokafka.AIOKafkaProducer(bootstrap_servers='51.38.185.58:9092')
    await producer.start()
    async for message in consumer:
        value = message.value
        #check if the value can be converted to a numpy array
        try:
            jsn = value.decode('utf-8')
            jsn = json.loads(jsn)
            np_arr = np.array(jsn["data"])
            sum = np_arr.sum()
            print (f"Sum of {np_arr} is {sum}")
            await producer.send_and_wait('processed_belval', json.dumps({"sum": sum}).encode())
        except:
            print("The value is not a numpy array")
            continue

asyncio.run(process_and_resend())
        