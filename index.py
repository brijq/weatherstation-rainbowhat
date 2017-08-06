import rainbowhat as rh
import time
import colorsys
import struct

# Imports the Google Cloud client library
from google.cloud import pubsub

# Instantiates a client
pubsub_client = pubsub.Client()

# The name for the new topic
topic_name = 'weatherstation'

# Prepares the new topic
topic = pubsub_client.topic(topic_name)

# Creates the new topic
topic.create()

print('Topic {} created.'.format(topic_name))


#publishing message
pubsub_client = pubsub.Client()

topic = pubsub_client.topic(topic_name)

# Data must be a bytestring
#data = data.encode('utf-8')

@rh.touch.B.press()
def touch_b(channel):
   rh.display.clear()
   rh.display.print_str('Brian Rocks')
   rh.display.show()
   print('Button B pressed')

while True:
   t = rh.weather.temperature()
   p = rh.weather.pressure()
   rh.display.clear()
   data = rh.display.print_float(t)
   rh.display.show()
   print(t, p)
   time.sleep(1.0)


   data = "{:.9f}".format(rh.weather.temperature())
   message_id = topic.publish(data)

   print('Message {} published.'.format(message_id))
