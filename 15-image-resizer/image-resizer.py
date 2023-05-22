# Install pillow
# Install pillow
# pip3 install Pillow

# Import Image from Pillow
from PIL import Image

def resize_image(size1, size2):
    
    image = Image.open('test.png')

    print(f"Current size: {image.size}")

    resized_image = image.resize((size1, size2))

    resized_image.save('test-' + str(size1) + '.png')

size1 = int(input('Write width: '))
size2 = int(input('Write lenght: '))

resize_image(size1, size2)