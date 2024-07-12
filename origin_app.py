import pandas as pd
import random
import streamlit as st
from faker import Faker

# Generar datos
fake = Faker('es_CO')

id_llamada = list(range(36, 236))
id_cliente = [random.randint(10000000, 9999999999) for _ in range(200)]
nombre_cliente = [fake.name() for _ in range(200)]
nombre_agente = random.choices(['Agente A', 'Agente B', 'Agente C', 'Agente D', 'Agente E'], k=200)
resolucion = random.choices(['Resuelto', 'No Resuelto', 'Pendiente'], k=200)
csat = random.choices(['1', '2', '3', '4', '5'], k=200)
respuesta_cliente = [fake.text(max_nb_chars=20) for _ in range(200)]

# Crear DataFrame
df = pd.DataFrame({
    'Id_Llamada': id_llamada,
    'IdCliente': id_cliente,
    'NombreCliente': nombre_cliente,
    'NombreAgente': nombre_agente,
    'Resolucion': resolucion,
    'CSAT': csat,
    'RespuestaCliente': respuesta_cliente
})

# Mostrar DataFrame con Streamlit
st.title('Tabla de Llamadas')
st.write(df)
