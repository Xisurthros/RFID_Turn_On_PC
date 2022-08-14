import serial
from wakeonlan import send_magic_packet
print("Attempting to connect")
ser = serial.Serial("/dev/ttyACM0", 9600)
print("connected")
IDs = ["63 A0 58 93", "4C DC 64 49"] # Change to the IDs you want to allow

while True:
	try:
		code = ser.readline().decode('utf-8')[1:12]
		print(code)
		if code in IDs:
			send_magic_packet('YOUR_DEVICE_MAC_ADRESS') # Set to your devices MAC address
			print("TURNING ON!")
	except KeyboardInterrupt:
		break