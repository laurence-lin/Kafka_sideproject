#!/bin/bash

echo "Statistic reports for Kafka topic 'user_activity' as below:  "

# Input text (replace with your file if needed)
input_text='{"user_id": "user_53", "event_type": "login", "page": "home", "timestamp": "2025-03-18T14:03:34.711878"}
{"user_id": "user_3", "event_type": "purchase", "page": "profile", "timestamp": "2025-03-18T14:03:37.722004"}
{"user_id": "user_29", "event_type": "page_view", "page": "home", "timestamp": "2025-03-18T14:03:39.726337"}
{"user_id": "user_54", "event_type": "purchase", "page": "products", "timestamp": "2025-03-18T14:03:40.730088"}'

# Extract user_ids and count unique users
unique_users=$(echo "$input_text" | grep -oP '"user_id": "\K[^"]+' | sort -u | wc -l)
echo "Total unique users: $unique_users"

# Extract event_types and count occurrences
echo "Event type counts:"
echo "$input_text" | grep -oP '"event_type": "\K[^"]+' | sort | uniq -c | sort -nr

# Extract pages and count occurrences
echo "Page counts:"
echo "$input_text" | grep -oP '"page": "\K[^"]+' | sort | uniq -c | sort -nr