       

import copy

def imprimir(estado):

    for linea in estado:
        for celda in linea:
            if celda == 0:
                print("_", end = "")
            
            if celda == 1:
                print("X", end = "")
            
            if celda == -1:
                print("O", end = "")
        print()

def generar_movimiento_usuario(estado):
    no_permitido = True
    while no_permitido:    
        linea = int(input("linea de movimiento: "))
        columna = int(input("columna de movimiento: "))
    
        linea -= 1
        columna -= 1

        if estado[linea][columna] == 0:
            movimiento = copy.deepcopy(estado)
            movimiento[linea][columna] = 1
            return movimiento
        
        else:
            print("No valido")

def generar_movimiento_ia(estado):
    pass
    
    

def ganador(estado):
    
    empate = set()
    
    #Checamos si alguien gana en las lineas
    for linea in estado:
        linea = set(linea)
        if len(linea) == 1 and not 0 in linea:
            ganador = 1 if 1 in linea else -1            
            return ganador
    

    #Checamos si alguien gana en las columnas
    columnas = set()   
    for i in range(3):
        linea = list()
        for j in range(3):
            empate.add(estado[i][j])
            linea.append(estado[j][i])
        linea = tuple(linea)
        columnas.add(linea)
    for linea in columnas:
        linea = set(linea)
        if len(linea) == 1 and not 0 in linea:
            ganador = 1 if 1 in linea else -1            
            return ganador
    if 0 not in empate:
        return 0

    #Checamos si alguien gana en las diagonales
    diagonales = {(estado[0][0], estado[1][1], estado[2][2]), (estado[0][2], estado[1][1], estado[2][0])}
    for linea in diagonales:
        linea = set(linea)
        if len(linea) == 1 and not 0 in linea:
            ganador = 1 if 1 in linea else -1            
            return ganador
    return None


def movimientos(estado, jugador_maximo):
    movimientos = list()
    figura = 1 if jugador_maximo else -1
    for i, linea in enumerate(estado):
        for j, casilla in enumerate(linea):
            copia = copy.deepcopy(estado)            
            if casilla == 0:
                copia[i][j] = figura
                movimientos.append(copia)
    return movimientos
    
             


#algoritmo minimax

def minimax(estado, jugador_maximo):
    fin = ganador(estado)
    if fin is not None:
        return [fin, estado]

    if jugador_maximo:
        evaluacion_max = [-255, []]
        for hijo in movimientos(estado, jugador_maximo):
            evaluacion = minimax(hijo, False)
            evaluacion_max[1] = hijo if max(evaluacion[0], evaluacion_max[0]) > evaluacion_max[0] else evaluacion_max[1]
            evaluacion_max[0] = max(evaluacion[0], evaluacion_max[0])
        return evaluacion_max


    else:
        evaluacion_min = [255, []]
        for hijo in movimientos(estado, jugador_maximo):
            evaluacion = minimax(hijo, True)
            evaluacion_min[1] = hijo if min(evaluacion[0], evaluacion_min[0]) < evaluacion_min[0] else evaluacion_min[1]
            evaluacion_min[0] = min(evaluacion[0], evaluacion_min[0])
        return evaluacion_min
        
    



#gato = [[1, -1, 1], [0, -1, 1], [0, 0, 0]]
#print(movimientos(gato, True))
#movimiento = minimax(gato, False)
#imprimir(movimiento[1])



print("Gato: ")
print("indique la coordenada de su movimiento")
imprimir([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
tablero = [[],[[0, 0, 0], [0, 0, 0], [0, 0, 0]]]

while True:
    resultado = ganador(tablero[1])
    if ganador(tablero[1]) is not None:
        if resultado == 0:
            print("Empate")
            break
        elif resultado == -1:
            print("Gano Circulo")
            break
        else:
            print("Gano tache")
            break
    tablero[1] = generar_movimiento_usuario(tablero[1])
    imprimir(tablero[1])
    print()
    tablero = minimax(tablero[1], False)
    imprimir(tablero[1])
    print()
    
print("Se acabo el juego")
    
    
    







































