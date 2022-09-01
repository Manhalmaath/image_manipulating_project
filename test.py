from PIL import Image
import os

Image.open(os.path.join('images', 'ic_beenhere_white_48dp')).rotate(90).convert('RGB').resize(
    (128, 128)).save(os.path.join('opt', 'icons', 'ic_beenhere_white_48dp' + '.jpeg'))
im = Image.open(os.path.join('opt', 'icons', 'ic_beenhere_white_48dp' + '.jpeg'))
print(im.format, im.size, im.mode)
