# Función para formatear la cadena de texto
def formatear_receta(nombre_receta, numero_calorias):
    return f"La receta de {nombre_receta} contiene {numero_calorias} calorías."

# Función para solicitar los datos al usuario
def solicitar_datos():
    nombre_receta = (pizza)
    numero_calorias = (300)
    return nombre_receta, numero_calorias

# Función principal
def main():
    nombre_receta, numero_calorias = solicitar_datos()
    texto_final_correcto = formatear_receta(nombre_receta, numero_calorias)
    print(texto_final_correcto)
    
    texto_final_correcto = f"La receta de {nombre_receta} contiene {numero_calorias} calorías."
    print(texto_final_correcto)

# Ejecutar la función principal
if _name_ == "_main_":
    main()
