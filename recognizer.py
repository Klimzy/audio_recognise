import json
import pyaudio
import os

from vosk import Model, KaldiRecognizer
from pydub import AudioSegment



FRAME_RATE = 16000
CHANNELS = 1



model = Model('vosk-model-small-ru-0.4')
rec = KaldiRecognizer(model, FRAME_RATE)


def get_path():
    try:
        path = os.path.abspath(input('Enter path to file:'))
    except:
        print('Error with getting path')
    return path


def write_in_file(text):
    file = open('output.txt', 'w')

    try:
        file.write(text)
        file.close()
    except:
        print('Ошибка записи в файл')



while True:
    path = get_path()

    print('starting recognise')
    wav = AudioSegment.from_wav(path)
    wav = wav.set_channels(CHANNELS)
    wav = wav.set_frame_rate(FRAME_RATE)


    rec.AcceptWaveform(wav.raw_data)
    result = rec.Result()

    text = json.loads(result)['text']
    print(text)



