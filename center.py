from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

print("moving servo to 90 degree")

while True:
    for i in range(16):
        try:
            kit.servo[i].angle = 90
        except:
            pass

    time.sleep(1)
print ("done")