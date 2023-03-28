import openai
import os

def read_api_key():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    api_key_path = os.path.join(script_dir, "api_key.txt")
    with open(api_key_path, "r") as f:
        return f.read().strip()

def generate_mesh_script(prompt):
    openai.api_key = read_api_key()

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
