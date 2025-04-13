import json
import os

def align_lyrics(audio_path, lyrics_path):
    # Dummy output for now — replace with Aeneas forced aligner
    with open(lyrics_path, "r") as f:
        lines = f.read().strip().split("\n")

    # Fake timestamps for prototype
    aligned = []
    for i, line in enumerate(lines):
        aligned.append({
            "line_id": i,
            "lyric": line,
            "start": i * 3.0,
            "end": (i + 1) * 3.0
        })
    return aligned
