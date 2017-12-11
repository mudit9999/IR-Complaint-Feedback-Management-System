from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient
import json

access_token = "your_access_token"
access_token_secret =  "your-access_token_secret"
consumer_key =  "your_consumer_key"
consumer_secret =  "your_consumer_secret"

class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send_messages("twitterstream", data.encode('utf-8','ignore'))
	data=json.loads(data)
        try:
	   print (data["text"])
	except:
	   print(data["text"])
        return True

kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track=['RailMinIndia','rail minister','suresh prabhu','northern railways'], stall_warnings=True, languages = ['en'])
