import paho.mqtt.client as mqtt
import uuid
import ssl
import cv2
from pydub import AudioSegment
from pydub.playback import play

# the # wildcard means we subscribe to all subtopics of IDD
topic = 'IDD/emergencyalerts/#'


def image_fullscreen(image_path):
	image = cv2.imread(image_path)
	resized_image = cv2.resize(image, (1920,1080))
	cv2.imshow("EMERGENCY ALERT", resized_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def play_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    play(audio)

#this is the callback that gets called once we connect to the broker. 
#we should add our subscribe functions here as well
def on_connect(client, userdata, flags, rc):
	print(f"connected with result code {rc}")
	client.subscribe(topic)
	# you can subsribe to as many topics as you'd like
	# client.subscribe('some/other/topic')


# this is the callback that gets called each time a message is recived
def on_message(cleint, userdata, msg):
	if msg.topic == 'IDD/emergencyalerts/fire':
		image_fullscreen("/home/pi/Documents/idd/Interactive-Lab-Hub/Lab 6/FireAlarm.png")
		play_audio("/home/pi/Documents/idd/Interactive-Lab-Hub/Lab 6/fire.mp3")
		play_audio("/home/pi/Documents/idd/Interactive-Lab-Hub/Lab 6/firealarm.mp3")
	elif msg.topic == 'IDD/emergencyalerts/lockdown':
		image_fullscreen("/home/pi/Documents/idd/Interactive-Lab-Hub/Lab 6/lockdown.png")
		play_audio("/home/pi/Documents/idd/Interactive-Lab-Hub/Lab 6/lockdown.mp3")

	print(f"topic: {msg.topic} msg: {msg.payload.decode('UTF-8')}")
	# you can filter by topics
	# if msg.topic == 'IDD/some/other/topic': do thing


# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set(cert_reqs=ssl.CERT_NONE)
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

# attach out callbacks to the client
client.on_connect = on_connect
client.on_message = on_message

#connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

# this is blocking. to see other ways of dealing with the loop
#  https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php#network-loop
client.loop_forever()
