lineas = open("resultado_mapper5.csv", encoding="utf-8").read().splitlines()
# ¿Cuáles alimentos aportan más de 1 mg de hierro y menos de 3 g de grasas?
# Alimento;grasa;hierro
mensajeFinal = ""
for linea in lineas:
    mensaje = linea.split(";")
    nombreAlimento = mensaje[0]
    grasasAlimento = mensaje[1]
    hierroAlimento = mensaje[2]
    if (float(grasasAlimento) < 3) and (float(hierroAlimento) > 1):
        mensajeFinal += f"{nombreAlimento};{grasasAlimento};{hierroAlimento}\n"

#print(f"El/los alimentos con más de 1mg de hierro y menos de 3gr de grasas es/son:\n{mensajeFinal}")

resultadoFinal = open("resultado_reducer5.txt", "w", encoding="utf-8")
resultadoFinal.write(mensajeFinal[:-1])
resultadoFinal.close()