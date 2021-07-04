# Easter Egg Hunt

https://wensveen-wordpress-com.cdn.ampproject.org/c/s/wensveen.wordpress.com/2021/04/12/easter-egg-hunt-solution/amp/

## Zeroth egg

https://wensveen.wordpress.com/2021/03/28/easter-egg-hunt/

## First egg

View the contents of the gif file with:
```
cat ./original/clue.gif | head
```

This yields the URL for the first egg:

https://drive.google.com/file/d/1JObjSCDkcerk6bWs5VDB_h-LU8c5hXht/view

The hint is `ZIP`.

## Second egg

Work in progress. First attempt:

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

## Third egg


## Fourth egg
