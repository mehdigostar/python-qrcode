#version 3.0

import zbar
import sys

class QRCode():

    data = None
    proc = None
    scanner = None

    def qr_handler(self,proc,image,closure):
        # extract results
        for symbol in image:
            if not symbol.count:
                self.data = symbol.data

    def __init__(self):
        self.proc = zbar.Processor()
        self.scanner = zbar.ImageScanner()
        self.scanner.parse_config('enable')

        self.proc.init("/dev/video0")
        self.proc.set_data_handler(self.qr_handler)
        self.proc.visible = False
#display cam window if True,  hide if False
        self.proc.active = True

    def get_data(self):
        self.proc.process_one()
        return(self.data)

#if(QRCode().get_data() == "test"):
#	print "DATA IS test"

data = QRCode().get_data()
if (data == "test"):
	print "data is test"

elif (data == "EXIT"):
	print "data is EXIT"
	sys.exit()

# blue LEDS

elif (data == "LEDBlueON"):
	print ("Data is LEDBlueON")

elif (data == "LEDBlueOFF"):
	print ("Data is LEDBlueOFF")

# Green LEDS

elif (data == "LEDGreenON"):
	print ("Data is LEDGreenON")

elif (data == "LEDGreenOFF"):
	print ("Data is LEDGreenOFF")

# Red LEDS

elif (data == "LEDRedON"):
	print ("Data is LEDBRedN")

elif (data == "LEDRedOFF"):
	print ("Data is LEDRedOFF")

# Yellow LEDs

elif (data == "LEDYellowON"):
	print ("Data is LEDYellowON")

elif (data == "LEDYellowOFF"):
	print ("Data is LEDYellowOFF")

# All ON

elif (data == "LEDSON"):
	print ("Data is LEDSON")

# ALL OFF

elif (data == "LEDSOFF"):
	print ("Data is LEDOFF")

#if(__name__ == "__main__"):
 #  print QRCode().get_data() 



