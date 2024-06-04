# LLM-VoiceSynthesizer

## Initial Goal 

Develop a Python program to automatically transcribe all segmented audio files using a text-to-speech API, simply said an Audio-2-Text Bot.

## Initial Strategic Plan

1. Automate Project Creation:
    - Research and integrate the ElevenLabs Python SDK to automate the creation of a new project for each video.

2. Configure Project Settings:
    - Develop a configuration module that sets project-specific parameters such as model version (v2), quality (high), and voice selection based on user input or predefined settings.

3. Automate Chapter Creation:
    - Implement a function that automatically creates a new chapter in the ElevenLabs project for each segmented audio file, associating each chapter with its corresponding segment ID or name.

5. Transcript Integration:
    - Create a script to upload and attach translated transcripts to their respective chapters without altering the preset voice settings.

6. Convert Text to Speech:
    - Develop functionality to convert the text in each chapter to speech, ensuring the output is a separate audio file for each segment and language.
    - Integrate error handling to manage failures in text-to-speech conversion processes, ensuring robust operation.

7. Cost Management:
    - Program a budget tracker to estimate and record the cost of conversions based on the length of audio and the rate of 9 euros per hour, including alerts for budget overruns.

## Project Architecture

The project will use a layered architecture that separates the logic for interfacing with the ElevenLabs API, managing data, and running the automation scripts.

1. Data Model Layer:

 - Handles data structures and storage, interfacing directly with the database if needed, or managing in-memory data structures.

2. Service Layer:

- Contains business logic and service integration logic.
- Communicates with external APIs (like ElevenLabs) and handles data transformation.

3. Controller/Scripting Layer:

- Orchestrates the execution of tasks in the service layer.
- Handles sequencing of operations and ensures correct data flow between tasks.

4. Configuration/Environment Layer:

- Manages configuration settings such as API keys, project settings, and environment-specific variables.

### Source File Architecture

Here’s how the source files might be organized along with their main functions:

1. config.py

    - Purpose: Manages all configuration-related settings such as API keys, service URLs, and any other configurable parameters.
    - Main Functions:
        - Load and parse configuration settings from environment variables or configuration files.

2. elevenlabs_api_client.py

    - Purpose: Interfaces with the ElevenLabs API to create projects, chapters, and handle audio conversions.
    - Main Functions:
        - create_project(title, model, quality, voice): Creates a new project with specified settings.
        - add_chapter_to_project(project_id, chapter_name, transcript): Adds a chapter with the given transcript to a project.
        - convert_text_to_speech(chapter_id): Converts the chapter's text to speech.

3. transcript_manager.py

    - Purpose: Manages the uploading and formatting of transcripts.
    - Main Functions:
        - format_transcript(raw_transcript): Formats raw transcripts to meet ElevenLabs specifications.
        - upload_transcript(project_id, chapter_id, transcript): Uploads and attaches a transcript to a chapter in a project.

4. cost_estimator.py

    - Purpose: Manages cost estimation and tracking for the audio conversion process.
    - Main Functions:
        - estimate_conversion_cost(duration): Estimates the cost based on the audio duration.
        - track_budget(estimated_costs): Tracks and records costs, providing alerts for budget overruns.

5. main.py

    - Purpose: Entry point for running the automation scripts.
    - Main Functions:
       - run_automation_sequence(video_details): Orchestrates the full process from project creation, transcript uploading, chapter creation, to audio conversion.


