import logging
from kafka import KafkaConsumer
from common.config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC, KAFKA_CONSUMER_GROUP
from common.models import UserActivity
from consumer.data_processor import process_user_activity
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_consumer():
    return KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id=KAFKA_CONSUMER_GROUP,
        auto_offset_reset='earliest', # Consumer read from earliest avaiable offset, since this is develop first launch
        value_deserializer=lambda x: x.decode('utf-8')
    )

def run_consumer():
    consumer = create_consumer()
    logger.info("Consumer created. Start listening to broker topic...")
    
    try:
        while True:
            message_batch = consumer.poll(timeout_ms=2000) # Listen to batch message every time interval

            if not message_batch:
                logger.info(f"No new message for topic {KAFKA_TOPIC}, waiting...")
                continue

            
            for tp, messages in message_batch.items():
                for message in messages:
                    activity = UserActivity.from_json(message.value) # Parse message
                    process_result = process_user_activity(activity) # Process message
                    
                    print(f"Successfully get Topic message! Consumed: {activity}, Result: {process_result}")
                    logger.info(f"Consumed: {activity}, Result: {process_result}")
    
    except Exception as e:
        logger.info(f"Exception occurs for Consumer: {e}")
    finally:
        logger.info("Close Consumers.")
        consumer.close()

if __name__ == "__main__":
    logger.info("Start Consumer!")
    run_consumer()