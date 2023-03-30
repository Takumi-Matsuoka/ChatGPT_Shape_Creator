bl_info = {
    "name": "ChatGPT Shape Creator",
    "author": "Takumi Matsuoka",
    "version": (0, 1, 1),
    "blender": (2, 80, 0),
    "location": "View3D > Tool Shelf > ChatGPT Shape Creator",
    "description": "Creates mesh shapes using ChatGPT",
    "warning": "",
    "wiki_url": "",
    "category": "Object",
}

import bpy
from . import operators, panels
from .script_parser import parse_chatgpt_response

def register():
    operators.register()
    panels.register()

def unregister():
    operators.unregister()
    panels.unregister()

if __name__ == "__main__":
    register()
