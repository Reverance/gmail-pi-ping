import gmail, RPi.GPIO as GPIO, time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

g = gmail.login("amohabbat02@gmail.com","Hermes12")
unread_messages = g.inbox().mail(unread=True)
total_messages = 0

for message in unread_messages:
	total_messages += 1

if total_messages > 0:
	GPIO.output(18, True)
else:
	GPIO.output(18, False)
