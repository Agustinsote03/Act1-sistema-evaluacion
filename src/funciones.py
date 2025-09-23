def calcular_puntaje(stats): #stats es un diccionario, cuya clave es el nombre del equipo y el valor es otro diccionario con las estadisticas
    innovacion = 3
    presentacion = 1
    puntos = innovacion * stats['innovacion'] + presentacion * stats['presentacion']
    if stats['errores']:
     puntos = puntos - 1
    return puntos

def mejor_equipo_de_ronda(ronda): #ronda es un diccionario
    puntajes = {} #diccionario vacio
    for equipo, stats in ronda.items(): #recorro el diccionario, y voy tomando la clave(equipo) y el valor(stats)
        puntuacion = calcular_puntaje(stats) #Guardo el puntaje en la variable
        puntajes[equipo] = puntuacion #la clave es el equipo y el valor es la puntuacion
    mejor_equipo = max(puntajes, key=puntajes.get) #me quedo con la clave del diccionario que tiene el valor mas alto
    return mejor_equipo

def mostrar_mejor_equipo_por_ronda(evaluaciones):
    print("MEJOR EQUIPO POR RONDA")
    print("=" * 50)

    for i, ronda in enumerate(evaluaciones,0):
      mejor_equipo = mejor_equipo_de_ronda(ronda) #llamo a la funcion que me devuelve el mejor equipo de la ronda
      puntaje_mejor = calcular_puntaje(ronda[mejor_equipo])
      print(f"\nRonda {i+1}: {mejor_equipo} - {puntaje_mejor} puntos")
            
      
    

def generar_tabla_de_resultados(evaluaciones):
    resultados = {}   
    for ronda in evaluaciones:
        for equipo, stats in ronda.items():
            puntaje = calcular_puntaje(stats)
            resultados[equipo] = resultados.get(equipo, 0) + puntaje 
    ranking = sorted(resultados.items(), key=lambda x: x[1], reverse=True)  
    for equipo, puntaje in ranking:
        print(f"{equipo}: {puntaje} puntos") 
    return ranking  #retornamos el ranking, que es una lista de tuplas (equipo, puntaje)