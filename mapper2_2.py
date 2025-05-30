lineas = open("Dataset2.csv", encoding="utf-8").read().splitlines()

# ¿Cuál es el alimento con mayor cantidad de vitamina C?

listaAEntregar = []

for linea in lineas:
    lineaATrabajar = linea.split(";")
    nombreAlimento = lineaATrabajar[0].strip()
    vitaminaCAlimento = lineaATrabajar[10]

    if vitaminaCAlimento == "-":
        vitaminaCAlimento = "0"

    mensaje = [nombreAlimento, vitaminaCAlimento]
    listaAEntregar.append(mensaje)

mensajeFinal = ""
for mensaje in listaAEntregar:
    mensajeFinal += str(mensaje[0]) + ";" + str(mensaje[1]) + "\n"

archivoAEntregar = open("resultado_mapper2_2.csv", "w", encoding="utf-8")
archivoAEntregar.write(mensajeFinal[:-1])
archivoAEntregar.close()