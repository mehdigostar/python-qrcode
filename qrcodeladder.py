import zbar
import RPi.GPIO as GPIO
import time

# init gpio
GPIO.setmode(GPIO.BOARD)

# supress warnings
GPIO.setwarnings(False)

# cleanup
GPIO.cleanup()

#init pins 11 and 12 for output

GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

#turn off leds

GPIO.output(11, False)
GPIO.output(12, False)

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
#turn on red leds	
	GPIO.output(11, True)
	GPIO.output(12, True)    

#if(__name__ == "__main__"):
 #  print QRCode().get_data() 



