import aiokafka
import asyncio
import json
import model_utils

async def process_and_resend():
    model = model_utils.load_model()
    consumer = aiokafka.AIOKafkaConsumer('belval_exo4', bootstrap_servers='51.38.185.58:9092',group_id="MyGreatConsumerGroup")
    await consumer.start()
    async for message in consumer:
        print("je l'ai")
        await asyncio.sleep(5)
        producer = aiokafka.AIOKafkaProducer(bootstrap_servers='51.38.185.58:9092',value_serializer=lambda v: json.dumps(v).encode())
        await producer.start()
        value = message.value
        jsn = value.decode('utf-8')
        jsn = json.loads(jsn)
        input = [jsn["size"], jsn["nb_rooms"], jsn["garden"]]

        prediction = model_utils.predict(model,input)
        await producer.send_and_wait('predict_belval', prediction[0])
        await producer.stop()
        
        

asyncio.run(process_and_resend())
        