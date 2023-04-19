"""Escribe un bucle para que itere sobre una la lista de nombres para crear una lista de nombres de usuario. 
Para crear un nombre de usuario para cada nombre, convierta todas las letras en minúsculas y reemplaza los espacios por 
guiones bajos.

nombres = ["Sheldon Cooper", "Leonard Hofstadter", "Howard Wolowitz", "Rajesh Koothrappali"]

debería crear la lista:

nombres_de_usuario = ["sheldon_cooper", "leonard_hofstadter", "howard_wolowitz", "Rajesh_koothrappali"]

SUGERENCIA: Utiliza el método.replace() para reemplazar los espacios con guiones bajos. Busque cómo usar este método en internet,
 sino lo encuentra abra o continúe el hilo del foro para este concepto, quizá los compañeros puedan ayudar.
"""

nombres = ["Sheldon Cooper", "Leonard Hofstadter", "Howard Wolowitz", "Rajesh Koothrappali"]
nombres_de_usuario=[]
for nom in nombres:
    user = nom.lower()
    user = user.replace(" ","_")
    nombres_de_usuario.append(user)
    print (nombres_de_usuario)