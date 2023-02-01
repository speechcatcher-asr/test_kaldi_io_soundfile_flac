# test_kaldi_io_soundfile_flac

Tests kaldiio + writing out a flac

Create a virtual environment:

    virtualenv -p python3.10 test_env

Activate it:

    source test_env/bin/activate

Install requirements:

    pip3 install -r requirements.txt

Run the test:

    python3 test_soundfile_flac.py -i https://someurl/test.mp3 -o test10.flac
