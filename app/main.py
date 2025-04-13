from app.audio_processing import separate_instruments
from app.transcription import transcribe_audio
from app.lyrics_aligner import align_lyrics
from app.line_mapper import map_lines_to_music
from app.music_llm import explain_music

def main(audio_path, lyrics_path):
    print("Separating instruments...")
    stems = separate_instruments(audio_path)

    print("Transcribing audio...")
    midi_data = transcribe_audio(stems)

    print("Aligning lyrics...")
    aligned_lines = align_lyrics(audio_path, lyrics_path)

    print("Mapping notes/chords to lines...")
    music_lines = map_lines_to_music(midi_data, aligned_lines)

    print("Generating musical explanations...")
    for line in music_lines:
        explanation = explain_music(line)
        print(f"\n>> {line['lyric']}\n{explanation}\n")

if __name__ == "__main__":
    main("data/input/song.mp3", "data/input/lyrics.txt")
