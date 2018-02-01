from bleeps import Bleeps
from KlassiKrypto import Morse
import datetime

class MorseStation:
    # preamble True enable the internal preable
    def __init__(self, frequency=1000, wpm=18, timeunit=1.2, volume=1, preamble=False, spacing=5):
        self.timeunit = timeunit
        self.wpm = wpm
        self.frequency = frequency
        self.volume = volume
        self.preamble = preamble
        self.spacing = spacing

    def farnsworth2_1(self):
        unit = float(self.timeunit / self.wpm)
        dot_wait = unit * 1000
        dash_wait = (unit * 3) * 1000
        element_wait = (unit * 1000)
        letter_wait = (unit * 3) * 1000
        word_wait= (unit * 12) * 1000
        return dot_wait, dash_wait, element_wait, letter_wait, word_wait

    # Create a Morse code WAV file 
    # Accepts A-Z 0-9 as input
    # preamble and eot (end of transmission are used if one wants and always overrides the internal preamble
    def transmit(self, data, filename, preamble="", eot="", msgnumber=0, station=""):
        if self.preamble == True and preamble == "" and eot == "":
           if msgnumber != 0:
               msgn = str(msgnumber)
           else:
               msgn = ""
           preamble = station + "MSG" + msgn + "CK" + str(len(data)) + "CK" + datetime.datetime.now().strftime('%Y%M%d%H%M') + "BT"
           eot = "000"

        code = Morse().encode(preamble+data+eot)
        bleeps = Bleeps()
        letters = code.split()
        dot_wait, dash_wait, element_wait, letter_wait, word_wait = self.farnsworth2_1()
        count = 0
        for c, letter in enumerate(letters):
            count += 1
            for element in letter:
                if element == ".":
                    bleeps.append_sinewave(freq=self.frequency,duration_milliseconds=dot_wait,volume=self.volume)
                elif element == "-":
                    bleeps.append_sinewave(freq=self.frequency,duration_milliseconds=dash_wait,volume=self.volume)
                bleeps.append_silence(duration_milliseconds=element_wait)
            if (count == self.spacing) and self.spacing != 0 and self.spacing != 1:
                bleeps.append_silence(duration_milliseconds=word_wait)
                count = 0
            else:
                bleeps.append_silence(duration_milliseconds=letter_wait)
        bleeps.save_wave(filename)
