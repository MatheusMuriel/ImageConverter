import struct
import zlib

f = open('teste_15.png', 'rb')
header = f.read(8)
#print("%s: %s" % ('Header', header))

formatLenght = '>I' # >(big-endian), I(unsigned int)
formatType = '>4s' # >(big-endian), 4s(String with 4 bytes)
formatCrc = '>I' # >(big-endian), I(unsigned int)
endOfFile = b'IEND'

def readChunk():
  chunk = {}
  chunk["lenght"] = struct.unpack( formatLenght, f.read(4) )[0]
  chunk["type"] = struct.unpack( formatType, f.read(4) )[0]
  chunk["data"] = f.read(chunk["lenght"])
  # Calcular CRC aqui
  chunkCrc = struct.unpack(formatCrc, f.read(4))[0]
  return chunk

chunks = []
while True:
  chunk = readChunk()
  chunks.append(chunk)
  if (chunk["type"] == endOfFile):
    break

# Metadados
metadataChunk = chunks[0]
imageWidth = struct.unpack('>I', metadataChunk["data"][:4])[0]
imageHeigth = struct.unpack('>I', metadataChunk["data"][4:8])[0]
bitDepth = struct.unpack('>B', metadataChunk["data"][8:9])[0]
colorType = struct.unpack('>B', metadataChunk["data"][9:10])[0]
compressionMethod = struct.unpack('>B', metadataChunk["data"][10:11])[0]
filterMethod = struct.unpack('>B', metadataChunk["data"][11:12])[0]
interlaceMethod = struct.unpack('>B', metadataChunk["data"][12:13])[0]

idatData = b''.join(chunk["data"] for chunk in chunks if chunk["type"] == b'IDAT')
imageData = zlib.decompress(idatData)

# Tratar aqui o filter type

pixel = 3 if colorType == 2 else 4;

paso = imageWidth * pixel

_i = 0
for i in range(imageHeigth):
  _i += 1
  pixel = []
  for j in range(imageHeigth):
    pixelValues = []
    for k in range(3):
      data_x = imageData[_i]
      pixelValues.append(data_x)
      _i += 1
    print(pixelValues)
    pixel.append(pixelValues)
  print("---")
  
