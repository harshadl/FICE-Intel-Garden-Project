import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Firebase configuration
cred = credentials.Certificate("path/to/your/firebase-credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-database-url.firebaseio.com/'
})

# Reference to your database
data_ref = db.reference('sensor_data')

# Rest of your sensor setup...

def send_data_to_firebase(temperature, humidity, soil_moisture, pump_status):
    data = {
        'temperature': temperature,
        'humidity': humidity,
        'soil_moisture': soil_moisture,
        'pump_status': pump_status,
        'timestamp': time.time()
    }
    data_ref.push(data)

try:
    while True:
        soil_moisture = read_moisture()
        temperature, humidity = read_temp_humidity()
        pump_status = None

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
        time.sleep(10) # Check every 10 seconds

except KeyboardInterrupt:
    print("Program stopped")
finally:
    GPIO.cleanup()
