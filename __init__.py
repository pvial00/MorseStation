from bleeps import Bleeps
from KlassiKrypto import Morse
import datetime

class MorseStation:
    def __init__(self, frequency=1000, wpm=18, timeunit=1.2, volume=1, preamble=True):
        self.timeunit = timeunit
        self.wpm = wpm
        self.frequency = frequency
        self.volume = volume
        self.preamble = preamble

    def farnsworth2_1(self):
        unit = float(self.timeunit / self.wpm)
        dot_wait = unit * 1000
        dash_wait = (unit * 3) * 1000
        element_wait = (unit * 1000)
        letter_wait = (unit * 3) * 1000
        word_wait= ((unit * 7) - (unit * 3)) * 1000
        return dot_wait, dash_wait, element_wait, letter_wait, word_wait

    def transmit(self, data, filename, preamble="", eot="", msgnumber=0, station=""):
        if self.preamble == True:
            if preamble == "":
               if msgnumber != 0:
                   msgn = str(msgn)
               else:
                   msgn = ""
               pre = station + "MSG" + msgn + "CK" + str(len(data)) + "CK" + datetime.datetime.now().strftime('%Y%M%d%H%M') + "BT"
            if eot == "":
               eot = "000"
        else:
            pre = ""
            eot = ""
        code = Morse().encode(pre+data+eot)
        bleeps = Bleeps()
        letters = code.split()
        dot_wait, dash_wait, element_wait, letter_wait, word_wait = self.farnsworth2_1()
        for c, letter in enumerate(letters):
            for element in letter:
                if element == ".":
                    bleeps.append_sinewave(freq=self.frequency,duration_milliseconds=dot_wait,volume=self.volume)
                elif element == "-":
                    bleeps.append_sinewave(freq=self.frequency,duration_milliseconds=dash_wait,volume=self.volume)
                bleeps.append_silence(duration_milliseconds=element_wait)
            if c % 5 == 0:
                bleeps.append_silence(duration_milliseconds=word_wait)
            else:
                bleeps.append_silence(duration_milliseconds=letter_wait)
        bleeps.save_wave(filename)
