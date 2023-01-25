"""
  Brady Monks
  1/25/2023

  This code sends a custom message to the server queue.
"""

# add imports at the beginning of the file
import pika

# create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters("LOCALHOST"))
# use the connection to create a communication channel
ch = conn.channel()
# use the channel to declare a queue
ch.queue_declare(queue="hello")
# Creat a variable for the message
message = 'Whoop Whoop!'
# use the channel to publish a message to the queue
ch.basic_publish(exchange="", routing_key="hello", body=message)
# print a message to the console for the user
print(" [x] Sent ",message)
# close the connection to the server
conn.close()
