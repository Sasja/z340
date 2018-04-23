[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/Sasja/z340/master?filepath=z340.ipynb)

# z340
Testdriving Jupyter Notebook using superpumpie's blog post [The Zodiac Killer's unsolved z340: like a fake substitution cipher](http://tsjuzek.com/blog/z340.html) ([github repo](https://github.com/superpumpie/z340))

# How to run this notebook
## online
Simply click the Binder badge above

## locally on ubuntu
1. clone the this repo in an appropriate folder
2. run
```bash
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
jupyter notebook z340.ipynb
```
3. the notebook should now open in your browser
