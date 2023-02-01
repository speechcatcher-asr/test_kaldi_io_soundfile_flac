import kaldiio
import numpy as np
from io import BytesIO
import soundfile
import argparse

def process(input_file, output_file, audio_format = '.flac', samplerate='16000'):
    audio_format = 'flac'

    wavpath = f'ffmpeg -i "{input_file}" -acodec pcm_s16le -ar {samplerate} -ac 1 -f wav - |'

    #uttid, wavpath = line.strip().split(None, 1)

    with kaldiio.open_like_kaldi(wavpath, "rb") as f:
        with BytesIO(f.read()) as g:
            wave, rate = soundfile.read(g, dtype=np.int16)

    assert(wave.ndim == 1)
    
    if output_file == '':
        output_file = input_file + audio_format

    if not output_file.endswith(audio_format):
        output_file += audio_format

    soundfile.write(output_file, wave, samplerate=rate)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='us (XML) into text transcriptions for KALDI')
    parser.add_argument('-i', '--input_file', dest='input_file', help='input file or url', type=str, required=True)
    parser.add_argument('-o', '--output_file', dest='output_file', help='output file', type=str, default='')
    parser.add_argument('-a', '--audio_format', dest='audio_format', help='output file', type=str, default='.flac')
    parser.add_argument('-s', '--samplerate', dest='samplerate', type=str, default='16000')

    args = parser.parse_args()

    process(args.input_file, args.output_file, args.audio_format, args.samplerate)
