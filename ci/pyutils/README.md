# How to setup environment
create virtual environment, e.g.
```batch
virtualenv .venv
```

copy `ci/pyutils/<system>.pth ` to `.venv`'s `site-packages` dir, e.g.
```batch
copy ci\pyutils\win.pth .venv\Lib\site-packages\
```
