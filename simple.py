import RPi.GPIO as GPIO
import Adafruit_DHT
import time

# Set up GPIO pins
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
MOISTURE_SENSOR_PIN = 5
BUZZER_PIN = 7
RELAY_PIN = 9

GPIO.setmode(GPIO.BCM)
GPIO.setup(MOISTURE_SENSOR_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(RELAY_PIN, GPIO.OUT)

def read_moisture():
    return GPIO.input(MOISTURE_SENSOR_PIN)

def read_temp_humidity():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return temperature, humidity

def control_pump(turn_on):
    GPIO.output(RELAY_PIN, turn_on)
    if turn_on:
        print("Water pump ON")
    else:
        print("Water pump OFF")

try:
    while True:
        soil_moisture = read_moisture()
        temperature, humidity = read_temp_humidity()

        if soil_moisture < 30 or (soil_moisture < 40 and temperature > 29 and humidity > 90):
            control_pump(True)
            time.sleep(1800) # 30 minutes
            control_pump(False)
        elif soil_moisture > 50 and temperature < 26 and humidity == 100:
            control_pump(False)

        time.sleep(10) # Check every 10 seconds

except KeyboardInterrupt:
    print("Program stopped")
finally:
    GPIO.cleanup()
