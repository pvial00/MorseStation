#!/usr/bin/python 
# based on : www.daniweb.com/code/snippet263775.html
# and based on : https://stackoverflow.com/questions/33879523/python-how-can-i-generate-a-wav-file-with-beeps
import math
import wave
import struct

# Audio will contain a long list of samples (i.e. floating point numbers describing the
# waveform).  If you were working with a very long sound you'd want to stream this to
# disk instead of buffering it all in memory list this.  But most sounds will fit in 
# memory.
class Bleeps:
    def __init__(self, sample_rate=44100.0):
        self.audio = []
        self.sample_rate = sample_rate

    def append_silence(self, duration_milliseconds=500):
        """
        Adding silence is easy - we add zeros to the end of our array
        """
        num_samples = duration_milliseconds * (self.sample_rate / 1000.0)

        entry = []
        for x in range(int(num_samples)): 
            entry.append(0.0)
        self.audio.append(entry)


    def append_sinewave(self,
            freq=440.0, 
            duration_milliseconds=500, 
            volume=1.0):
        """
        The sine wave generated here is the standard beep.  If you want something
        more aggresive you could try a square or saw tooth waveform.   Though there
        are some rather complicated issues with making high quality square and
        sawtooth waves... which we won't address here :) 
        """ 

        num_samples = duration_milliseconds * (self.sample_rate / 1000.0)

        entry = []
        for x in range(int(num_samples)):
            entry.append((volume * math.sin(2 * math.pi * freq * ( x / self.sample_rate ))))
        self.audio.append(entry)
            #self.audio.append(entry.append((volume * math.sin(2 * math.pi * freq * ( x / self.sample_rate )))))

    def save_wave(self, file_name):
        # Open up a wav file
        wav_file=wave.open(file_name,"w")

        # wav params
        nchannels = 1

        sampwidth = 2

        # 44100 is the industry standard sample rate - CD quality.  If you need to
        # save on file size you can adjust it downwards. The stanard for low quality
        # is 8000 or 8kHz.
        nframes = len(self.audio)
        comptype = "NONE"
        compname = "not compressed"
        wav_file.setparams((nchannels, sampwidth, self.sample_rate, nframes, comptype, compname))

        # WAV files here are using short, 16 bit, signed integers for the 
        # sample size.  So we multiply the floating point data we have by 32767, the
        # maximum value for a short integer.  NOTE: It is theortically possible to
        # use the floating point -1.0 to 1.0 data directly in a WAV file but not
        # obvious how to do that using the wave module in python.
        for sample in self.audio:
            for entry in sample:
                wav_file.writeframes(struct.pack('h', int( entry * 32767.0 )))

        wav_file.close()
