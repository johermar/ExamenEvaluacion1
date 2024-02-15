#Ejercicio 5: Descomposición de Dirección IP

#Crea un script que tome una dirección IP como argumento y la descomponga en sus cuatro octetos, mostrándolos línea a línea.

def descomponer_ip(ip):
    octetos = ip.split('.')
    for octeto in octetos:
        print(octeto)

# Ejemplo de uso
ip = "192.168.1.1"
descomponer_ip(ip)