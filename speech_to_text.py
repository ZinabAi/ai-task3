import whisper
import os

# ضعِي هنا مسار ffmpeg.exe عندك
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg-2026-07-27-git-a757b708ae-full_build\bin"

model = whisper.load_model("base")

def speech_to_text(audio_file):
    result = model.transcribe(audio_file)
    return result["text"]