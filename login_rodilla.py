import streamlit as st

def mostrar_login():
    st.markdown("""
    <style>

    header[data-testid="stHeader"] {
        visibility: hidden;
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
                
    [data-testid="stHeadingWithActionElements"] > h2 {
        font-size: 40px;            
    }   
         
    div[data-baseweb="select"] > div{
        height: 60px !important;
        display: flex;
        align-items: center;
        font-size: 25px;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    
    [data-testid="stSelectboxVirtualDropdown"] div {
        font-size: 25px;
        display: flex;
        height: 35px;
        align-items: center; 
    }
    [data-testid="stBaseButton-primary"] div{
        font-size: 23px;
    }
                
    </style>
    """,unsafe_allow_html=True)

    st.header("Registro de Horas", divider="grey", text_alignment="center")
    st.space()
    # 1. Entrada de usuario
    nombre = st.selectbox("Selecciona tu nombre", 
        ["Esteban", "Maria", "Andreina", "Kevin", "Noemi"],
        index=None,
        placeholder="Busca tu nombre...")
    
    
    # 2. El boton del login que comprueba lo anterior 
    

    if st.button("ACCEDER", type="primary", use_container_width=True):
        if not nombre: 
            st.error("Selecciona un Usuario")
        else: 
            st.session_state.autenticado = True
            st.session_state.usuario_nombre = nombre
            st. rerun()
