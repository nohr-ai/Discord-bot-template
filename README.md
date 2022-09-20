# Discord-bot-template
Template for creating discord bots in python

## Requirements
---
This implementation requires python version >= 3.10

See `requirements.txt` for further dependencies

## Setup
---
1. Clone the repository to your machine
2. To interact with the discord api and get access to your server, we need an access token
    - Go to [discordDeveloperPortal](https://discord.com/developers/applications)
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
        - The bot requires privileged intents to access members and messages in your server, enable:
            - `SERVER MEMBERS INTENT`
            - `MESSAGE CONTENT INTENT`


3. We will now invite the bot to your server:
    - Under `OAuth2`:
        - `URL Generator`
            - Select `bot`
            - No permissions needed by default
                - Repeat this step with diferent permissions if you require it later
            - Copy the generated URL into your browser's search field

4. Install dependencies
    - With python3.10 or later, install dependencies found in 'requirements.txt'
        - python3.10 -m pip install -r requirements.txt

5. Configure the bot
    - In order for the bot to work, it needs to know what server it's suppose to listen/talk to and what members it should listen to
        - You can write the config file `config.json` yourself 
        - or
        - Run the bot and do the setup from terminal
            - The results are stored in `config.json`
        - By default the bot listens to all members in the server
            - You can set 1 special role_ID `member_role_ID` if you want special authorization for some members

## Running the bot
---
- `python3.10 bot.py`
- The bot should send a message `I'm online' to your server's general channel
    - Try reach the template handler by typing the command `!template` in the chat

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

