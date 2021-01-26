from PIL import Image

WIDTH, HEIGHT = 5, 5
FILENAME = ("teste_pillow.png", "PNG")

pillow_obj = Image.new("RGB", (WIDTH, HEIGHT))
pixel_set = pillow_obj.load()

isBlack = True
for row in range(HEIGHT):
  for col in range(WIDTH):
    color = (0, 0, 0) if isBlack else (255, 255, 255)
    isBlack = not isBlack
    pixel_set[col, row] = color

pillow_obj.save(*FILENAME)