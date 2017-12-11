from pyspark import SparkConf, SparkContext
from pyspark.mllib.classification import  NaiveBayesModel
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import operator
import pickle
import json
    
from pyspark.streaming import StreamingContext
conf = SparkConf().setMaster("local[2]").setAppName("Streamer")
sc = SparkContext(conf=conf)
#sc.setLogLevel("ERROR")
val = sc.parallelize("abd")


ssc = StreamingContext(sc, 10)
ssc.checkpoint("checkpoint")
kstream = KafkaUtils.createDirectStream(
ssc, topics = ['twitterstream'], kafkaParams = {"metadata.broker.list": 'localhost:9092'})
tweets = kstream.map(lambda x: x[1].encode("utf-8", "ignore"))

with open('IRModel', 'rb') as f:
    loadedModel = pickle.load(f)

bc_model = sc.broadcast(loadedModel)

from pyspark.mllib.feature import HashingTF
from pyspark.mllib.feature import IDF


def predictSentiment(tweetText):
    tweetText.foreachPartition(process_data)

def process_data(data):    

    for i in data:
        tweets_data = json.loads(i)
      
        abc = val.map(lambda x:tweets_data["text"])
        nbModel=bc_model.value
        hashingTF = HashingTF(100000)
        tf = hashingTF.transform(abc)
        tf.cache()
        idf = IDF(minDocFreq=2).fit(dictionary)
        tfidf = idf.transform(tf)
        tfidf.cache()
        prediction=nbModel.predict(tfidf)
        print(tweets_data['text'].encode('utf-8')+"\t"+prediction+"\n\n\n")
    

tweets.foreachRDD(predictSentiment)
ssc.start() 
ssc.awaitTerminationOrTimeout(1000)
#ssc.stop(stopGraceFully = True)
