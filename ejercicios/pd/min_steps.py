# (★★) Dado un número K, se quiere obtener la mínima cantidad de operaciones para llegar desde 0 a K,
# siendo que las operaciones posibles son:
# (i) aumentar el valor del operando en 1;
# (ii) duplicar el valor del operando.
# Implementar un algoritmo que, por programación dinámica, obtenga la menor cantidad de operaciones 
# (y cuáles son dichas operaciones). Desarrollar la ecuación de recurrencia. 
# Indicar y justificar la complejidad del algoritmo implementado. 
# Aclaración: asegurarse de que el algoritmo presentado sea de programación dinámica, 
# con su correspondiente ecuación de recurrencia.

# Recurrencia: 
#
# opt(k) = (
#   0                               --> si k = 0
#   opt(k-1) + 1                    --> si k impar
#   min(opt(k-1), opt(k/2)) + 1     --> si k par
# )

def min_steps(k):
    opt = [0] * (k+1)
    i = 0
    opt[1] = 1
    opt[2] = 2

    for i in range(2, k+1):
        if i % 2 == 0:
            idx = i//2
            opt[i] = 1 + min(opt[i-1], opt[idx])
        else:
            opt[i] = 1 + opt[i-1]
    
    # reconstruccion
    ops = []
    while i > 0:
        if i % 2 == 0 and opt[i] == 1 + opt[i//2]:
            i = i // 2
            ops.append("*2")
        else:
            i = i - 1
            ops.append("+1")
    ops.reverse()
    print(ops)
    
    return opt[k]

if __name__ == "__main__":
    print(min_steps(2))
