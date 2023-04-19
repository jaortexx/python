import math

try:
    numero = int(input("Introduzca un número natural: "))
except:
        print("Ese numero no es natural")
else:
    if numero < 0:
        print("Ese numero no es natural")
    elif numero == float :
        print("Ese numero no es natural")

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

print(is_prime(numero)) 

