# Armando, el arquitecto, fue contratado por la ciudad para diseñar un nuevo aeropuerto internacional
# con una capacidad inigualable para mover pasajeros.
# Ya tiene diseñado el plan de piso de la terminal A, que tiene forma de un largo pasillo recto
# con puertas de abordaje de un lado y locales de Duty Free del otro.
# Quiere colocar puestos para el personal de seguridad en algunas de las puertas,
# de tal modo que ninguna puerta quede a una distancia mayor de d metros de algún puesto de seguridad.
# Diseñar un algoritmo que, dado un arreglo con la ubicación de cada puerta
# (representada en metros desde el inicio de la terminal), le permita a Armando
# asignar la menor cantidad de puestos de seguridad posible.

def puertas_aeropuerto(puertas: list[int], distancia: int) -> set[int]:
    alcance = -9999999999
    puestos = set()

    puertas.sort()

    i = 0
    while i < len(puertas):
        actual = puertas[i]

        if actual in puestos or actual <= alcance:
            i+=1
            continue

        # busco la puerta siguiente a donde ira el puesto
        j = i
        while j < len(puertas) and  (-1 * (puertas[i] - puertas[j]) <= distancia):
            j+=1

        puestos.add(puertas[j-1])
        alcance = distancia + puertas[j-1]

        i+=1

    return puestos


if __name__ == "__main__":
    print(puertas_aeropuerto([5, 10, 15, 20, 25, 30, 35, 60, 70, 75], 5))
