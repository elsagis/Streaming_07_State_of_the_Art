"""
    This program listens "Building in USA" csv data and alerts if the number is changes from samll to medium or large.  
    Author:Elsa Ghirmazion
    Date: February 25, 2023
"""
################################################################################################################################
import pika
import sys
import pickle
from collections import deque
###################################################################################################################################
# Define variables
host = "localhost"
csv_file = "Buildings_in_usa.csv"
small_deque = "01-small"
medium_deque = "02-medium"
large_deque = "03-large"
show_offer = True  # (RabbitMQ Server option - T=on, F=off)
####################################################################################################################################
# Limit small readings to last 2.5 minutes/5 readings
small_deque = "01-small"
small_deque = deque(maxlen = 14)
# limit medium readings to last 10 minutes/20 readings
medium_deque = "02-medium"
medium_deque = deque(maxlen = 28)
# limit large readings to last 2 minutes/8 readings
large_deque = "03-large"
large_deque = deque(maxlen=8)


######################################################################################################################################
# define a callback function to be called when a message is received from the Building_in_usa
def small_callback(ch, method, properties, body):
    """ Define behavior on getting a message."""
    # decode the binary message body to a string
    print(f" [x] Received {pickle.loads(body)} on 01-small")
    # acknowledge the message was received and processed 
    # (now it can be deleted from the queue)
    ch.auto_ack(delivery_tag=method.delivery_tag)
    # convert message from binary to tuple
    message = pickle.loads(body)
    # add message to deck only if a number of building has been recorded
    if isinstance(message[1], int):
        small_deque.appendleft(message)
##########################################################################################################################################
    # only perform checks and send readings when number of buildings are recorded
        # find first item in deque
        cur_small_deque_number_of_buildings = small_deque[0]
        # get the first reading of the small
        small_number_of_buildings_first = cur_small_deque_number_of_buildings[1]
   
        # find last item in deque
        last_small_deque_number_of_buildings = small_deque[-1]
        # get the last number of buildings in the small
        small_number_of_buildings_last = last_small_deque_number_of_buildings[1]
#############################################################################################################################################
        # compare first and last message if there has been at least 5 messages sent
        if len(small_deque) == 5:
            # find mumber of buildings difference
            if small_number_of_buildings_last - small_number_of_buildings_current >= 10000:
                # send alert if small has increased 10000 or more numbers
                print(f"Small Alert! Number of building  has increased 10,000  or more numbers from {small_number_of_buildins_last} to {small_number_of_buildings_current}")
            else: # else print the current number of building
                print(f"Current small number of buildings is {small_number_of_buildings_current}")
        else: # print current temp if there are less than 5 readings
            print(f"Current small number of buildings is {small_number_of_buildings_current}")
###############################################################################################################################################
# define a callback function to be called when a message is received from 02_medium
def medium_callback(ch, method, properties, body):
    """ Define behavior on getting a message."""
    # decode the binary message body to a string
    print(f" [x] Received {pickle.loads(body)} on 02-medium")
    # acknowledge the message was received and processed 
    # (now it can be deleted from the queue)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    # convert message from binary to tuple
    message = pickle.loads(body)
    # add message to deck only if a number of buildings has been recorded
    if isinstance(message[1], float):
        medium_deque.appendleft(message)
        # only perform checks and send readings when tempuratures are recorded
        # find first item in deque
        cur_medium_deque_number_of_buildings = medium_deque[0]
        # get the current number of buildings of medium
        medium_number_of_buildings_current = cur_medium_deque_number_of_buildings[1]
   ##############################################################################################################################################
        # find last item in deque
        last_medium_deque_number_of_buildings = medium_deque[-1]
        # get the last number of buildings of medium
        medium_number_of_buildings_last = last_medium_deque_number_of_buildings[1]

        # check if 28 messages have been sent to compare medium number of buildings
        if len(medium_deque) == 28:
            if medium_number_of_buildings_last - medium_number_of_buildings_current < 50000:
                # send alert if medium number of buildings has increased
                print(f"medium number of buildings has increased! Number of buildings has increased more than 50000 {medium_number_of_buildings_last} to {medium_number_of_buildings_current}")
            else: # else print the current number of buildings
                print(f"Current medium number of buildings is {medium_number_of_buildings_current}")
        else: # else print the current number of buildings
            print(f"Current medium  number of buildings is {medium_number_of_buildings_current}")
