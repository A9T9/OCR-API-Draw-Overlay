"""
**************************************
OCR.space OCR Result Checker
**************************************

=> Draw OCR overlay on top of image

This little Python tool takes the OCR.space JSON output as input, and draws an overlay on top of the image. 

The tool can be useful - for example - to test and debug OCR results.

Free OCR API => https://ocr.space/OCRAPI

---------------------
License: Open-Source MIT License  - https://opensource.org/licenses/MIT

V1.1  - 20211125
V2.0  - 20220130
"""

import sys
from PIL import Image, ImageDraw, ImageFont
import json
import os
from os import path

# install: pip install --upgrade arabic-reshaper
import arabic_reshaper

# install: pip install python-bidi
from bidi.algorithm import get_display

unicode_font_name = "./Arial Unicode.ttf"

TINT_COLOR = (255, 255, 0) 
TRANSPARENCY = .70  # Degree of transparency, 0-100%
OPACITY = int(255 * TRANSPARENCY)

if len(sys.argv) != 3:
    print("Usage: python3 " + sys.argv[0] + " image_file_name json_file_name")
    exit(-1)

image_file_name = sys.argv[1]
json_file_name = sys.argv[2]

if not path.exists(image_file_name):
    print("File not found: " + image_file_name)
    exit(-1)

if not path.exists(json_file_name):
    print("File not found: " + json_file_name)
    exit(-1)

img = Image.open(image_file_name)
img = img.convert("RGBA")

overlay = Image.new('RGBA', img.size, TINT_COLOR+(0,))
draw = ImageDraw.Draw(overlay)  # Create a context for drawing things on it.

with open(json_file_name, encoding="utf8") as data_file:
    data = json.load(data_file)

image_file_name_without_extension = os.path.splitext(image_file_name)[0]
is_arabic = image_file_name_without_extension.endswith("_ara")

for pr in data["ParsedResults"]:
    for line in pr["TextOverlay"]["Lines"]:
        for w in line["Words"]:
            x1 = (w["Left"], w["Top"])
            x2 = (x1[0] + w["Width"], x1[1] + w["Height"])

            # Adjust font size according to the rectangle height
            font_size = abs(x1[1] - x2[1])
            font = ImageFont.truetype(unicode_font_name, int(font_size))

            draw.rectangle((x1, x2), fill=TINT_COLOR+(OPACITY,))

            text = w["WordText"]
            if is_arabic:
                reshaped_text = arabic_reshaper.reshape(text)    # correct its shape
                bidi_text = get_display(reshaped_text)           # correct its direction
                text = bidi_text

            draw.text(x1, text, fill=(255, 0, 0, 255), font=font)

        
img = Image.alpha_composite(img, overlay)

output_file_name = image_file_name_without_extension + "_overlay.png"
img.save(output_file_name)
#img.show()

