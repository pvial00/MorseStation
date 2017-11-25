from bleeps import Bleeps
from KlassiKrypto import Morse

class MorseStation:
    def __init__(self, frequency=1000, timeunit=60, volume=1):
        self.frequency = frequency
        self.short_duration = timeunit
        self.long_duration = timeunit * 3
        self.wait_duration = timeunit
        self.letter_wait_duration = (timeunit * 3) - timeunit
        self.volume = volume

    def transmit(self, data, filename):
        code = Morse().encode(data)
        bleeps = Bleeps()
        letters = code.strip(',')
        for letter in letters:
            for element in letter:
                if element == ".":
                    bleeps.append_sinewave(freq=self.frequency,duration_milliseconds=self.short_duration,volume=self.volume)
                    bleeps.append_silence(duration_milliseconds=self.wait_duration)
                elif element == "-":
                    bleeps.append_sinewave(freq=self.frequency,duration_milliseconds=self.long_duration,volume=self.volume)
                bleeps.append_silence(duration_milliseconds=self.wait_duration)
            bleeps.append_silence(duration_milliseconds=self.letter_wait_duration)
        bleeps.save_wave(filename)
