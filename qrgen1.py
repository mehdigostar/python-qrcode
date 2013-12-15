#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  qrgen1.py
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
#  
def __init__(
self, data=u'NULL', pixel_size=3, level='L', margin_size=4, data_type=u'text', filename=None
):

	from qrtools import QR
	myCode = QR(data=u"Simpledata", pixel_size=10)
	myCode.encode()
	print myCode.filename
	print myCode
