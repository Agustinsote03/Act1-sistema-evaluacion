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

def procesar_evaluaciones_completo(evaluaciones):
    # Inicializo un diccionario para almacenar las estadísticas acumuladas de cada equipo
    equipos = list(evaluaciones[0].keys()) #tomo los nombres de los equipos
    # Defino las estadísticas que quiero rastrear, en un diccionario anidado por equipo
    estadisticas = {equipo: {
         'innovacion_total': 0,
         'presentacion_total': 0,
         'errores_total': 0,
         'veces_mejor': 0,
         'puntos_totales': 0
        } for equipo in equipos}
    
    resultados_por_ronda = []  # Lista para almacenar los resultados de cada ronda
    puntajes_acumulados = {equipo: 0 for equipo in equipos}  # Diccionario para acumular puntajes
    print("PROCESANDO EVALUACIONES...")
    print("=" * 50)
    
    for numero_ronda, ronda in enumerate(evaluaciones, 0):
     puntajes_ronda = {} #Diccionario para almacenar los puntajes de cada equipo en la ronda actual
     mejor_equipo_ronda= "none"
     mejor_puntaje_ronda= -1
     print(f"\nRonda {numero_ronda + 1}:")
     print("-" * 50)
    
     for equipo, stats in ronda.items(): #recorro el diccionario, y voy tomando la clave(equipo) y el valor(stats)
        puntaje=calcular_puntaje(stats)
        puntajes_ronda[equipo]=puntaje   
        puntajes_acumulados[equipo] += puntaje  
        
        # Acumulo el puntaje del equipo (Para el punto 4)
        
        estadisticas[equipo]['innovacion_total'] += stats['innovacion']
        estadisticas[equipo]['presentacion_total'] += stats['presentacion']
        estadisticas[equipo]['puntos_totales'] += puntaje
        if stats['errores']: estadisticas[equipo]['errores_total'] += 1 #Cuento los errores
        
        #Ahora buscamos el mejor equipo de la ronda (Lo mostramos durante el recorrido)
        if puntaje > mejor_puntaje_ronda:
            mejor_puntaje_ronda = puntaje
            mejor_equipo_ronda = equipo
        print(f"{numero_ronda + 1} - {equipo}: {puntaje} puntos")
    #Ahora se guarda el mejor equipo de la ronda
    estadisticas[mejor_equipo_ronda]['veces_mejor'] += 1
    #Guardo los resultados de la ronda
    resultados_por_ronda.append({
      'ronda': numero_ronda,
      'puntajes': puntajes_ronda,
      'mejor_equipo': mejor_equipo_ronda,
      'mejor puntaje': mejor_puntaje_ronda        
     })
    #Ahora devolvemos una estructura con las estadisticas, los resultados por ronda y los puntajes acumulados
    return {
        'estadisticas': estadisticas, #diccionario con las estadisticas de cada equipo
        'resultados_por_ronda': resultados_por_ronda, #esta estructura es una lista de diccionarios
        'puntajes_acumulados': puntajes_acumulados #diccionario con los puntajes acumulados de cada equipo
}

#Para punto (4)
def mostrar_tabla_tabla_de_resultados(puntajes_acumulados):
    ranking = sorted(puntajes_acumulados.items(), key=lambda x: x[1], reverse=True)
    print("\nTABLA DE RESULTADOS FINAL")
    print("=" * 50)
    for equipo, puntaje in ranking:
        print(f"{equipo}: {puntaje} puntos")
    return ranking


    
        
        
        