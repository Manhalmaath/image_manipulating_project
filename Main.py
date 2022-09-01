import os
from PIL import Image

if 'opt' not in os.listdir('.'):
    os.mkdir('opt')
if 'icons' not in os.listdir('opt'):
    os.mkdir(os.path.join('opt', 'icons'))

images = os.listdir('images')
for image in images:
    if image.startswith('.'):
        continue
    with Image.open(os.path.join('images', image)) as img:
        img.rotate(-90).convert('RGB').resize((128, 128)).save(os.path.join('opt', 'icons', image), "JPEG")
