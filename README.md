# Pycord Bot

## Requirements
Rename `.example.env` to `.env` and paste your Discord Bot Token after `TOKEN=` in it. 

## To Run Locally
Before running the bot you will need to install all the requirements with this command:

```
python3 -m pip install -r requirements.txt
```

After that you can start it with

```
python3 bot.py
```

## To Run on an Open Ocean Ubuntu 24.04 (LTS) x64 OS from scratch
```
apt install python3-pip
apt install python3.12-venv
mkdir ~/.virtualenvs
python3 -m venv ~/.virtualenvs/botenv
source ~/.virtualenvs/botenv/bin/activate
pip install -r requirements.txt
python3 bot.py
```