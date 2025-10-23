import os
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
import mlx_whisper
from pydub import AudioSegment
import numpy as np

# 音声ファイルを指定して文字起こし
def Transcription():
    audio_file_path = "python-audio-output.wav"

    result = mlx_whisper.transcribe(
        audio_file_path,
        path_or_hf_repo="mlx-community/whisper-base-mlx"
    )

    text = result["text"].strip()
    print(text)
    
    return text