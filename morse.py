class Morse:
    morse = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
    numbers = ['-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']
    morse.extend(numbers)
    alphabet = []
    for x in range(65, 91):
        alphabet.append(chr(x))
    for x in range(48, 58):
        alphabet.append(chr(x))

    def encode(self, data, delimiter=' '):
        buf = ""
        datalen = len(data)
        for c, letter in enumerate(data):
            buf += self.morse[self.alphabet.index(letter)]
            if c != datalen - 1:
                buf += delimiter
        return buf

    def decode(self, data, delimiter=' '):
        buf = ""
        for letter in data.split(delimiter):
            buf += self.alphabet[self.morse.index(letter)]
        return buf
