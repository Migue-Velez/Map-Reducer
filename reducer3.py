archivo1 = open("resultado_mapper3_1.csv", encoding="utf-8").read()
archivo2 = open("resultado_mapper3_2.csv", encoding="utf-8").read()

archivoCompleto = archivo1 + "\n" + archivo2

lineas = archivoCompleto.splitlines()
# ¿Cuántos alimentos tienen más de 0.1 gramos de tiamina?
listaAlimentos = []
mensajeFinal = "null "
for linea in lineas:
    mensaje = linea.split(";")
    cantidadTiamina = float(mensaje[1])

    # Debemos comparar con una cantidad mayor o igual a 100 ya que los datos porporcionados están en miligramos y nos preguntar por los que tienen 0.1 gramos.
    # 0.1 gramos = 100 miligramos
    if cantidadTiamina > 100:
        if mensajeFinal == "null":
            mensajeFinal = mensaje[0] + ";" + str(cantidadTiamina) + "\n"
        else:
            mensajeFinal += mensaje[0] + ";" + str(cantidadTiamina) + "\n"

#print("El/los alimentos con más tiamina (vitamina B1) es/son:\n" +  mensajeFinal)
resultadoFinal = open("resultado_reducer3.txt", "w", encoding="utf-8")
resultadoFinal.write(mensajeFinal[:-1])
resultadoFinal.close()