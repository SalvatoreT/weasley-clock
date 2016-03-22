# Weasley Clock [![Build Status](https://travis-ci.org/SalvatoreT/weasley-clock.svg?branch=master)](https://travis-ci.org/SalvatoreT/weasley-clock)
See who's home on your Raspberry Pi or any small screen

## Install
To get the ball rolling quickly, I have a virtual environment set up.

```bash
# Download the code
git clone https://github.com/SalvatoreT/weasley-clock.git
cd weasley-clock
# Create a virtual environment
virtualenv venv # not winning any awards for create naming
source venv/bin/activate # run deactivate to stop
pip install -r requirements.txt # pull in the requirements
```

## Run
```bash
./weasley_clock.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```