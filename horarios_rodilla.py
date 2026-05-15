import streamlit as st
import os
from login_rodilla import mostrar_login
from datetime import datetime, time

st.set_page_config(page_title="Rodilla Molina", layout="wide")

def estilos_globales():

    st.markdown("""
    <style>
        /*  conteo cajas  */        
        p{
        font-size: 30px !important;
        }
                 
        footer {
        visibility: hidden;
        height: 0%;
        }
            
        button[data-testid="stNumberInputStepDown"],button[data-testid="stNumberInputStepUp"]{
            padding-right: 50px;       
            padding-left: 50px;  
            border: 1px solid #a8a0a0; 
            border-radius: 5px; 
        }   
        div[data-testid="stNumberInputContainer"], input[data-testid="stNumberInputField"]{
                
            height: 70px;        
            font-size: 30px;
        }  
        div[data-testid="stNumberInputContainer"]:focus-within {
            border-color: #1f80cf !important;
            box-shadow: 0 0 10px rgba(31, 128, 207, 0.2);
        }        
                
        /*    vista_fechar  */      
                 
        header[data-testid="stHeader"] {
        visibility: hidden;
        transition: opacity .3s ease;
        }
    
        header[data-testid="stHeader"]:hover {
            opacity: 1;
        }
        .stMainBlockContainer {
            padding-top: 1rem !important;
        }
        
        div[data-baseweb="select"] > div{
            height: 45px !important;
            display: flex;
            align-items: center;
            font-size: 25px;
        }
                
        [data-testid="stBaseButton-primary"] p{
            font-size: 25px !important;
        }
                      
        /* ------- lo nuevo --------- */ 
        div[data-baseweb="tab-list"] {
        width: 100% !important;
        display: flex !important;
        justify-content: space-around !important;
        gap: 0px !important; 
        }
                
        button[data-testid="stTab"] {
        flex: 1 !important; /* Cada tab ocupa 1/3 del ancho */
        padding-bottom: 10px; 
        padding-top: 10px; 
        }
                
        button[data-testid="stTab"] p {
            font-size: 30px !important;   
            margin: 0 !important; 
        }
        
        button[aria-label="Scroll tabs right"], 
        button[aria-label="Scroll tabs left"] {
            display: none !important;
        }
        
        li[role="option"] {
            font-size: 25px !important; 
            padding-top: 10px !important;
            padding-bottom: 10px !important;
        }
        li[role="option"] div {
            height: auto !important; 
        }

        div[data-baseweb="tab-highlight"] {
            background-color: #00843D !important; /* Línea verde */
        }
    </style>
    """,unsafe_allow_html=True)

def conteo_cajas(): 
    st.header("Conteo de Cajas", divider="green", text_alignment="center")

    ###Empiezan las monedas ###
    st.space("small")
    st.header("Monedas",text_alignment="center")
    st.space()

    e2 = st.number_input(label="2 Euros: ", min_value=0, placeholder="0", key="2e")* 2
    e1 = st.number_input(label="1 Euro: ", min_value=0, placeholder="0", key="1e")  * 1
    c50 = st.number_input(label="50 Céntimos:", min_value=0,  placeholder="0", key="50c")* 0.50
    c20 = st.number_input(label="20 Céntimos: ", min_value=0,  placeholder="0", key="20c") * 0.20
    c10 = st.number_input(label="10 Céntimos: ", min_value=0,  placeholder="0", key="10c") * 0.10
    c5 = st.number_input(label="5 Céntimos: ", min_value=0,  placeholder="0", key="5c")* 0.05
    c2 = st.number_input(label="2 Céntimos: ", min_value=0,  placeholder="0", key="2c") * 0.02
    c1 = st.number_input(label="1 Céntimo: ", min_value=0,  placeholder="0", key="1c")* 0.01

    ###Empieza los billetes####

    st.divider()
    st.header("Billetes",text_alignment="center")
    st.space()

    numeros = [1,2,3,4,5,6,7,8,9,10,11]

    b50 = st.number_input(label="50 Euros: ", min_value=0, key="50b") * 50
    b20 = st.number_input(label="20 Euros: ", min_value=0,  key="20b")  * 20
    b10 = st.number_input(label="10 Euros: ", min_value=0,  key="10b")* 10
    b5 = st.number_input(label="5 Euros: ", min_value=0,  key="5b")  * 5
    billetefalso = st.selectbox(options=numeros, label="",label_visibility="collapsed", index=None, placeholder="")

    total = e2 + e1 + c50 + c20 + c10 + c5 + c2 + c1 + b50 + b20 + b10 + b5
    declarar = total - 100
    def reset_cajas():
        limpiar = ["2e","1e","50c","20c","10c","5c","2c","1c","50b","20b", "10b", "5b"]
        for key in limpiar:
            st.session_state[key]=0

    st.divider()
    st.space()

    ###Empiezan los botones ###
    @st.dialog("¿Reiniciar conteo?")
    def modal_confirmar_reset():
        st.write("¿Estás seguro de que quieres borrar todos los datos?")
        
        col_si, col_no = st.columns(2)
        
        if col_si.button("Sí, borrar todo", type="primary", use_container_width=True):
            # Ejecutamos la limpieza
            limpiar = ["2e","1e","50c","20c","10c","5c","2c","1c","50b","20b", "10b", "5b"]
            for key in limpiar:
                st.session_state[key] = 0
            st.rerun() # Recargamos para que los inputs vuelvan a 0
            
        if col_no.button("Cancelar", type="secondary", use_container_width=True):
            st.rerun() # Simplemente cerramos el modal

    left, right = st.columns(2)
    contar = left.button(label="Contar", type="primary", width="stretch")
    reset = right.button(label="Reset", type="secondary",on_click=modal_confirmar_reset, width="stretch" )

    if contar: 
        if total < 100: 
            st.error("⚠️ ERROR. El total no puede ser menor que 100€")
            st.info("Revisa el conteo de monedas y billetes.")
        else: 
            st.write(f"El total de la caja es: **{total:.2f}** euros")
            st.write(f"Total a declarar: **{declarar:.2f}** euros")

