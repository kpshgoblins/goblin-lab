import openai

openai.api_key="{key}"


def transcript(audio_path):
    audio_file = open(audio_path, "rb")
    # todo audio segmentation
    text = openai.Audio.transcribe("whisper-1", audio_file)
    print(text)
