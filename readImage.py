import struct
import zlib

f = open('test_xadrez.png', 'rb')
print("%s: %s" % ('Header', f.read(8)))

## Chunks
formatLenght = '>I' # >(big-endian), I(unsigned int)
chunkLength = struct.unpack( formatLenght, f.read(4) )[0]
print(chunkLength)
formatType = '>4s' # >(big-endian), 4s(String with 4 bytes)
chunkType = struct.unpack( formatType, f.read(4) )[0]
print(chunkType)
chunkData = f.read(chunkLength)
print(chunkData)
# Calcular CRC aqui
formatCrc = '>I'
chunkCrc = struct.unpack(formatCrc, f.read(4))[0]
print(chunkCrc)
