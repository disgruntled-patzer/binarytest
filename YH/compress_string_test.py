#!/usr/bin/env python3

# Copyright (C) 2020, Lau Yan Han (sps08.lauyanhan@gmail.coms)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>

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