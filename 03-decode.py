
#!/usr/bin/env python3

"""
Decode the string.
"""

import pathlib
import base64
import numpy as np
from PIL import Image
import collections
import pprint

path = pathlib.Path.cwd()
input_filename = str(path / 'result' / 'result.txt')
output_filename = str(path / 'result' / 'result.png')

with open(input_filename, encoding='utf-8') as reader:
    text = reader.read()
    print('Input text [{}]:\n{}'.format(len(text), text))

    c = collections.Counter(text)
    print('Counter:')
    pprint.pprint(c)
    word = [k for k,v in c.items() if k.isalpha()]
    print(word)

    # Cleanup
    text = text.replace("@", "c")
    print('Input text cleaned [{}]:\n{}'.format(len(text), text))

    cc = collections.Counter(text)
    print('Counter cleaned:')
    pprint.pprint(cc)

    word = [k for k,v in c.items() if k.isalpha()]
    print(word)

    base64_bytes = text.encode('utf-8')

    missing_padding = len(base64_bytes) % 4
    if missing_padding:
        base64_bytes += b'='* (4 - missing_padding)

    print('Input bytes:\n{}'.format(base64_bytes))

    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('utf-8', 'replace')
    print('Decoded text:\n{}'.format(message))

    arr = list(base64_bytes)
    # print(arr)

    arr = np.asarray(arr, dtype=np.uint8)
    matrix = arr.reshape(8, 931)
    img = Image.fromarray(matrix)
    img.save(output_filename, "PNG")