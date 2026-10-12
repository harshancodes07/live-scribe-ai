
import sounddevice as sd
import soundfile as sf

DEVICE_ID = 2
SAMPLE_RATE = 44100
CHANNELS = 2
OUTPUT_FILE = "system_audio_test.wav"

print("Recording system audio...")
print("Press ENTER to stop recording.")

with sf.SoundFile(
    OUTPUT_FILE,
    mode="w",
    samplerate=SAMPLE_RATE,
    channels=CHANNELS,
) as audio_file:

    def callback(indata, frames, time, status):
        if status:
            print(status)
        audio_file.write(indata)

    with sd.InputStream(
        device=DEVICE_ID,
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="float32",
        callback=callback,
    ):
        input()

print(f"Recording saved to {OUTPUT_FILE}")
