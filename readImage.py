import struct
import zlib

f = open('test_xadrez.png', 'rb')
print("%s: %s" % ('Header', f.read(8)))

formatLenght = '>I' # >(big-endian), I(unsigned int)
formatType = '>4s' # >(big-endian), 4s(String with 4 bytes)
formatCrc = '>I' # >(big-endian), I(unsigned int)

def readChunk():
  chunk = {}
  chunk["lenght"] = struct.unpack( formatLenght, f.read(4) )[0]
  chunk["type"] = struct.unpack( formatType, f.read(4) )[0]
  chunk["data"] = f.read(chunk["lenght"])
  # Calcular CRC aqui
  #chunkCrc = struct.unpack(formatCrc, f.read(4))[0]
  return chunk

print(readChunk())

