# Kafka_sideproject
Kafka side project for practice


Kafka Application Kafka(Docker container) + Zookeeper(Docker container)
確保環境隔離

Producer & Consumer Application: Python application
簡易的用單一 producer 和 consumer, 犧牲 Container 的易於擴展性和 Deployment 自動化, 輕量化的簡易部署


# Launch Application: Step by Step
#### 1. Kafka Launch:
docker compose up -d


#### 1.5 Install dependencies:
python3 -m pip install -r requirements.txt

#### 2. Producer & Consumer Launch:

Consumer: 
python -m consumer.main

Producer:
python -m producer.main



# View Consumer retrieved topic message report:
script/consumer_report.sh

This would display statistic report for topic 'user_activity' recieved by Consumer such as:

Statistic reports for Kafka topic 'user_activity' as below:

Total unique users: 18

Event type counts:

      5 search

      5 purchase

      4 login

      3 page_view

      2 button_click

Page counts:

      4 profile

      4 checkout

      4 cart

      3 home

      2 products

      2 help



