import os
from .src import EasyPony

WEB_DIRECTORY = os.path.join(os.path.dirname(__file__), "js")

NODE_CLASS_MAPPINGS = {
    "EasyPony": EasyPony,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EasyPony": "Tokens",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
