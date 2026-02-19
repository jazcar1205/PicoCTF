# import PIL module
from PIL import Image
# Front Image
fOne = 'scrambled1.png'
# Back Image
fTwo = 'scrambled2.png'

fNew = PIL.Image.new(mode="RGB", size=(iOne.size[0], iOne.size[0]))

frontImage = Image.open(filename)

# Open Background Image
background = Image.open(filename1)

#Convert image to RGBA
iOne = frontImage.convert("RGBA")

# Convert image to RGBA
iTwo = background.convert("RGBA")

# Calculate width to be at the center
width = (background.width - frontImage.width) // 2

# Calculate height to be at the center
height = (background.height - frontImage.height) // 2

# Paste the frontImage at (width, height)
background.paste(frontImage, (width, height), frontImage)

# Save this image
background.save("new.png", format="png")

pixels = img.load() # create the pixel map

for i in range(img.size[0]): # for every pixel:
    for j in range(img.size[1]):
        if pixels[i,j] != (255, 0, 0):
            # change to black if not red
            pixels[i,j] = (0, 0 ,0)
