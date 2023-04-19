ph_level = int(input('Enter a pH level (0-14): '))

print(ph_level)

if ph_level > 7:
    print("Basic")
elif ph_level < 7:
    print("Acid")
else:
    print("Neutral")