Python
import pandas as pd

print("--- TAREA DE CONDICIONALES: CALIDAD DEL AGUA ---")

# 1. Tupla con nombres de sitios inventados (datos fijos)
sitios = ("Estación Norte", "Estación Sur", "Estación Centro", "Laguna Alta", "Río Bajo")

# 2. Lista con una medición inventada (ejemplo: Oxígeno Disuelto en mg/L)
oxigeno = [8.2, 4.5, 6.1, 9.0, 3.8]

# 3. Diccionario que une los datos para formar las columnas
datos = {
    "Sitio": sitios,
    "Oxigeno_mg_L": oxigeno
}

# 4. DataFrame (la tabla formal)
df = pd.DataFrame(datos)
print("\nTabla de Datos:")
print(df)

print("\n--- Evaluación con Condicionales ---")

# 5. Condicionales para evaluar cada valor de oxígeno
for i in range(len(df)):
    lugar = df.loc[i, "Sitio"]
    ox = df.loc[i, "Oxigeno_mg_L"]
    
    print(f"\nSitio: {lugar} | Oxígeno: {ox} mg/L")
    
    if ox > 7.0:
        print("-> Estado: EXCELENTE (Alta concentración de oxígeno).")
    elif 5.0 <= ox <= 7.0:
        print("-> Estado: ACEPTABLE (Niveles normales).")
    else:
        print("-> Estado: ALERTA - DEFICIENTE (Riesgo para la vida acuática).")
