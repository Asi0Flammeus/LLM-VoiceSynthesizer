import os
import requests
from pathlib import Path
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed

# Load environment variables
load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

if not ELEVENLABS_API_KEY:
    print("API key is not loaded correctly.")
    exit()

# Voice Character
voice_ids = {
    "Rogzy": "RmicS1jU3ei6Vxlpkqj4",

}


# List voices for user selection
print("Available Voices:")
for i, voice in enumerate(voice_ids.keys()):
    print(f"{i+1}. {voice}")

voice_index = int(input("Enter the number to select a voice: ")) - 1
voice_list = list(voice_ids.keys())
VOICE_ID = voice_ids[voice_list[voice_index]]

# List project folders
project_path = Path('./projects/')
project_folders = [f.name for f in project_path.iterdir() if f.is_dir()]

# Headers configuration
HEADERS = {
    "Accept": "application/json",
    "xi-api-key": ELEVENLABS_API_KEY,
    "Content-Type": "application/json"
}

# Define function for text-to-speech processing
def text_to_speech(text_file):
    text_to_speak = text_file.read_text()
    output_path = text_file.with_suffix(".mp3")
    tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"
    data = {
        "text": text_to_speak,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.8,
            "style": 0.0,
            "use_speaker_boost": True
        }
    }
    response = requests.post(tts_url, headers=HEADERS, json=data, stream=True)
    if response.ok:
        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f"Audio stream saved successfully to {output_path}")
    else:
        raise Exception(f"API Request Failed: {response.text}")

# Parallel execution across files in a selected folder
def run_parallel_text_to_speech(folder_path):
    file_patterns = ["*_transcript_English.txt", "*_transcript_Spanish.txt"]
    text_files = [text_file for pattern in file_patterns for text_file in folder_path.rglob(pattern)]
    with ThreadPoolExecutor(max_workers=len(project_folders)) as executor:
        futures = {executor.submit(text_to_speech, text_file): text_file for text_file in text_files}
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(e)

# Process each project folder in parallel
for folder in project_folders:
    folder_path = project_path / folder
    print(f"Processing folder: {folder}")
    run_parallel_text_to_speech(folder_path)

