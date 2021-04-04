
#!/usr/bin/env python3

"""
Convert each frame to a character.
Write the resulting string to an output text file.
"""

import cv2 
import pytesseract
import pathlib
from progress.bar import Bar

path = pathlib.Path.cwd()
input_path = path / 'frames-gray'
output_path = path / 'result'

# Adding custom options (single character recognition)
custom_config = r'--oem 3 --psm 10'

num_frames= 7448
output_filename = str(output_path / "result.txt")

with open(output_filename, 'w') as writer:

    bar = Bar('Converting', max=num_frames) 

    for i in range(num_frames):
        filename = 'clue-{:04d}.png'.format(i)
        input_filename = str(input_path / filename)

        img = cv2.imread(input_filename)
        
        character = pytesseract.image_to_string(img, config=custom_config)

        # Remove whitespace, pick first character
        character = character.rstrip()[0]
        # print("{} => {}".format(filename, character))

        writer.write(character)

        bar.next()
    
    bar.finish()
