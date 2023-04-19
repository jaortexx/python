from io import open

fichero = open('equipo.txt','r', encoding="utf8")
lineas = fichero.readlines()
fichero.close()

personas = []
for linea in lineas:
    # Borramos los saltos de línea y separamos
    campos = linea.replace("\n", "").split(";")  
    # print(campos[1])
    persona = {"id":campos[0], "nombre":campos[1],"apellido":campos[2], "nacimiento":campos[3]}
    personas.append(persona)

for p in personas:
    #print (p)
    print(f"(id={p['id']}) {p['nombre']} {p['apellido']} => {p['nacimiento']} " )
