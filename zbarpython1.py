import zbar

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
        self.proc.active = True

    def get_data(self):
        self.proc.process_one()
        return(self.data)


if(__name__ == "__main__"):
   print QRCode().get_data() 
