# Kafka Config
KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092' # Kafka broker node server
KAFKA_TOPIC = 'user_activity'   # Produced topics
KAFKA_CONSUMER_GROUP = 'activity_consumers'    # Consumer groups for topic

# Producer
PRODUCER_INTERVAL = 1.0  # Data generation interval
MAX_RECORDS = 1000  # Max number of record published limit for development. In Production, set to None

# Consumer for batch processing when high throughput
BATCH_SIZE = 100  