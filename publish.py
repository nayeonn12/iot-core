from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import sys

myMQTTClient = AWSIoTMQTTClient("esp32")

myMQTTClient.configureEndpoint("asftum2h954pq-ats.iot.ap-southeast-2.amazonaws.com", 8883)
myMQTTClient.configureCredentials("/home/ec2-user/AmazonRootCA1.pem","/home/ec2-user/esp32-private.pem.key", "/home/ec2-user/esp32-certificate.pem.crt")

myMQTTClient.connect()
print("Client Connected")

msg = "Sample data from the device";
topic = "general/inbound"
myMQTTClient.publish(topic, msg, 0)  
print("Message Sent")

myMQTTClient.disconnect()
print("Client Disconnected")