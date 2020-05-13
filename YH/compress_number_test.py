#!/usr/bin/env python3

# Attempts to binary compress a regular payload with all its accompanying prefixes to be sent to a Rockblock 9603

import binascii
import struct
import time

# Original msg
msg = "19 259 1 21 2 2304 102 6798 4 0 10"
serial = 19466

# Add prefixes
msg = "RB " + str(serial) + " R " + str(int(time.time())) + " " + msg
print ("Original msg (with prefixes): " + msg)
print ("Original msg length: " + str(len(msg)))

# Spilt the msg into a list (can we tell the despatcher node to send us a list instead of a string...?)
li = msg.split(" ")
li_size = len(li)

# Prepare the prefixes.
# 1st entry: RB (2 characters)
# 2nd entry: Rockblock serial number (unsigned short int, assuming serial doesn't exceed 65535)
# 3rd entry: R (to identify payload as regular payload. 1 character)
# 4th entry: 32 bit (4 byte) UNIX timestamp
# Preparing the 1st entry (RB, which are 2 characters)
li[0] = li[0].encode()
li[1] = int(li[1])
li[2] = li[2].encode()
li[3] = int(li[3])
struct_cmd = '2s H s I'

# Preparing the rest of the payload (which are all short ints) 
i = 4
while i < li_size:
	struct_cmd = struct_cmd + ' H'
	li[i] = int(li[i])
	i = i + 1

# Pack the data
s = struct.Struct(struct_cmd)
packed_data = s.pack(*li)
print(packed_data)
print("Packed msg length: " + str(s.size))

# 56 byte regular payload in text format becomes 34 bytes in compressed format. Yay!
# Note that total length of the struct is not equal to sum of sizeof each individual entry
# See https://www.geeksforgeeks.org/is-sizeof-for-a-struct-equal-to-the-sum-of-sizeof-of-each-member/

# Calculate Checksum. Looks deceptively easy; I'll test this on a Rockblock tomorrow...
checksum = sum(packed_data)
print("Checksum: " + str(checksum))
higher_byte = checksum >> 8
lower_byte = checksum & 0xFF
print(higher_byte)
print(lower_byte)

# Now unpack it
print(s.unpack(packed_data))