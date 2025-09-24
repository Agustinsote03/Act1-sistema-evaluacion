def calcular_puntaje(stats): #stats es un diccionario, cuya clave es el nombre del equipo y el valor es otro diccionario con las estadisticas
    innovacion = 3
    presentacion = 1
    puntos = innovacion * stats['innovacion'] + presentacion * stats['presentacion']
    if stats['errores']:
        puntos = puntos - 1
    return puntos

def puntajes_con_map(ronda):
    """
    Devuelve un diccionario {equipo: puntaje} usando map()
    """
    return dict(map(lambda item: (item[0], calcular_puntaje(item[1])), ronda.items()))

def mejor_equipo_de_ronda(ronda): #ronda es un diccionario
    # Uso de la función auxiliar con map()
    puntajes = puntajes_con_map(ronda)
    mejor_equipo = max(puntajes, key=puntajes.get) #me quedo con la clave del diccionario que tiene el valor mas alto
    return mejor_equipo

def procesar_evaluaciones_completo(evaluaciones):
    equipos = list(evaluaciones[0].keys())
    estadisticas = {equipo: {
        'innovacion_total': 0, 'presentacion_total': 0, 'errores_total': 0,
        'veces_mejor': 0, 'puntos_totales': 0
    }for equipo in equipos}
    
    resultados_por_ronda = []
    puntajes_acumulados = {equipo: 0 for equipo in equipos}
    
    print("PROCESANDO EVALUACIONES...")
    print("=" * 50)
    
    for numero_ronda, ronda in enumerate(evaluaciones, 0):
        puntajes_ronda = puntajes_con_map(ronda) #Uso de map() para calcular todos los puntajes
        mejor_equipo_ronda = "none"
        mejor_puntaje_ronda = -1
        
        print(f"RONDA {numero_ronda + 1}")
        print("=" * 30)
        
        #Se recorren los puntajes calculados
        for equipo, puntaje in puntajes_ronda.items():
            puntajes_acumulados[equipo] += puntaje
            
            #Se acumulan las estadisticas
            estadisticas[equipo]['innovacion_total'] += ronda[equipo]['innovacion']
            estadisticas[equipo]['presentacion_total'] += ronda[equipo]['presentacion']
            estadisticas[equipo]['puntos_totales'] += puntaje
            if ronda[equipo]['errores']: 
                estadisticas[equipo]['errores_total'] += 1
            
            if puntaje > mejor_puntaje_ronda:
                mejor_puntaje_ronda = puntaje
                mejor_equipo_ronda = equipo
                
        estadisticas[mejor_equipo_ronda]['veces_mejor'] += 1
        print(f"MEJOR EQUIPO DE LA RONDA: {mejor_equipo_ronda} ({mejor_puntaje_ronda} puntos)")
        print("\nRANKING ACTUALIZADO:")
        
        ranking_actual = sorted(puntajes_acumulados.items(), key=lambda x: x[1], reverse=True)
        for pos, (equipo, puntaje) in enumerate(ranking_actual, 1):
            print(f"   {pos}. {equipo}: {puntaje} puntos")
        
        # Guardar resultados
        resultados_por_ronda.append({
            'ronda': numero_ronda + 1,
            'puntajes': puntajes_ronda,
            'mejor_equipo': mejor_equipo_ronda,
            'mejor_puntaje': mejor_puntaje_ronda
        })
        
        print("-" * 50) 
    
    return {
        'estadisticas': estadisticas,
        'resultados_por_ronda': resultados_por_ronda,
        'puntajes_acumulados': puntajes_acumulados
    }

#Para punto (4)
def mostrar_tabla_de_resultados(puntajes_acumulados):
    ranking = sorted(puntajes_acumulados.items(), key=lambda x: x[1], reverse=True) #ranking es una lista de tuplas (equipo, puntaje)
    print("\nTABLA DE RESULTADOS FINAL")
    print("=" * 50)
    for equipo, puntaje in ranking:
        print(f"{equipo}: {puntaje} puntos")



    
        
        
        