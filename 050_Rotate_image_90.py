import sys
import os
import os.path
from PIL import Image


jpg = sys.argv[1]

split = jpg.split("\\")
name_img = split[-1]
name_archive = name_img.split(".")
name = name_archive[0]

way = os.path.dirname(os.path.abspath(jpg))

original_image = Image.open(jpg)

rotated_image = original_image.rotate(90)
rotated_image.save(f"{way}\{name}_rotated.jpg")

# "C:\Users\Milton\Documents\Chorris_skate.jpg"