import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import adafruit_dht
import yaml


with open("/data/config.yml", "r") as stream:
    try:
        config = yaml.safe_load(stream)['config']
    except yaml.YAMLError as exc:
        print(exc)

mqttBrokerURL = config['brokerURL']  #'batman.local'
mqttBrokerPort = config['brokerPort']
topic = config['mqttTopic'] #"homeassistant/sensor/pool/weather"
mqttUser = config['mqttUser']
mqttPassword = config['mqttPassword']
clientName = config['clientName']

print("BrokerURL: " + mqttBrokerURL + ", Port: " + mqttBrokerPort)
print("MQTT Topic: " + topic)

dhtDevice = adafruit_dht.DHT11(board.D4, use_pulseio=False)

temperature_c_str = ""
temperature_f_str = ""
humidity = 0.0

def connect_mqtt():
	def on_connect(client, userdata, flags, rc):
		if rc == 0:
			print("Connected to MQTT Broker!")
		else:
			print("Failed to connect to MQTT Broker, return code %d\n", rc)

	client = mqtt.Client(clientName)
	client.username_pw_set(mqttUser, mqttPassword)
	client.on_connect = on_connect
	client.connect(mqttBrokerURL, mqttBrokerPort)
	return client

def publish(client):
	msg_count = 0
	while True:
		weather_status = fetch_weather_data()
		if weather_status[0] == 0:
			temperature_f_str = weather_status[1]
			temperature_c_str = weather_status[2]
			humidity = weather_status[3]
			payload = '{ "temperature_f": ' + temperature_f_str + ', "temperature_c": ' + temperature_c_str + ' ,"humidity": ' + str(humidity) + ' }'
			result = client.publish(topic, payload)
			status = result[0]
			if status == 0:
				print(f"Send `{payload}` to topic `{topic}`")
			else:
				print(f"Faled to send message to topic `{topic}`")
			time.sleep(60)
		else:
			print("failed to fetch weather status")
			time.sleep(5)

def run():
	client = connect_mqtt()
	client.loop_start()
	publish(client)

def fetch_weather_data(): 
	status = [1, "", "", 0.0]
	try:
		temperature_c = dhtDevice.temperature
		temperature_f = temperature_c * (9 / 5) + 32
		temperature_c_str = "{:.1f}".format(temperature_c)
		temperature_f_str = "{:.1f}".format(temperature_f)
		humidity = dhtDevice.humidity
		print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(temperature_f, temperature_c, humidity))
		status = [0, temperature_f_str, temperature_c_str, humidity]

	except RuntimeError as error: 
		print(error.args[0])
		time.sleep(5)
		return status

	except Exception as error:
		dhtDevice.exit()
		raise error

	return status

run()