import time
import logging
from kafka import KafkaProducer
from common.config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC, PRODUCER_INTERVAL, MAX_RECORDS
from common.models import UserActivity
from producer.data_generator import generate_user_activity

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_producer():
    return KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda x: x.encode('utf-8')
    )

def run_producer():
    producer = create_producer()
    counter = 0 # Number of generated messages from producer
    
    try:
        while MAX_RECORDS is None or counter < MAX_RECORDS:
            # Generate user action data
            activity = generate_user_activity()
            
            
            producer.send(  # Publish message to topic
                KAFKA_TOPIC,
                value=activity.to_json()
            )
            
            logger.info(f"Successfully produced to topic {KAFKA_TOPIC} with message: {activity} ")
            counter += 1

            time.sleep(PRODUCER_INTERVAL) # Generate new message every specific period of time
    
    except Exception as e:
        logger.info(f"Exception occurs for Producer: {e}")
    finally:
        logger.info("Close Producers.")
        producer.close()

if __name__ == "__main__":
    run_producer()