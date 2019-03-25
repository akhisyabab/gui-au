# Automatic GUI Process
Build with pyautogui lib: https://pyautogui.readthedocs.io/en/latest/index.html

## Installation
```
$ python3 -m virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

# Notes
This tool is used for examples of auto gui for chrome applications and text editor

## Steps
1. get your current cursor position. Point it to opened app tab in bottom and run ```python3 cursor.py```
2. edit run.py and edit tab1, tab2, etc.  x, y result from step above
3. (example) if chrome in first opened app tab, so at the bottom run.py is ```chrome(tab1)```


*. move the cursor to the upper-left will stop your program 