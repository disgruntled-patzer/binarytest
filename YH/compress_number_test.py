#!/usr/bin/env python3

# So I tried compressing a string using python struct to see if it would really compress...
# Turns out it doesn't. Original and final size is still 36 bytes

import binascii
import struct

# Original msg: Regular payload plus a 'R' prefix (if we plan to prefix our regular payloads)
msg = "R 19 259 1 21 2 2304 102 6798 4 0 10"
print ("original msg: " + msg)
print ("original msg length: " + str(len(msg)))

# Now spilt the msg into a list (can we tell the despatcher node to send us a list instead of a string...?)
# E.g. create a new topic specially for sbd node, and pass msg as a special ros msg
li = msg.split(" ")
li_size = len(li)

# Preparing the prefix (which is a character)
li[0] = li[0].encode()
struct_cmd = 's'

# Preparing the rest of the payload (which are all short ints) 
i = 1 # Start from index 1
while i < li_size:
	struct_cmd = struct_cmd + ' h'
	li[i] = int(li[i])
	i = i + 1

s = struct.Struct(struct_cmd)
packed_data = s.pack(*li)
print(packed_data)
print("packed msg length " + str(s.size))

# 38 byte regular payload in text format becomes 24 bytes in compressed format. Yay!