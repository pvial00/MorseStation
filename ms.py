from morse_station import MorseStation

data = input("Enter text to transmit: ")
filename = input("Enter output filename: ")
MorseStation().transmit(data, filename)
