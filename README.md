[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/Sasja/z340/master?filepath=z340.ipynb)

## The Zodiac Killer's unsolved z340: like a fake substitution cipher
Testdriving Jupyter Notebook based on [superpumpie's blogpost](http://tsjuzek.com/blog/z340.html) ([github repo](https://github.com/superpumpie/z340))

## How to use this notebook
### Online static:
Just view the file [z340.ipynb](z340.ipynb) on github.

### Online interactive:
Click the Binder badge above or [here](https://mybinder.org/v2/gh/Sasja/z340/master?filepath=z340.ipynb)

### Run the notebook locally on Ubuntu:
1. clone the this repo into an appropriate folder
2. run
```bash
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
jupyter notebook z340.ipynb
```
3. the notebook should now open in your browser
