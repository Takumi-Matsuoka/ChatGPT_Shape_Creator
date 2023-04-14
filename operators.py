import bpy
from .script_parser import parse_chatgpt_response
from .chatgpt import generate_mesh_script

class ChatGPT_OT_CreateMesh(bpy.types.Operator):
    bl_idname = "object.chatgpt_create_mesh"
    bl_label = "Create Mesh"
    bl_options = {"REGISTER", "UNDO"}

    prompt: bpy.props.StringProperty(name="Prompt")

    def execute(self, context):
        preferences = context.preferences.addons[__package__].preferences
        if not preferences.api_key:
            self.report({"WARNING"}, "Please enter your API key in the addon preferences.")
            return {"CANCELLED"}
        instructions = (f"You are an assistant made for the purposes of helping the user with Blender, the 3D software. "
                        f"- Respond with your answers in markdown (```). "
                        f"- Preferably import entire modules instead of bits. "
                        f"- Do not perform destructive operations on the meshes. "
                        f"- Do not use cap_ends. Do not do more than what is asked (setting up render settings, adding cameras, etc)"
                        f"- Do not respond with anything that is not Python code."
                        f"\n\nuser: {self.prompt}")

        mesh_script = generate_mesh_script(instructions)
        mesh_script = mesh_script.replace("```", "").strip()  # Remove markdown backquotes
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
        try:
            bpy.ops.text.run_script(override)
        except Exception as e:
            self.report({"ERROR"}, f"Script execution failed: {str(e)}")
            return {"CANCELLED"}

        return {"FINISHED"}

class ChatGPTAddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    api_key: bpy.props.StringProperty(
        name="API Key",
        description="Enter your OpenAI API key",
        default="",
        subtype="PASSWORD",
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "api_key")

def register():
    bpy.utils.register_class(ChatGPTAddonPreferences)
    bpy.utils.register_class(ChatGPT_OT_CreateMesh)

def unregister():
    bpy.utils.unregister_class(ChatGPTAddonPreferences)
    bpy.utils.unregister_class(ChatGPT_OT_CreateMesh)