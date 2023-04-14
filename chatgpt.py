import bpy
import openai

def generate_mesh_script(prompt):
    # Get API key from addon preferences
    addon_prefs = bpy.context.preferences.addons[__package__].preferences
    api_key = addon_prefs.api_key

    openai.api_key = api_key

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Create a Blender Python script to generate a 3D mesh based on the following description: {prompt}",
        temperature=0.5,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    mesh_script = response.choices[0].text.strip()
    return mesh_script