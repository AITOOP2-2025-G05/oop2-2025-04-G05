import mlx_whisper
from pydub import AudioSegment
import numpy as np

# 音声ファイルを指定して文字起こし
audio_file_path = "python-audio-output.wav"

# result = mlx_whisper.transcribe(
#   audio_file_path, path_or_hf_repo="whisper-base-mlx"
# )
# print(result)
result = mlx_whisper.transcribe(
    audio_file_path,
    path_or_hf_repo="mlx-community/whisper-base-mlx"  # ←これが正
)
# print(result)

text = result["text"].strip()
print(text)