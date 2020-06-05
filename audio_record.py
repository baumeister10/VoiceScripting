import sounddevice as sd
from scipy.io.wavfile import write


def recording_audio():
    print("recording...")
    fs = 44100
    seconds = 4

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    write('scriptCommand.wav', fs, myrecording)

if __name__ == "__main__":
    recording_audio()
