# LLM-VoiceSynthesizer

## Initial Goal 

Develop a Python program to automatically transcribe all segmented audio files using a text-to-speech API, simply said an audio-2-audio Bot with translation in between.

## Initial Strategic Plan

- write a single file called `playground.py` for quick MVP, though constant will be placed in `config.py`
- encapsulate atomic process  using simple functions
- will use `LLM-Translator` and `LLM-Scribe` if needed
- use folder `projects` to centralize all file produced
    - `/projects/project-name/audios/`: initial audio to translate
    - `/projects/project-name/transcripts/`: corresponding transcripts 
    - `/projects/project-name/translations/`: corresponding translations 
    - `/projects/project-name/outputs/`: audios produced with 11labs api 

