lineas = open("resultado_mapper1.csv", encoding="utf-8").read().splitlines()

# ¿Cuál es el alimento con mayor cantidad de grasas?
grasasMasAlto = 0
for linea in lineas:
    mensaje = linea.split(";")
    cantidadGrasas = float(mensaje[1])

    if cantidadGrasas > grasasMasAlto:
        grasasMasAlto = cantidadGrasas

mensajeFinal = ""
listaAlimentos = []
for linea in lineas:
    mensaje = linea.split(";")
    
    if float(mensaje[1]) == grasasMasAlto:
        alimentoConMasGrasas = mensaje[0]
        mensajeFinal += alimentoConMasGrasas + ";" + str(grasasMasAlto) + "\n"

resultadoFinal = open("resultado_reducer1.txt", "w", encoding="utf-8")
resultadoFinal.write(mensajeFinal[:-1])
resultadoFinal.close()