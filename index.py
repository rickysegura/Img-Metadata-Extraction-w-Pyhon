# Written by Ricky Segura
# POC: rickysegura2001@gmail.com

# Imports
from pyexpat import model
from re import M
import PIL
from PIL import Image
from PIL.ExifTags import TAGS

# open the image
IMAGE = Image.open("test.jpg")

# exctract other basic metadata
INFO_DICT = {
    "filename":IMAGE.filename,
    "Image Size":IMAGE.size,
    "Image Height": IMAGE.height,
    "Image Width": IMAGE.width,
    "Image Format": IMAGE.format,
    "Format Description":IMAGE.format_description,
    "Image Mode": IMAGE.mode,
    "Image is Animated": getattr(IMAGE, "is_animated", False),
    "Frames in Image": getattr(IMAGE, "n_frames", 1),
}

for label,value in INFO_DICT.items():
    print(f"{label:25}: {value}")

from exif import Image as McDoodle

MY_IMAGE = McDoodle("test.jpg")

def THERE_IS_DATA():
    print(f"EXIF Dictionary: {MY_IMAGE.list_all()}")

if MY_IMAGE.has_exif:
    THERE_IS_DATA()
elif MY_IMAGE.has_exif == False:
    print(f"EXIF DATA: {MY_IMAGE.has_exif}")
