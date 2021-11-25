from pydub import AudioSegment

original = AudioSegment.from_wav('beat.wav')
print(type(original))
print(original)

reversed = original.reverse()
# reversed.export('reversed2.wav')
reversed = reversed + 15 # increases the volume

# print(dir(original))

first_two = original[0:2000]
# first_two.export('first_two.wav')

print(len(original))

merged = original + reversed
merged2 = original + AudioSegment.silent(1000) + reversed
# merged2.export("merged2.wav")
merged3 = original * 2 + AudioSegment.silent(1000) + reversed
# merged3.export('merged3.wav')