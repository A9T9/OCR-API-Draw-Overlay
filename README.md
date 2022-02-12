**************************************
OCR.space OCR Result Checker
**************************************

=> Draw OCR overlay on top of image

Python tool that takes the OCR.space JSON output as input, and draws an overlay on top of the image. 

The tool can be useful - for example - to test and debug OCR results from the 
[Free OCR API](https://ocr.space/OCRAPI).

---------------------
License: Open-Source MIT License  - https://opensource.org/licenses/MIT

V1.1  - 20211125
V2.0  - 20220130
V2.1  - 20220212

---------------------


How to use it:

- Make sure you have python 3 installed.

- Make sure you have pillow (PIL, Python Imaging Library) installed.
  pip install pillow

- These libraries must be installed For Arabic (right to left) support.
  pip install --upgrade arabic-reshaper
  pip install python-bidi

- Each platform may have different fonts for Unicode which include Chinese characters and they are in different folders. 
  In order to make it standard across platforms we included Arial Unicode.ttf font within this project.

- Keep Arial Unicode.ttf in the same folder with the script.

- Usage example:

  ```python overlay.py input.jpg input.json``` **[=> output will be INPUT file name with "_overlay.png" added.]**
  
  OR depending on your python installations and configurations
  
  ```python3 overlay.py input.jpg input.json```

- Input can be both jpeg and png. Output will always be a png.



Added Arabic (right to left text) support:

If an image file name (before extension) ends with "_ara" then right to left logic is applied.
