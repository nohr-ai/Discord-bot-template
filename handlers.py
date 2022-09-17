from functools import partial
from templateHandler import TemplateHandler
from genericMessageHandler import GenericMessageHandler

handlers = [
    TemplateHandler("Template handler", "Nothing to see here", False),
    GenericMessageHandler("???", "Not implemented", True)
]
