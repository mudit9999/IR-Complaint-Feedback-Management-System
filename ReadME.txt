Project Live Link: 

Pre-Requisites:

Setup Spark Cluster of atleast 3 Nodes 
Install Kakfa & Zookeeper(Refer tutorialspoint.com)
Install Apache-2, PHP-7 (Refer digitalocean.com)

Steps:
All the following commands have to be executed on terminal.

STEP-1: Start kafka-consumer:
$ bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic twitterstream --from-beginning

STEP-2: Run streaming.py file to check tweets are coming or not:
$ python streaming.py

STEP-3: Next step is to run model-train.py file to train our model, it would produce file "IRModel":
$ 