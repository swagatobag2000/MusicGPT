def map_lines_to_music(midi_data, aligned_lyrics):
    mapped = []
    for line in aligned_lyrics:
        start, end = line["start"], line["end"]
        notes = []
        for stem, note_events in midi_data.items():
            for note in note_events:
                if start <= note["start"] <= end:
                    notes.append(note["pitch"])
        mapped.append({
            "lyric": line["lyric"],
            "notes": notes,
            "chords": ["Am", "F", "C"],  # Placeholder
        })
    return mapped
