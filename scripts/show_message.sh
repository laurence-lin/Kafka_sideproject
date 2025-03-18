docker exec -it $(docker ps --filter  "ancestor=wurstmeister/kafka" --format {{.ID}}) \
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic user_activity --from-beginning \
--timeout-ms 5000