# Uninstall Python and their Env variables

# Install miniconda from [conda](https://docs.conda.io/en/main/miniconda.html)

# SETUP
## create isolated environment
```
conda create --name tenv
```

## start isolated environment
```
conda activate tenv
```

## install required packages
```
pip install telethon crypty py-mon watchdog requests pyshorteners
# OR
pip install -r requirements.txt
```

## start bot
```
pymon main.py
```

# Packages used
- telethon
- crypty
- py-mon
- watchdog
- requests
- pyshorteners

# NOTE:
Edit `strings.py` to make it work properly.
