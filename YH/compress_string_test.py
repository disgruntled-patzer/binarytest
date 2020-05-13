#!/usr/bin/env python3

# So I tried compressing a string using python struct to see if it would really compress...
# Turns out it doesn't. Original and final size is still 36 bytes

import binascii
import struct

msg = "19 259 1 21 2.23041 102.67982 4 0 10"
msg_len = len(msg)
print ("original msg: " + msg)
print ("original msg length: " + str(msg_len))
values = (msg.encode(),)
s = struct.Struct(str(msg_len) + 's')
packed_data = s.pack(*values)
print ("Packed msg length: " + str(s.size))