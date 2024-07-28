# SpeechScribe - Automatic Speech Recognition (ASR) System using Whisper from OpenAI

This repository contains a Python project for implementing an Automatic Speech Recognition (ASR) system using Whisper from OpenAI, directly adapted from a Hugging Face Space. The project demonstrates how to leverage Whisper's advanced capabilities to transcribe spoken language into text accurately and efficiently.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Automatic Speech Recognition (ASR) systems convert spoken language into written text, enabling applications such as voice assistants, transcription services, and more. This project utilizes Whisper from OpenAI, a state-of-the-art ASR model known for its high accuracy and robustness across various languages and accents. The code in this repository is directly taken from a Hugging Face Space and utilizes the Gradio library for creating a user-friendly web interface.

## Features
- Loading and setting up the Whisper ASR model
- Processing audio files for transcription
- Generating and saving transcriptions
- Support for microphone input and audio file upload
- User-friendly interface using Gradio

## Installation
To run this project, you need to have the following dependencies installed:

- Python 3.x
- Transformers (Hugging Face)
- Gradio
- Torch

You can install the required packages using `pip`:
```bash
pip install transformers gradio torch
```

## Usage
1. Clone the repository:
```bash
git clone https://github.com/saadtariq001s/asr-whisper.git
cd asr-whisper
```

2. Run the ASR system:
```bash
python app.py
```

3. Open your browser and go to the provided Gradio link to interact with the ASR system. You can either speak into the microphone or upload an audio file to get the transcription.

## Results
The ASR system generates accurate transcriptions for various types of audio inputs. You can evaluate the performance by comparing the transcriptions with the original spoken content.

Check out the demo on my LinkedIn: https://www.linkedin.com/posts/muhammad-saad-tariq-103272233_huggingface-gradio-ai-activity-7193691415510474752-_311?utm_source=share&utm_medium=member_desktop

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
