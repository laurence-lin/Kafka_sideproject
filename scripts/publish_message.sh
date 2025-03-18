echo "Test message content" | \
docker exec -i $(docker ps --filter  "ancestor=wurstmeister/kafka" --format {{.ID}}) \
/opt/kafka/bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic practice_topic