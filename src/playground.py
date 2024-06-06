import os
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
ELVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
CHUNK_SIZE = 1024

# Voice Character
voice_ids = {
    "Rogzy": "RmicS1jU3ei6Vxlpkqj4",
    "Giacomo": "gFpPxLJAJCez7afCJ8Pd",
    "David St-onge": "0PfKe742JfrBvOr7Gyx9",
    "Fanis": "HIRH46f2SFLDptj86kJG",
    "Loic": "hOYgbRZsrkPHWJ2kdEIu",
    "Mogenet": "ld8UrJoCOHSibD1DlYXB",
    "Pantamis": "naFOP0Eb03OaLMVhdCxd",
    "Renaud": "UVJB9VPhLrNHNsH4ZatL",
    "es-question": "5K2SjAdgoClKG1acJ17G",
    "en-question": "ER8xHNz0kNywE1Pc5ogG"
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

print("\nAvailable Project Folders:")
for i, folder in enumerate(project_folders):
    print(f"{i+1}. {folder}")

folder_index = int(input("Enter the number to select a project folder: ")) - 1
selected_folder = project_folders[folder_index]

# Define base path
input_folder = project_path / selected_folder

# Function to process text to speech
def process_text_to_speech(text_file):
    text_to_speak = text_file.read_text()
    output_path = text_file.with_suffix(".mp3")

    # URL and headers for TTS API request
    tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"
    headers = {
        "Accept": "application/json",
        "xi-api-key": ELVENLABS_API_KEY
    }
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

    # Make the API request
    response = requests.post(tts_url, headers=headers, json=data, stream=True)
    if response.ok:
        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                f.write(chunk)
        print(f"Audio stream saved successfully to {output_path}")
    else:
        print(response.text)

# Process each text file in the folder and all subfolders
file_patterns = ["*_transcript_English.txt", "*_transcript_Spanish.txt"]
for pattern in file_patterns:
    for text_file in input_folder.rglob(pattern):
        process_text_to_speech(text_file)

