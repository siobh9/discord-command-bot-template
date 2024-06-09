# Pycord Bot

To connect this bot to your Discord server with the necessary permissions, you'll have to have 
1. Created an application on Discord
2. Categorized it as a bot
3. Gone to this URL to authorize your bot on the server(s) you want it: `https://discord.com/oauth2/authorize?client_id=<BOT_CLIENT_ID>&permissions=<PERMISSIONS>&integration_type=0&scope=bot+applications.commands` where
   - BOT_CLIENT_ID is also referred to as a bot's Application ID by Discord
   - PERMISSIONS is an integer that can be determined at the bottom of this page https://discord.com/developers/applications/YOUR_APPLICATION_ID_HERE/bot - you'll need to give permission to Read Channels, Send Messages, and Use Slash Commands (2147486720 at the time of writing but please always verify for your own bots)

## Requirements
Rename `.example.env` to `.env` and fill it in wither your Discord Bot Token and Server Ids you'd like to add the bot to. 

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

The last command in here will start the bot in the background so that the bot doesn't stop when you close your terminal, you can see it by running `ps` and looking for the line that says `python`.
```
apt install python3-pip
apt install python3.12-venv
mkdir ~/.virtualenvs
python3 -m venv ~/.virtualenvs/botenv
source ~/.virtualenvs/botenv/bin/activate
pip install -r requirements.txt
nohup python3 bot.py &
```

## Notes

### On slash vs prefixed Discord commands, and unprefixed commands/moderating use cases
[This commit](https://github.com/seanmc9/pycord-test/commit/c80bf79b0ec75c7480e1fa44fe9584bae10abb0e) contains the logic (and importantly the classes imported from the correct level of abstraction) necessary to support *both* slash and prefixed commands. What I have learned, however, is that you only really need one or the other; where things really break down is if you want unprefixed commands (the use case really being that the user doesn't know they're saying a command/moderating bots), then with how the abstraction is set up it actually makes sense to have 2 different bots at that point - because that sort of thing is easy to do with the Client library, but you lose access to all of the packaging in the higher abstraction Command classes (that support slash and prefixed commands) and they don't support client-level stuff (because that's what they abstract away - namely `on_message()`).

tldr: make separate bots for commands bots and moderating bots because the levels of abstraction in the code is setup to work that way/you might as well not use them if you try to do everything in one bot.