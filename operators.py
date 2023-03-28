import bpy
from .script_parser import parse_chatgpt_response
from .chatgpt import generate_mesh_script


class ChatGPT_OT_CreateMesh(bpy.types.Operator):
    bl_idname = "object.chatgpt_create_mesh"
    bl_label = "Create Mesh"
    bl_options = {"REGISTER", "UNDO"}

    prompt: bpy.props.StringProperty(name="Prompt")

    def execute(self, context):
        mesh_script = generate_mesh_script(self.prompt)
        parse_chatgpt_response(mesh_script)
        
        # Ensure a Text Editor is open
        for area in bpy.context.screen.areas:
            if area.type == 'TEXT_EDITOR':
                break
        else:
            bpy.ops.screen.area_split(direction='VERTICAL', factor=0.5)
            area = bpy.context.screen.areas[-1]
            area.type = 'TEXT_EDITOR'

        # Create a new text block and paste the generated script
        bpy.ops.text.new()
        text_data = bpy.data.texts[-1]
        text_data.name = "GeneratedMeshScript.py"
        text_data.from_string(mesh_script)

        # Set the active text block in the Text Editor to the generated script
        for space in area.spaces:
            if space.type == 'TEXT_EDITOR':
                space.text = text_data
                break

        # Run the script to create the mesh
        override = {'area': area, 'space_data': space}
        bpy.ops.text.run_script(override)

        return {"FINISHED"}

def register():
    bpy.utils.register_class(ChatGPT_OT_CreateMesh)

def unregister():
    bpy.utils.unregister_class(ChatGPT_OT_CreateMesh)
