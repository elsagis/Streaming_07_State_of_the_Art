# Streaming_07_State_of_the_Art
Putting all what we have learned and showing the skills build up.The project from module 05 and 06, I have used my producer and consumer modified to use them for new document and file.  This way all the files needed to run this program are in one repo, have a consumer with 3 callbacks.

Author: Elsa Ghirmazion
Date: February 24, 2023 
Class: Streaming Data Assignment: Module 07

This program uses 1 producer, 3 task queues (RabbitMQ), 1 consumer, and 3 callbacks. It reads data from the USBuildinggsFootprints file(public)
 # This data is freely available and licenced by Microsoft under the Open Data Commons Open Database License(ODbL). This data is faked to be suitable for the programming.

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
When running a Buildings in usa, we monitor the number of buildings of the states increase to ensure in the specified range of number to claisify as small, medium and large. Provides necesary information.
these readings are an example of stored data but with regular monitoring of the increase of the number of buildings the states might move to the next classification.And are considered streaming data or data in motion.

Streaming Data
Our thermometer records three temperatures every thirty seconds (two readings every minute). The three temperatures are:

Significant Events
Condition to monitor/we want to know if:

If small number of buildings increases by 10,000 or more in 10 or more readings--> small_deque alert 'Small number of buildings! 
If numbner of buildings increase by 50,000 or more Alert"Meddium number of buildings"! and the state is classified as Medium.
If number of buildings change by 300,000 or more the state is getting classified as Large. --> Alert " Large number of buildings"!

Smart System
We will use Python to:

Simulate a streaming series of number ofbuildings readings from our csv live streaming from data server. 
Create a producer to send the number of buildings readings to RabbitMQ. Create three consumer processes, each one monitoring one of the number of buildings streams. Perform calculations to determine if a significant event has occurred.

Windowing
For more on windowing, read https://softwaremill.com/windowing-in-big-data-streams-spark-flink-kafka-akka/Links to an external site. 

Deque
For more abut deques, read https://docs.python.org/3/library/collections.html#collections.deque Links to an external site.(only the description of the deque class) We want to create a deque of limited size (to hold just the last n readings) - it'll act like a continuous queue The deque will hold only the number of readings we need for the time window of interest.

Code example: from collections import deque small_deque = deque(maxlen=5) # limited to 5 items (the 5 most recent readings)

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
Producer Vs Consumer - Module 7 Screenshots
![Consumer_RabbitMq_Anacond_buildings](https://user-images.githubusercontent.com/105325747/221481606-d2980325-2eef-4824-ab9a-00bb7b8ea6e0.png)
![Consumer RabbitMQBuilding](https://user-images.githubusercontent.com/105325747/221728621-d638f745-b5a3-4828-a0ef-4a7f22e004c9.png)
![ConsumerBuilding](https://user-images.githubusercontent.com/105325747/221729134-1bfb39e3-ca72-440b-9436-00822cc3645c.png)


# sources
<https://github.com/microsoft/USBuildingFootprints/blob/master/README.md>

