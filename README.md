# RFID_Turn_On_PC
> Turn on your PC with an RFID scanner

### Setup
> Set IDs in the 'IDs' to will allow specified IDs to turn your device on.
> Add the MAC address for the PC you are want to turn on.

### Wiring
| Pin  | Wiring     |
|------|------------|
| SDA  | Digital 10 |
| SCK  | Digital 13 |
| MOSI | Digital 11 |
| MISO | Digital 12 |
| IRQ  | Unconnected|
| GND  | GND        |
| RST  | Digital 9  |
| 3.3V | 3.3V       |

### Getting RFID ID's
> To get your custom RFID ID you will need to connect your controller to your PC via USB.
> In the Arduino IDE select the correct board and COM port.
> Go to File > Settings > FRC522 > DumpInfo.
> Upload this file. Once upload is finished you will be able to scan your RFID device and get the ID.
> When the information prints out to serial you will find "Card UID: YOUR_CODE_HERE".
> This is the ID that you will need to add to your IDs variable on line 6 of main.py.

### Gettting MAC address
> Open Command Prompt on the device you are wanting to WOL.
> Type 'ipconfig /all'.
> Here you will want to look for the device and find 'Physical Address'.
> This is what you will want to replace to main.pyon line 13 where it says 'YOUR_DEVICE_MAC_ADRESS'.