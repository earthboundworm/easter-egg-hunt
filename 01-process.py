#!/usr/bin/env python3

"""
Convert each frame to a grayscale image.
"""

import cv2
import pathlib
from progress.bar import Bar

path = pathlib.Path.cwd()
input_path = path / 'frames'
output_path_gray = path / 'frames-gray'
output_path_threshold = path / 'frames-threshold'

num_frames = 7448

bar = Bar('Processing', max=num_frames)

for i in range(num_frames):
    filename = 'clue-{:04d}.png'.format(i)

    input_filename = str(input_path / filename)
    output_filename_gray = str(output_path_gray / filename)
    output_filename_threshold = str(output_path_threshold / filename)

    img = cv2.imread(input_filename)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_filename_gray, img_gray)

    img_threshold = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    cv2.imwrite(output_filename_threshold, img_threshold)

    bar.next()
    
bar.finish()