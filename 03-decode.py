
#!/usr/bin/env python3

"""
Decode the string.
"""

import pathlib
import base64
import numpy as np
from PIL import Image
import collections

path = pathlib.Path.cwd()
input_filename = str(path / 'result' / 'result.txt')
output_filename = str(path / 'result' / 'result.png')

with open(input_filename, encoding='ascii') as reader:
    text = reader.read()
    print('Input text []:\n{}'.format(len(text), text))

    c = collections.Counter(text)
    print('Counter:\n{}', c)

    # Cleanup
    text = text.replace("@", "c")
    print('Input text cleaned []:\n{}'.format(len(text), text))

    cc = collections.Counter(text)
    print('Counter cleaned:\n{}', cc)

    base64_bytes = text.encode('ascii')

    missing_padding = len(base64_bytes) % 4
    if missing_padding:
        base64_bytes += b'='* (4 - missing_padding)

    # Remove the 4 padded bytes at end
    base64_bytes = base64_bytes[:-4]
    print('Input bytes:\n{}'.format(base64_bytes))

    arr = list(base64_bytes[:-4])
    arr = np.asarray(arr, dtype=np.uint8)

    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii', 'replace')
    print('Decoded text:\n{}'.format(message))

    # Is it perhaps an image?
    # matrix = arr.reshape(200, 40)
    # img = Image.fromarray(matrix)
    # img.save(output_filename, "PNG")