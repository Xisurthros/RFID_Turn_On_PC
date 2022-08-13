import serial
from wakeonlan import send_magic_packet
print("Attempting to connect")
ser = serial.Serial("/dev/ttyACM0", 9600)
print("connected")
IDs = ["63 A0 58 93", "4C DC 64 49"]

while True:
	try:
		code = ser.readline().decode('utf-8')[1:12]
		print(code)
		if code in IDs:
			send_magic_packet('4C.CC.6A.2B.BA.A8')
			print("TURNING ON!")
	except KeyboardInterrupt:
		break