import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def explain_music(music_line):
    prompt = f"""
Lyric Line: "{music_line['lyric']}"
Chords: {music_line['chords']}
Notes: {music_line['notes']}

Explain the mood, emotion, and structure of the line in musical terms.
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"LLM error: {e}"
