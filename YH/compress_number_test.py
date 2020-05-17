#!/usr/bin/env python3

# Attempts to binary compress a regular payload with all its accompanying prefixes to be sent to a Rockblock 9603

import binascii
import struct
import time

# Pack Prefix
pre_1 = (b'RB',)
s1 = struct.Struct('2s')
packed_1 = s1.pack(*pre_1)
pre_2 = (19469,)
s2 = struct.Struct('> I')
packed_2 = s2.pack(*pre_2)
packed_2 = packed_2[1:]

# Original msg
msg = "19 259 1 21 2 2304 102 6798 4 0 10"

# Spilt the msg into a list
li = msg.split(" ")
li = list(map(int, li))
li_size = len(li)

# Preparing the regular payload (which are all short ints) 
i = 0
struct_cmd = '>'
while i < li_size:
	struct_cmd = struct_cmd + ' H'
	i = i + 1

# Pack the regular payload
s = struct.Struct(struct_cmd)
packed_3 = s.pack(*li)
packed_data = packed_1 + packed_2 + packed_3
print(packed_data)
print(binascii.hexlify(packed_data))
print("Packed msg length: " + str(s1.size + s2.size-1 + s.size))

# Now unpack it

# Unpack if it is binary
if packed_data[0] == ord('R') and packed_data[1] == ord('B'):
	packed_data = packed_data[5:]
	unpacked_data = struct.unpack(struct_cmd, packed_data)
	print(unpacked_data)