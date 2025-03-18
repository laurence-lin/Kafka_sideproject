# Kafka_sideproject
Kafka side project for practice


Kafka Application Kafka(Docker container) + Zookeeper(Docker container)
確保環境隔離

Producer & Consumer Application: Python application
簡易的用單一 producer 和 consumer, 犧牲 Container 的易於擴展性和 Deployment 自動化, 輕量化的簡易部署


Kafka Launch:
docker compose up -d



Producer & Consumer Launch:

# Install dependencies:
python3 -m pip install -r requirements.txt

Producer:
python -m producer.main

Consumer:
python -m consumer.main



