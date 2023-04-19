guess = 0
tries = 0

while guess != 6:
  guess = int(input("Guess the number:  "))
  tries += 1
  if tries == 4 and guess == 6:
    print("You got it!")
  elif tries == 4:
    print("Número de intentos máximos alcanzado")
    break
 
