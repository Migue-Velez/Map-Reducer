lineas = open("resultado_mapper4.csv", encoding="utf-8").read().splitlines()

# ¿Cuál es el alimento que posee la mayor suma de vitaminas?
# Lógica. Asumiremos que toda la vitamina A de estos alimentos provienen del retinol.
# 1 UI de vitamina A = 0.00003 miligramos
listaVitaminas = []
sumaCantidadVitaminas = 0
mayorCantidadVitaminas = 0
for linea in lineas:
    mensaje = linea.split(";")
    if sumaCantidadVitaminas > mayorCantidadVitaminas:
        mayorCantidadVitaminas = sumaCantidadVitaminas

    sumaCantidadVitaminas = 0

    for i in range(1,5):
        if i == 1:
            sumaCantidadVitaminas += float(mensaje[i])*0.00003
        else:
            sumaCantidadVitaminas += float(mensaje[i])
    vitamina = f"{mensaje[0]};{sumaCantidadVitaminas}"
    listaVitaminas.append(vitamina)

mensajeFinal = ""

for linea in listaVitaminas:
    mensaje = linea.split(";")
    
    if float(mensaje[1]) == mayorCantidadVitaminas:
        alimentoConMasVitaminas = mensaje[0]
        mensajeFinal += alimentoConMasVitaminas + ";" + str(mayorCantidadVitaminas) + "\n"

resultadoFinal = open("resultado_reducer4.txt", "w", encoding="utf-8")
resultadoFinal.write(mensajeFinal[:-1])
resultadoFinal.close()