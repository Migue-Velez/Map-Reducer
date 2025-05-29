lineas = open("Dataset.csv", encoding="utf-8").read().splitlines()

# ¿Cuál es el alimento con mayor cantidad de grasas?
listaAEntregar = []
for linea in lineas:
    lineaATrabajar = linea.split(";")
    nombreAlimento = lineaATrabajar[0].strip()
    grasaAlimento = lineaATrabajar[3].replace(",", ".")

    if grasaAlimento == "-":
        grasaAlimento = "0"

    mensaje = [nombreAlimento, grasaAlimento]
    listaAEntregar.append(mensaje)

mensajeFinal = ""
for mensaje in listaAEntregar:
    mensajeFinal += str(mensaje[0]) + ";" + str(mensaje[1]) + "\n"

archivoAEntregar = open("resultado_mapper1.csv", "w", encoding="utf-8")
archivoAEntregar.write(mensajeFinal[:-1])
archivoAEntregar.close()
