# ai-task3
# Voice-to-Voice AI Assistant

## Overview

This project is a Voice-to-Voice AI Assistant that allows the user to interact with an artificial intelligence model using voice input and voice output.

The system works through three main steps:

1. Recording the user's voice from the microphone.
2. Converting the recorded speech into text.
3. Sending the text to an AI language model and converting the response back into speech.

## Project Structure

Voice-to-Voice-AI-Assistant/

├── main.py
├── speech_to_text.py
├── llm.py
├── text_to_speech.py
├── input.wav
├── requirements.txt
└── README.md


## Requirements

The project requires:

- Python 3.10 or newer
- Microphone
- Internet connection
- API key for the AI model


## Installation

Create a virtual environment:

python -m venv venv


Activate the virtual environment:

Windows:

venv\Scripts\activate


Install required packages:

pip install -r requirements.txt


## Configuration

Create a file named:

.env

Add your API key inside the file:

API_KEY=your_api_key_here


## Microphone Setup

The assistant uses the computer microphone to record audio.

To view available audio devices, run:

python

Then:

import sounddevice as sd

sd.query_devices()


Choose the correct microphone device and update the device number in main.py if needed.

Example:

device=13


## Running the Assistant

Start the application:

python main.py


The program will:

1. Record audio from the microphone.
2. Save the audio as input.wav.
3. Convert speech into text.
4. Send the text to the AI model.
5. Convert the AI response into speech.


## Features

- Voice input through microphone.
- Speech-to-text conversion.
- AI response generation.
- Text-to-speech output.
- Continuous voice interaction.
- Support for exit commands.


## Exit Commands

The assistant can be stopped by saying:

exit

quit

stop


## Troubleshooting

### Microphone Error

If you see:

Error opening InputStream: Invalid device


Check available devices:

import sounddevice as sd

sd.query_devices()


Then update the microphone device number in main.py.


### No Audio Input

Make sure:

- The microphone is connected.
- Windows microphone permissions are enabled.
- The correct input device is selected.


### Python Environment Error

Make sure the virtual environment is activated before running the project.

The terminal should show:

(venv)


## Future Improvements

Possible improvements:

- Real-time voice streaming.
- Wake word detection.
- Multiple language support.
- ROS robot integration.
- Noise reduction.
- Faster speech processing.


## License

This project is created for educational and development purposes.
