import ffmpeg
import os

# 固定の出力ファイル名を作業者間で決定
FIXED_OUTPUT_FILE = 'python-audio-output.wav'
MAC_DEVICE_INDEX = 1
# device_index はマイク設定のため残す
def record_audio(duration: int = 10, device_index: int = 1) -> str:
    """
    10秒間の音声を録音し、'python-audio-output.wav'に保存する。

    Args:
        duration: 録音する時間（秒）。デフォルトは10秒。
        device_index: 使用するmacOSのオーディオデバイスインデックス。

    Returns:
        保存された音声ファイルの絶対パス (str)。
    """
    output_path = FIXED_OUTPUT_FILE # <-- 関数内で固定値を使用
    device_input = f":{device_index}"
    
    try:
        # ディレクトリ作成（必要であれば）
        os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
        
        print(f"{duration}秒間、マイクデバイス {device_input} からの録音を開始します...")
        
        (
            ffmpeg
            .input(device_input, format='avfoundation', t=duration) 
            .output(output_path, acodec='pcm_s16le', ar='44100', ac=1)
            .run(overwrite_output=True, capture_stdout=True, capture_stderr=True)
        )
        
        print(f"録音が完了しました。{output_path}に保存されました。")
        
        # 【必須】作業者2が使用するために、ファイルの絶対パスを返す
        return os.path.abspath(output_path)

    except ffmpeg.Error as e:
        error_msg = e.stderr.decode('utf8', errors='ignore')
        print(f"🔴 エラーが発生しました。FFmpegログ:\n{error_msg}")
        raise 
        
    except Exception as e:
        print(f"🔴 予期せぬエラー: {e}")
        raise

if __name__ == "__main__":
    try:
        # 呼び出し時に、事前に決定した定数を使用
        final_path = record_audio(duration=10, device_index=MAC_DEVICE_INDEX)
        print(f"テスト実行結果: 録音ファイルパス {final_path}")
    except Exception:
        print("録音テストが失敗しました。上記のエラーメッセージを確認してください。")