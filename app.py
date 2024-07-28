from transformers import pipeline

asr = pipeline(task="automatic-speech-recognition",
               model= "distil-whisper/distil-small.en")

import gradio as gr
demo = gr.Blocks()

def transcribe_long_form(filepath):
    if filepath is None:
        gr.Warning("No audio found, please retry")
        return
    output = asr(filepath,
                 max_new_tokens=256,
                 chunk_length_s=30,
                 batch_size=4,)
    return output['text']

mic_transcribe = gr.Interface(
    fn=transcribe_long_form,
    inputs=gr.Audio(sources="microphone",
                    type="filepath"),
    outputs=gr.Textbox(label="Transcription",
                       lines=7),
    allow_flagging="never",
    description="Speak into the microphone or upload an audio file to transcribe it into text. This model uses a state-of-the-art speech recognition algorithm to recognize spoken words and phrases")

file_transcribe = gr.Interface(
    fn=transcribe_long_form,
    inputs=gr.Audio(sources="upload",
                    type="filepath"),
    outputs=gr.Textbox(label="Transcription",
                       lines=7),
    allow_flagging="never",
    description="Speak into the microphone or upload an audio file to transcribe it into text. This model uses a state-of-the-art speech recognition algorithm to recognize spoken words and phrases")



with demo:
    gr.TabbedInterface(
        [mic_transcribe,
         file_transcribe],
        ["Transcribe Microphone",
         "Transcribe Audio File"],
        title="SpeechScribe - Automatic Speech Recognition"
    )
demo.launch()