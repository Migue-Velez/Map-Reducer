lineas = open("Dataset.csv", encoding="utf-8").read().splitlines()

# ¿Cuántos alimentos tienen más de 0.1 gramos de tiamina?
listaAEntregar = []

for linea in lineas:
    lineaATrabajar = linea.split(";")
    nombreAlimento = lineaATrabajar[0].strip()
    tiaminaAlimento = lineaATrabajar[7].replace(",", ".")

    if tiaminaAlimento == "-":
        tiaminaAlimento = "0"

    mensaje = [nombreAlimento, tiaminaAlimento]
    listaAEntregar.append(mensaje)

mensajeFinal = ""
for mensaje in listaAEntregar:
    mensajeFinal += str(mensaje[0]) + ";" + str(mensaje[1]) + "\n"

archivoAEntregar = open("resultado_mapper3.csv", "w", encoding="utf-8")
archivoAEntregar.write(mensajeFinal[:-1])
archivoAEntregar.close()
