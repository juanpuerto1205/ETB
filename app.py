import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuración de la conexión con Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Seleccionar la hoja de cálculo y la hoja específica
spreadsheet = client.open("BD_DEMO_ETB")
worksheet = spreadsheet.sheet1

# Función para leer datos
def get_data():
    data = worksheet.get_all_records()
    return data

# Función para agregar datos
def add_data(row):
    worksheet.append_row(row)

# Interfaz de Streamlit
st.title("DEMO ETB RPA")

menu = ["Leer datos", "Agregar datos"]
choice = st.sidebar.selectbox("Menú", menu)


Tipo_agente = ['Agente A','Agente B','Agente C','Agente D','Agente E']
Tipo_resolucion = ['Resuelto','No Resuelto','Pendiente']
Tipo_csat = ['1','2','3','4','5']
Tipo_respuesta = ['Satisfecho','Insatisfecho','Neutral']

if choice == "Leer datos":
    st.subheader("Datos de Google Sheets")
    data = get_data()
    #data = data.dropna(how='all')
    st.dataframe(data)

elif choice == "Agregar datos":
    st.subheader("Agregar nueva fila")
    IdLlamada = st.text_input(label = "IdLlamada")	
    IdCliente = st.text_input(label = "Cedula Cliente")	
    NombreCliente = st.text_input(label = "Nombre Cliente")		
    NombreAgente = st.selectbox('Agente Encargado', options=Tipo_agente, index=None)
    Resolucion = st.selectbox('Estado Resolucion', options=Tipo_resolucion, index=None)
    Csat = st.selectbox('Indice Satisfaccion', options=Tipo_csat, index=None)	
    RespuestaCliente = st.text_input(label = "Respuesta del Cliente")	

    if st.button("Agregar"):
        add_data([IdLlamada, IdCliente, NombreCliente, NombreAgente, 
                  Resolucion, Csat, RespuestaCliente])
        st.success("Datos agregados exitosamente")
