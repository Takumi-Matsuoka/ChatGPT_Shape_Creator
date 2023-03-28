import bpy
from .operators import ChatGPT_OT_CreateMesh

class ChatGPT_PT_Panel(bpy.types.Panel):
    bl_label = "ChatGPT"
    bl_idname = "OBJECT_PT_chatgpt"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "ChatGPT Shape Creator"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True

        row = layout.row()
        row.prop(context.scene, "chatgpt_prompt", text="Prompt")

        row = layout.row()
        row.operator("object.chatgpt_create_mesh", text="CreateMesh").prompt = context.scene.chatgpt_prompt

def register():
    bpy.utils.register_class(ChatGPT_PT_Panel)
    bpy.types.Scene.chatgpt_prompt = bpy.props.StringProperty(name="Prompt")

def unregister():
    bpy.utils.unregister_class(ChatGPT_PT_Panel)
    del bpy.types.Scene.chatgpt_prompt