#################################################################################################################################################
# define a callback function to be called when a message is received from large
def large_callback(ch, method, properties, body):
    """ Define behavior on getting a message."""
    # decode the binary message body to a string
    print(f" [x] Received {pickle.loads(body)} on 02-large")
    # acknowledge the message was received and processed 
    # (now it can be deleted from the queue)
    ch.auto_ack(delivery_tag=method.delivery_tag)
    # convert message from binary to tuple
    message = pickle.loads(body)
    # add message to deck only if a temp has been recorded
    if isinstance(message[1], float):
        large_deque.appendleft(message)
        # only perform checks and send readings when tempuratures are recorded
        # find first item in deque
        cur_large_deque_number_of_buildings = large_deque[0]
        # get the current temperature of food b
        large_number_of_buildings_current = cur_large_deque_number_of_buildings[1]
   
        # find last item in deque
        last_large_deque_number_of_buildings = large_deque[-1]
        # get the last temperature of large
        large_number_of_buildings_last = last_large_deque_number_of_buildings[1]

        # check if 9 messages have been sent to compare large number of buildings
        # if len(large_deque) == 9:
        if large_number_of_buildings_last - large_number_of_buildings_current < 300000:
                # send alert if large number of buildings has increased
                print(f"Large number of buildings! Large number of buildings has increased  in the last 10 readings from {large_number_of_buildings_last} to {large_number_of_buildings_current}")
        else: # else print the current temp
                print(f"Current large number of buildings is {large_number_of_buildings_current}")
    else: # else print the current number of buildings
            print(f"Current large number of buildings is {large_number_of_buildings_current}")


###################################################################################################################################################

# define a main function to run the program for 3 queues
def main(hn: str):
    """ Continuously listen for task messages on a named queue."""

    # when a statement can go wrong, use a try-except block
    try:
        # try this code, if it works, keep going
        # create a blocking connection to the RabbitMQ server
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=hn))

    # except, if there's an error, do this
    except Exception as e:
        print()
        print("ERROR: connection to RabbitMQ server failed.")
        print(f"Verify the server is running on host={hn}.")
        print(f"The error says: {e}")
        print()
        sys.exit(1)

    try:
        # use the connection to create a communication channel
        channel = connection.channel()

        # use the channel to declare a durable queues
        channel.queue_declare(queue="01-small", durable=True)
        channel.queue_declare(queue="02-medium", durable=True)
        channel.queue_declare(queue="03-large", durable=True)

        # set the prefetch count    
        channel.basic_qos(prefetch_count=1) 

        # configure the channel to listen on a specific queue,  
        channel.basic_consume( queue="01-small", auto_ack = False, on_message_callback=small_callback)
        channel.basic_consume( queue="02-medium",auto_ack = False, on_message_callback=medium_callback)
        channel.basic_consume( queue="03-large", auto_ack = False, on_message_callback=large_callback)

        # print a message to the console for the user
        print(" [*] Ready for work. To exit press CTRL+C")

         # start consuming messages via the communication channel
        channel.start_consuming()

    # except, in the event of an error OR user stops the process, do this
    except Exception as e:
        print()
        print("ERROR: something went wrong.")
        print(f"The error says: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print()
        print(" User interrupted continuous listening process.")
        sys.exit(0)
    finally:
        print("\nClosing connection. Goodbye.\n")
        channel.queue_delete(small_deque)
        channel.queue_delete(medium_deque)
        channel.queue_delete(large_deque)
        connection.close()


# Standard Python idiom to indicate main program entry point
# This allows us to import this module and use its functions
# without executing the code below.
# If this is the program being run, then execute the code below
if __name__ == "__main__":
    # call the main function with the information needed
    main("localhost")