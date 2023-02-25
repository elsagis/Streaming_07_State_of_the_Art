# Streaming_07_State_of_the_Art
Putting all what we have learned and showing the skills build up.The project from module 05 and 06, I have used my producer and consumer modified to use them for new document and file.  This way all the files needed to run this program are in one repo, have a consumer with 3 callbacks.

Author: Elsa Ghirmazion
Date: February 24, 2023 
Class: Streaming Data Assignment: Module 07

This program uses 1 producer, 3 task queues (RabbitMQ), 1 consumer, and 3 callbacks. It reads data from the       xxxxxx file for .

Instructions on how to run the program
Before you begin, adjust your settings in Visual Studio and set-up your conda environment
View / Command Palette - then Python: Select Interpreter
Select your conda environment.
Adjust your code as needed
Update your constants in the .py file
Update your constants in the consumer.py file, including alert limits and deque lengths
Execute the Producer
Open 2 Anaconda Prompt Terminals
In both terminals, change directory to your github folder for this module (where these files are located)
In both terminals, run code "conda activate base"
Run producer.py file "python _producer.py" (say y to monitor RabbitMQ queues)
Run _consumer.py file "python _consumer.py"
Assignment Details
Using a ()
When running a barbeque smoker, we monitor the temperatures of the smoker and the food to ensure everything turns out tasty. Over long cooks, the following events can happen:

The smoker temperature can suddenly decline.
The food temperature doesn't change. At some point, the food will hit a temperature where moisture evaporates. It will stay close to this temperature for an extended period of time while the moisture evaporates (much like humans sweat to regulate temperature). We say the temperature has stalled.

Sensors
We have temperature sensors track temperatures and record them to generate a history of both (a) the smoker and (b) the food over time. These readings are an example of time-series data, and are considered streaming data or data in motion.

Streaming Data
Our thermometer records three temperatures every thirty seconds (two readings every minute). The three temperatures are:

the temperature of the smoker itself.
the temperature of the first of two foods, Food A.
the temperature for the second of two foods, Food B.
Significant Events
Condition to monitor/we want to know if:

If smoker temp decreases by 15 F or more in 2.5 min (or 5 readings) --> smoker alert! If food temp change in temp is 1 F or less in 10 min (or 20 readings) --> food stall alert!

Smart System
We will use Python to:

Simulate a streaming series of temperature readings from our smart smoker and two foods. Create a producer to send these temperature readings to RabbitMQ. Create three consumer processes, each one monitoring one of the temperature streams. Perform calculations to determine if a significant event has occurred.

Windowing
For more on windowing, read https://softwaremill.com/windowing-in-big-data-streams-spark-flink-kafka-akka/Links to an external site. Smoker time window = 2.5 mins Food time window = 10 mins How many temperature readings are in the smoker time window? At one reading every 1/2 minute, the smoker deque max length is 5 (2.5 min * 1 reading/0.5 min) How many temperature readings are in the food time window? At one reading every 1/2 minute, the food deque max length is 20 (10 min * 1 reading/0.5 min)

Deque
For more abut deques, read https://docs.python.org/3/library/collections.html#collections.deque Links to an external site.(only the description of the deque class) We want to create a deque of limited size (to hold just the last n readings) - it'll act like a continuous queue The deque will hold only the number of readings we need for the time window of interest.

Code example: from collections import deque smoker_deque = deque(maxlen=5) # limited to 5 items (the 5 most recent readings)

References
Producer
Convert string to float (with blank cells in csv) - https://codedamn.com/news/programming/fix-valueerror
auto-ack: https://www.rabbitmq.com/confirms.html
SyntaxError: positional argument follows keyword argument - https://www.geeksforgeeks.org/how-to-fix-syntaxerror-positional-argument-follows-keyword-argument-in-python/
how to tell python to do nothing: https://realpython.com/python-pass/
Consumer
deques: https://docs.python.org/3/library/collections.html#collections.deque
split string: https://www.w3schools.com/python/ref_string_split.asp
remove last characters from string: https://careerkarma.com/blog/python-remove-character-from-string/#:~:text=You%20can%20remove%20a%20character,the%20string%20without%20a%20replacement.
round floats to 1 decimal place: https://stackoverflow.com/questions/3400965/getting-only-1-decimal-place
how to split a new line: https://www.freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline/
Producer - Module 7 Screenshots
