#Otener oracion del user

original = input ( " Ingresa una oracion: "). strip().lower()

# obtener oracion del user

palabras = original.split()

# Recorrer oalabaras y convertirlas con el traductor
nuevaspalabras = []
for palabra in palabras:
    if palabra [0] in " aeiou":
        nueva_palabra = palabra + "yay"
        nuevaspalabras.append(nueva_palabra)
    else:
        vocal_pos = 0
        for letra in palabra:
            if letra not in "aeiou":
                vocal_pos = vocal_pos + 1
            else:
                break
    cons = palabra [ :vocal_pos]
    el_resto =  palabra[vocal_pos:]
    nueva_palabra = el_resto + cons +"ay"
    nuevaspalabras.append(nueva_palabra) 

# Unir  Palabaras en una oracion

salida = " ".join(nuevaspalabras)

# Generar cadena final

print(salida)