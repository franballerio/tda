# Queremos meter en una mochila de capacidad W el mayor valor posible.
# Contamos con N elementos N_i = [Peso_i, Valor_i]
#
# Como siempre en un problema combinatorio vamos a tener 2 opciones:
#   - Si uso el elemento
#   - No uso el elemento
#
# Pero que nos garantiza que este elemento N_i no va mejor con otra combinacion de elementos
# que podriamos no haber considerado?
#       Lo resolvemos pensando el problema en 2 dimensiones.
#       Para este N_i elemento elijo el maximo entre mis 2 opciones, pero con una magia mas:
#           - si lo uso --> considero: Valor_i + opt(N - 1, W - Peso_i)
#           - no lo uso --> considero: opt(N - 1, W)
#
#       Esto nos garantiza que los optimos anteriores que estamos chequeando son realmente
#       la mejor opcion que podriamos considerar.
#
