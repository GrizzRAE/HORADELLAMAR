import streamlit as st
from datetime import datetime, timedelta

# Función para calcular las horas de llamada
def calcular_horas_llamadas(hora_inicio):
    # Convertir la hora de inicio a formato datetime
    hora_inicio = datetime.strptime(hora_inicio, '%H:%M')
    
    # Crear lista para almacenar las horas de llamada
    horas_llamadas = []
    
    # Calcular las siguientes llamadas a intervalos de 4 horas
    for i in range(4):
        siguiente_hora = hora_inicio + timedelta(hours=i*4)
        horas_llamadas.append(siguiente_hora.strftime('%H:%M'))
    
    return horas_llamadas

# Interfaz de la web
st.title("Programa de Llamadas a Julisa")

# Entrada de hora de inicio
hora_inicio = st.text_input("¿A qué hora deseas llamar a Julisa por primera vez? (Formato 24h, ej. 08:00)", "08:00")

# Verificar si la hora de inicio es válida
try:
    datetime.strptime(hora_inicio, '%H:%M')
    if st.button("Calcular próximas llamadas"):
        horas_llamadas = calcular_horas_llamadas(hora_inicio)
        st.write("Las próximas llamadas a Julisa son a las siguientes horas:")
        for hora in horas_llamadas:
            st.write(f"- {hora}")
except ValueError:
    st.error("Por favor, ingresa una hora válida en formato 24h (ej. 08:00)")
