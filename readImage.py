import struct
import zlib

f = open('test_xadrez.png', 'rb')
print("%s: %s" % ('Header', f.read(8)))