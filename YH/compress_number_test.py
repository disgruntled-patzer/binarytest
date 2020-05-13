#!/usr/bin/env python3

# So I tried compressing a string using python struct to see if it would really compress...
# Turns out it doesn't. Original and final size is still 36 bytes

import binascii
import struct

# Original msg: Regular payload plus a prefix
msg = "R 19 259 1 21 2.23041 102.67982 4 0 10"
print ("original msg: " + msg)
print ("original msg length: " + str(len(msg)))

# Now spilt the msg into a list (can we tell the despatcher node to send us a list instead of a string...?)
# E.g. create a new topic specially for sbd node, and pass msg as a special ros msg
li = msg.split(" ")
list_size = len(li)

# Hardcoding because no apparent pattern in regular payload
# Any way to move away from hardcoding? Looks like it's not a very good idea to pass everything to the link nodes as strings
li[0] = li[0].encode()
li[1] = int(li[1])
li[2] = int(li[2])
li[3] = int(li[3])
li[4] = int(li[4])
li[5] = float(li[5])
li[6] = float(li[6])
li[7] = int(li[7])
li[8] = int(li[8])
li[9] = int(li[9])

s = struct.Struct('s h h h h f f h h h')
packed_data = s.pack(*li)
print("packed msg: " + str(packed_data))
print("packed msg length " + str(s.size))

# 38 byte regular payload in text format becomes 26 bytes in compressed format. Yay!