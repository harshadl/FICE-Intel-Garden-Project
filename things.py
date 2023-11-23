import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import firebase_admin
from firebase_admin import credentials, db
import thingspeak

# Firebase configuration
# ...

# ThingSpeak configuration
channel_id = "YOUR_CHANNEL_ID" 
write_key  = "YOUR_WRITE_API_KEY" 
read_key = "YOUR_READ_API_KEY" 

channel = thingspeak.Channel(id=channel_id, api_key=write_key)

# Rest of your sensor setup...
# ...

def update_thingspeak(temperature, humidity, soil_moisture, pump_status):
    try:
        response = channel.update({
            1: temperature,
            2: humidity,
            3: soil_moisture,
            4: pump_status
        })
        print("Updated to ThingSpeak")
    except:
        print("Connection failed")

def manual_pump_control():
    # Implement a mechanism to receive input from a soft button
    # This could be via a simple web interface or another method
    # For example, checking a file's content, a database flag, etc.
    # Return True to turn on the pump, False to turn it off
    return False

try:
    while True:
        soil_moisture = read_moisture()
        temperature, humidity = read_temp_humidity()
        pump_status = None

        # Check for manual control
        if manual_pump_control():
            control_pump(True)
            pump_status = 'ON'
        else:
            if soil_moisture < 30 or (soil_moisture < 40 and temperature > 29 and humidity > 90):
                control_pump(True)
                pump_status = 'ON'
                time.sleep(1800) # 30 minutes
                control_pump(False)
                pump_status = 'OFF'
            elif soil_moisture > 50 and temperature < 26 and humidity == 100:
                control_pump(False)
                pump_status = 'OFF'

        send_data_to_firebase(temperature, humidity, soil_moisture, pump_status)
        update_thingspeak(temperature, humidity, soil_moisture, pump_status)
        time.sleep(10) # Check every 10 seconds

except KeyboardInterrupt:
    print("Program stopped")
finally:
    GPIO.cleanup()
