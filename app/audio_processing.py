import subprocess
import os

def separate_instruments(audio_path):
    out_dir = "data/separated"
    os.makedirs(out_dir, exist_ok=True)
    command = f"demucs --two-stems=vocals \"{audio_path}\" -o {out_dir}"
    subprocess.run(command, shell=True)
    return os.path.join(out_dir, "htdemucs", os.path.basename(audio_path).replace(".mp3", ""))
