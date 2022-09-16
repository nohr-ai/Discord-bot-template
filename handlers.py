from functools import partial
from templateHandler import TemplateHandler
from genericMessageHandler import GenericMessageHandler

message_handlers = [
    partial(TemplateHandler, "Template handler", "Nothing to see here", False),
    partial(GenericMessageHandler, "???", "Not implemented", True)]

reaction_handlers = [
    partial(TemplateHandler, "Template Handler", "Nothing to see here", False)
]
