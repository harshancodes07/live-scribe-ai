from faster_whisper import WhisperModel

model = WhisperModel("tiny")

def transcribe_audio(audio_path):
    segments , info  = model.transcribe(audio_path)
    transcript = ""

    for segment in segments :
        transcript+= segment.text

    return transcript 
if __name__ == "__main__":
    result = transcribe_audio("test_audio.m4a")

    print("Transcrpit:", result )