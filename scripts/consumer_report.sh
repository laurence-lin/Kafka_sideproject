#!/bin/bash


# Input text (replace with your file if needed)
input_text=$(docker exec -i $(docker ps --filter  "ancestor=wurstmeister/kafka" --format {{.ID}}) kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic user_activity --from-beginning --timeout-ms 5000 2>&1 | grep user_id)

echo "Statistic reports for Kafka topic 'user_activity' as below:  "

# Extract user_ids and count unique users
unique_users=$(echo "$input_text" | grep -oP '"user_id": "\K[^"]+' | sort -u | wc -l)
echo "Total unique users: $unique_users"

# Extract event_types and count occurrences
echo "Event type counts:"
echo "$input_text" | grep -oP '"event_type": "\K[^"]+' | sort | uniq -c | sort -nr

# Extract pages and count occurrences
echo "Page counts:"
echo "$input_text" | grep -oP '"page": "\K[^"]+' | sort | uniq -c | sort -nr