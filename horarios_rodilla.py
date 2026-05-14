import streamlit as st
from login_rodilla import mostrar_login
from datetime import datetime, time

st.set_page_config(page_title="Login Rodilla", layout="centered")

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

def mostrar_horarios():
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
    [data-testid="stWidgetLabel"] p{
        font-size: 25px;
    }
    
    div[data-baseweb="select"] > div{
        height: 45px !important;
        display: flex;
        align-items: center;
        font-size: 25px;
    }
        </style>
        """, unsafe_allow_html=True)
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
        st.write(f"Vas a registrar el siguiente horario para hoy: ")
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


if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
if "finalizado" not in st.session_state:
    st.session_state.finalizado = False


if not st.session_state.autenticado:
    mostrar_login()
    
elif st.session_state.finalizado:
    mostrar_agradecimiento()
else: 
    mostrar_horarios()
