archivo1 = open("resultado_mapper2_1.csv", encoding="utf-8").read()
archivo2 = open("resultado_mapper2_2.csv", encoding="utf-8").read()

archivoCompleto = archivo1 + "\n" + archivo2

lineas = archivoCompleto.splitlines()
# ¿Cuál es el alimento con mayor cantidad de vitamina C?
VitaminaCMasAlto = 0
for linea in lineas:
    mensaje = linea.split(";")
    cantidadVicaminaC = int(mensaje[1])

    if cantidadVicaminaC > VitaminaCMasAlto:
        VitaminaCMasAlto = cantidadVicaminaC

mensajeFinal = ""
for linea in lineas:
    mensaje = linea.split(";")
    
    if int(mensaje[1]) == VitaminaCMasAlto:
        alimentoConMasGrasas = mensaje[0]
        mensajeFinal += alimentoConMasGrasas + ";" + str(VitaminaCMasAlto) + "\n"

resultadoFinal = open("resultado_reducer2.txt", "w", encoding="utf-8")
resultadoFinal.write(mensajeFinal[:-1])
resultadoFinal.close()