
# Voice ChatGPT

Creating the "VoiceChat GPT" project involved leveraging the combined power of Bluetooth communication, Python programming, and Raspberry Pi hardware to build a sophisticated and conservative conversational AI device with voice interaction and speaker output.

# Hardware Setup

Raspberry Pi: A Raspberry Pi serves as the brain of the "VoiceChat GPT" device. It runs the Python-based AI application, handles user input, processes the AI responses, and manages the Bluetooth communication with the monospeaker.

Monospeaker: The monospeaker, paired with the Raspberry Pi via Bluetooth, functions as both the audio input and output device. Users interact with the "VoiceChat GPT" device by speaking their questions to the monospeaker, which captures the audio and sends it to the Raspberry Pi for processing.

## Work Flow
First User inut is captured via BT monospeaker

After capturing the user's voice input and converting it to text, the text is sent for processing using an unofficial API to interact with ChatGPT. This custom API allows the "VoiceChat GPT" device to leverage the power of ChatGPT's language model capabilities. The unofficial API takes the user's text query as input and sends it to ChatGPT, where the language model processes the text and generates a response.

Once ChatGPT's response is obtained as a text string from the unofficial API, the "VoiceChat GPT" device proceeds to convert this text response into audible speech using a Text-to-Speech (TTS) engine. The TTS-generated speech is then transmitted via Bluetooth to the monospeaker, where it is played back for the user to hear.

## Chat GPT API

https://github.com/acheong08/ChatGPT-lite.git


## Demo

![pic](https://github.com/rayy2002/VoiceChat-GPT/assets/88958861/929c1cc8-5bc1-4867-9504-f47e84089e8d)

https://github.com/rayy2002/VoiceChat-GPT/assets/88958861/7a238c68-a68d-46d0-b115-9b6fd1800c57


