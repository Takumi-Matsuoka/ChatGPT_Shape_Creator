def parse_chatgpt_response(response_text):
    # 必要な前処理を行います（例：改行や不要な文字を削除）
    # 必要に応じて、テキストを分析し、適切なPythonコードに変換します
    
    # "size" を "radius" に置き換える
    mesh_script = response_text.replace("size=", "radius=")
    
    return mesh_script
