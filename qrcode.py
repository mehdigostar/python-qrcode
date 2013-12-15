#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  qrcode.py
#  
#  Copyright 2013 psutton <zleap@zleap.net>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# references
# http://sourceforge.net/apps/mediawiki/zbar/index.php?title=HOWTO:_Scan_images_using_the_API
# http://ralgozino.wordpress.com/2011/06/13/how-to-create-and-decode-a-qr-code-in-python-using-qrtools/

import qrtools
from sys import argv
import zbar
import Image
from qrtools import QR
myCode = QR()
print myCode.decode_webcam()



if len(argv) < 2: exit(1)

# create a reader
scanner = zbar.ImageScanner()

# configure the reader
scanner.parse_config('enable')

# obtain image data
pil = Image.open(argv[1]).convert('L')
width, height = pil.size
raw = pil.tostring()

# wrap image data
image = zbar.Image(width, height, 'Y800', raw)

# scan the image for barcodes
scanner.scan(image)

# extract results
for symbol in image:
    # do something useful with results
    print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data

# clean up
del(image)

print myCode.decode_webcam()
