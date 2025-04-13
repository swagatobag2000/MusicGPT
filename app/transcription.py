from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH
import os

def transcribe_audio(audio_folder):
    from glob import glob
    wavs = glob(os.path.join(audio_folder, "*.wav"))
    midi_data = {}
    for wav in wavs:
        print(f"Transcribing {wav}")
        model_output, midi, note_events = predict(wav, model_path=ICASSP_2022_MODEL_PATH)
        midi_data[os.path.basename(wav)] = note_events
    return midi_data
