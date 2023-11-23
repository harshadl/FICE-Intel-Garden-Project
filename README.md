# FICE-Intel-Garden-Project
Machine Learning powered smart irrigation system using IoT
DHT22 sensor (or similar) for temperature and humidity readings.
Soil moisture sensor.
Buzzer.
Relay module to control the DC water pump.
A DC water pump.
To run the sensor code to get the results  python3 simple.py

Step 1: Set Up Firebase
Go to the Firebase Console.
Create a new project.
Once your project is created, go to "Develop" and then "Database".
Create a Realtime Database.
In the rules for your database, make sure you have read and write permissions set appropriately for your use case.
Step 2: Install Firebase Python SDK
Install the Firebase Python SDK in your Raspberry Pi. You can do this using pip: pip install firebase-admin
Step 3: Integrate Firebase into Your Script
Modify your Python script to include Firebase integration. Below is an example of how you can do this python fireb.py
In this script fireb.py, you'll need to replace "path/to/your/firebase-credentials.json" with the path to your Firebase project's credentials JSON file and "https://your-database-url.firebaseio.com/" with your Firebase database URL.
This script fireb.py will send the temperature, humidity, soil moisture, and pump status to Firebase every time it checks these values. The data will be stored with a timestamp for easy tracking. Ensure to test the integration in a controlled environment before deploying it to avoid any data mishandling.


Integrating your Raspberry Pi project with ThingSpeak for monitoring parameters and adding manual control for the water pump can be done in several steps. ThingSpeak is an IoT analytics platform service that allows you to aggregate, visualize, and analyze live data streams in the cloud.

Step 1: Set Up ThingSpeak
Create a ThingSpeak Account:
Go to ThingSpeak and sign up for an account if you don't have one.

Create a Channel:

Once logged in, create a new channel.
Name your channel and create fields for temperature, humidity, soil moisture, and pump status.
Note Your API Keys:

Note the Write API Key to send data to ThingSpeak.
Note the Read API Key if you plan to read data from ThingSpeak.
Step 2: Install ThingSpeak Python Library
Install the ThingSpeak Python library on your Raspberry Pi: pip install thingspeak

Step 3: Modify Your Script with name as things.py
Modify your Python script to include ThingSpeak integration and add manual control for the water pump.


The manual_pump_control function in the script is a placeholder for your implementation of a manual control mechanism. This could be a button on a web interface that changes a value in a file or database, which the script checks regularly.
If the function returns True, the pump will turn on regardless of the sensor readings.
This script integrates your data collection with both Firebase and ThingSpeak, offering cloud storage and visualization capabilities. The manual control requires additional implementation based on your preferred method of interaction (e.g., a web-based interface). 


