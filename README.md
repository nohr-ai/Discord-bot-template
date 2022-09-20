# Discord-bot-template
Template for creating discord bots in python

## Requirements
---
This implementation requires python version >= 3.10

See `requirements.txt` for further dependencies

## Setup
---
1. To interact with the discord api and get access to your server, we need an access token
    - Go to `https://discord.com/developers/applications`
        - Under 'Applications'
            - Select 'New Applicaion'
            - Name your bot something meaningful
            - Accept terms and press create
        - After creating your application find the setting 'Bot'
            - Select 'Add Bot'
                - Yes, do it!
            - If you cannot see your token:
                - Select Reset Token
            - Create a file 'auth' in your repository
                - Copy the token into the file
                - Save

2. Install dependencies
    - With python3.10 or later, install dependencies found in 'requirements.txt'
        - python3.10 -m pip install -r requirements.txt

3. Configure the bot
    - In order for the bot to work, it needs to know what server it's suppose to listen/talk to and what members it should listen to
        - You can write the config file `config.json` yourself 
        - or
        - Run the bot and do the setup from terminal
            - The results are stored in `config.json`

## Running the bot
---
- `python3.10 bot.py`

## Adding your own logic
---
See templateHandler.py for an idea how to start

1. To create a handler
    - Copy the templateHandler into a new file
    - Add your new methods with fitting names
        - For messages: `def message_myMethod(self, message, permission)`
            - To invoke this handler, send `!myMethod` in a channel that the bot is in
            - Please note: The convention for sending commands is to prefix them with `!`
            - Message is an object defined in the discord.py api:
                - See: [discord.py](https://discordpy.readthedocs.io/en/stable/api.html#messages)
        - For reactions: `def reaction_add(self, reaction, permission)`
            - reaction is an object defined in the discord.py api:
                - See: [discord.py](https://discordpy.readthedocs.io/en/stable/api.html#rawreactionactionevent)
            - Permission is the permission-level for the user invoking the method
                - Defined in: constants.py
            - Please note: reaction methods can only be either `add` or `remove`

2. To add a handler 
    - Create a line in handlers.py that imports your handler
    - Add a line that adds your handler to the list of handlers

