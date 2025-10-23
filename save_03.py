# save_txt.py
import os
from Transcription import Transcription  # 02.py の関数を import

# 保存先フォルダと固定ファイル名
FOLDER = "."
FILENAME = os.path.join(FOLDER, "transcription.txt")  # 1つのファイルに固定

def save_transcription(text: str, file_path: str = FILENAME) -> str:
    """
    文字起こし結果を1つのファイルに追記する関数。
    """
    # 保存先フォルダがなければ作成
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # 追記モードでファイルに書き込む（改行して追記）
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(text + "\n")

    return file_path

# 実行例
if __name__ == "__main__":
    text = Transcription()  # 02.py の文字起こし関数を呼ぶ
    saved_path = save_transcription(text)
    print(f"文字起こし結果を保存しました: {saved_path}")
