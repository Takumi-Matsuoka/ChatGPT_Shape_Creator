import os

def get_api_key():
    # 現在のファイル（config.py）のディレクトリパスを取得
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # 現在のディレクトリパスに、"api_key.txt"を追加してパスを作成
    api_key_file = os.path.join(current_directory, "api_key.txt")
    
    # "api_key.txt"を開いて、APIキーを読み込む
    with open(api_key_file, "r") as f:
        api_key = f.read().strip()
    return api_key