# Voice Assistant - Tony

This Python project is a voice-activated personal assistant that can perform various tasks such as telling the time, opening websites, telling jokes, and playing music. It uses voice commands to respond to user queries and execute actions.

## Features

- Responds to basic queries like name and age.
- Tells the current time.
- Opens popular websites like YouTube, Google, Spotify, and Gmail.
- Tells a random joke using the `pyjokes` library.
- Plays music from a specified folder.
- Gracefully exits upon receiving an "exit" command.

## Requirements

Before running the project, make sure you have the following dependencies installed:

- `pyttsx3` (Text-to-speech library)
- `SpeechRecognition` (For speech-to-text conversion)
- `PyAudio` (Required for `SpeechRecognition` to work with the microphone)
- `webbrowser` (For opening websites)
- `datetime` (For getting the current time)
- `pyjokes` (For fetching jokes)
- `os` (For interacting with the file system)

You can install the required libraries with the following commands:

```bash
pip install pyttsx3 SpeechRecognition pyjokes pyaudio
