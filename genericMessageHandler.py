import re
import inspect
import logging
import discord


class GenericMessageHandler:
    def __init__(self, help_text, response, reply_private, log_level=logging.WARNING):
        self.command_prefix = '!'
        self.message_prefix = "message_"
        self.reaction_prefix = "reaction_"
        self.response = response
        self.help_text = help_text
        self.reply_private = reply_private
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(log_level)

    async def unhandled(self, message):
        await self.reply(message, "Unimplemented")

    async def reply(self, input, response):
        if self.reply_private:
            message = await input.author.send(response)
        else:
            message = await input.channel.send(response)
        return message

    async def dispatch(self, message, permission):
        if isinstance(message, discord.Message):
            result = re.match("^!([a-zZ-a]*)", message.content)
            if result:
                group = result.group(1)
                for name, method in inspect.getmembers(self, predicate=inspect.ismethod):
                    if name == self.message_prefix+group:
                        await method(message, permission)
        if isinstance(message, discord.RawReactionActionEvent):
            match message.event_type:
                case 'REACTION_ADD':
                    for name, method in inspect.getmembers(self, predicate=inspect.ismethod):
                        if name == self.reaction_prefix+"add":
                            await method(message, permission)
                case "REACTION_REMOVE":
                    for name, method in inspect.getmembers(self, predicate=inspect.ismethod):
                        if name == self.reaction_prefix+"remove":
                            await method(message, permission)