def mostrar_agradecimiento():
    st.markdown("""
        <style>
        header[data-testid="stHeader"] {
        opacity: 0;
        transition: opacity .3s ease;
    }
    
    header[data-testid="stHeader"]:hover {
        opacity: 1;
    }
    .stMainBlockContainer {
        padding-top: 2rem !important;
    }             
        </style>
        """,unsafe_allow_html=True)
    st.header("¡Muchas Gracias!", text_alignment="center")
    st.subheader("Tu turno ha sido registrado correctamente", text_alignment="center")
    st.balloons()

    st.space()

    if st.button("Volver al inicio", type="secondary"):
        st.session_state.autenticado = False
        st.session_state.finalizado = False
        st.rerun()

def vista_fechar():
    nombre = st.session_state.usuario_nombre
    hoy = datetime.now()

    st.header("Registro de Horas", text_alignment="center", divider="green")
    st.subheader(f"📅 {hoy.strftime(" %d / %m / %Y")}")

    st.space()

    entrada = st.time_input("Hora Entrada", time(7,0))

    st.divider()

    salida = st.time_input("Hora Salida", time(15,0))

    @st.dialog("¿Confirmar Turno?")
    def confirmar_envio(n, e, s): 
        st.write(f"Vas a registrar el siguiente horario para hoy, **{hoy.strftime('%d/%m/%Y')}**: ")
        st.info(f"{n} | {e.strftime('%H:%M')} - {s.strftime('%H:%M')}")
        st.write("¿Los datos son correctos?")
        col_si, col_no = st.columns(2)
    
        if col_si.button("Sí, Firmar", type="primary", use_container_width=True):
            st.session_state.finalizado = True
            st.rerun()
            
        if col_no.button("Cancelar", type="secondary", use_container_width=True):
            st.rerun() 

    if st.button("Registrar turno", type="primary", use_container_width=True):
        if entrada and salida:
            confirmar_envio(nombre,entrada,salida)
        else: 
            st.warning("⚠️ Completa todos los campos para proceder")
    if st.button("Cerrar sesion", type="secondary"):
        st.session_state.autenticado = False
        st.rerun()

def vista_horarios():
    st.header("Consulta de Horarios", divider="green", text_alignment="center")

    dict_horarios = {
        "Mayo 18-24 ": "horarios/18-24-05.JPG",
        "Mayo 11-17": "horarios/11-17-05.JPG",
        "Mayo 04-10": "horarios/04-10-05.JPG"
    }

    semana = st.selectbox("Selecciona la semana", list(dict_horarios.keys()))

    ruta = dict_horarios[semana]

    if os.path.exists(ruta):
        st.image(ruta, width="content")
        
    else: 
        st.error("ERROR. Foto no subida todavia")

if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
if "finalizado" not in st.session_state:
    st.session_state.finalizado = False

if not st.session_state.autenticado:
    mostrar_login()
    
elif st.session_state.finalizado:
    mostrar_agradecimiento()
else: 

    estilos_globales()

    tab_fichar, tab_ver, tab_cajas = st.tabs(["🕒", "🗓️", "💵"])
    with tab_fichar: 
        vista_fechar()
    with tab_ver: 
        vista_horarios()
    with tab_cajas: 
        conteo_cajas()

