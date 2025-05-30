lineas = open("Dataset2.csv", encoding="utf-8").read().splitlines()

mensajeFinal = ""
# ¿Cuáles alimentos aportan más de 1 mg de hierro y menos de 3 g de grasas?
for linea in lineas:
    lineaATrabajar = linea.split(";")
    nombreAlimento = lineaATrabajar[0].strip()
    mensajeFinal += f"{nombreAlimento};"
    
    if lineaATrabajar[3] == "-":
        mensajeFinal += "0;"
    else:
        grasasAlimento = lineaATrabajar[3].replace(",",".")
        mensajeFinal += f"{grasasAlimento};"

    if lineaATrabajar[5] == "-":
            mensajeFinal += "0"
    else:
        hierroAlimento = lineaATrabajar[5].replace(",",".")
        mensajeFinal += f"{hierroAlimento}\n"

archivoAEntregar = open("resultado_mapper5_2.csv", "w", encoding="utf-8")
archivoAEntregar.write(mensajeFinal[:-1])
archivoAEntregar.close()