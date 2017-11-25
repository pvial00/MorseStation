from MorseStation import MorseStation

data = raw_input("Enter text to transmit: ")
filename = raw_input("Enter output filename: ")
MorseStation().transmit(data, filename)
