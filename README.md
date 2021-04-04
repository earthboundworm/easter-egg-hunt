# Easter Egg Hunt

https://wensveen.wordpress.com/2021/03/28/easter-egg-hunt/

First, convert the animated gif to separate frames:
```
convert ./original/clue.gif ./frames/clue-%04d.png
```

Start the Python shell with
```
pipenv install
pipenv shell
```

Next, convert the frames to text. See the `result` folder for the output text file.
```
python 01-process.py
python 02-convert.py
```

Next, attempt to decode the string with 
```
python 03-decode.py
```
