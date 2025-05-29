lineas = open("Dataset.csv", encoding="utf-8").read().splitlines()

# ¿Cuál es el alimento que posee la mayor suma de vitaminas?
mensajeFinal = ""
for linea in lineas:
    lineaATrabajar = linea.split(";")
    nombreAlimento = lineaATrabajar[0].strip()
    mensajeFinal += f"{nombreAlimento}"

    for i in range (6,11):
        if i == 9:
            pass
        else:
            try:
                vitamina = lineaATrabajar[i].replace(",",".")
                mensajeFinal += f";{float(vitamina)}"
            except ValueError:
                mensajeFinal += ";0"
    mensajeFinal += "\n"

archivoAEntregar = open("resultado_mapper4.csv", "w", encoding="utf-8")
archivoAEntregar.write(mensajeFinal[:-1])
archivoAEntregar.close()