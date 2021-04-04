
#!/usr/bin/env python3

"""
Decode the string.
"""

import pathlib
import base64
import numpy as np
from PIL import Image

path = pathlib.Path.cwd()
input_filename = str(path / 'result' / 'result.txt')
output_filename = str(path / 'result' / 'result.png')

with open(input_filename, encoding='ascii') as reader:
    text = reader.read()
    print('Input text:\n{}'.format(text))

    base64_bytes = text.encode('ascii')

    missing_padding = len(base64_bytes) % 4
    if missing_padding:
        base64_bytes += b'='* (4 - missing_padding)

    print('Input base64_bytes:\n{}'.format(base64_bytes))

    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii', 'replace')
    print('Decoded text:\n{}'.format(message))

    arr = list(message_bytes)

    arr = np.asarray(arr, dtype=np.uint8)

    print(len(arr))

    matrix = arr.reshape(39, 5)

    print(matrix)
    img = Image.fromarray(matrix)
    img.save(output_filename, "PNG")