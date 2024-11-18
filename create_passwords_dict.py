import math

while True:
    try:
        inicio = int(input('''Insert start number: ej. 20000000
> '''))
        fin = int(input('''Insert end number: ej. 40000000
> '''))
        if fin > inicio:
            break
        else:
            print("Error: The start number most be upper than end")
    except:
        print("Error: must insert numbers")

prefijo = input('''Insert pre value (optional)
> ''')
post = input('''Insert post value (optional)
> ''')

# Size of bloque wich will write in file. Write up 100000 numbers at time in orden to avoid RAM memory or system collapse
tamano_bloque = 100000

extension = fin - inicio +1

bloques = []
if (extension >= tamano_bloque):
    num_bloques = math.floor(extension / tamano_bloque)
    for block in range(num_bloques):
        bloques.append(tamano_bloque)
    bloques_restantes = extension%tamano_bloque
    if bloques_restantes:
        bloques.append(bloques_restantes)
else:
    bloques = [extension,]

print(f'Generating {len(bloques)} of passwords...')

with open("passwords.lst", "w") as archivo:
    for block in bloques:
        data = ""
        for _ in range(block):
            data += f"{prefijo}{inicio}{post}\n"
            inicio +=1
        archivo.write(data)

        porcentaje = (inicio / fin) * 100
        print(f"Progress: {porcentaje:.2f}% done", end='\r')

print("Archivo 'passwords.lst' created successfully.")
