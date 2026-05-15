import streamlit as st

def conteo_cajas(): 
    st.markdown("""
    <style>
    p{
        font-size: 30px !important;
    }
        header[data-testid="stHeader"] {
        visibility: hidden;
        height: 0%;
        }
        
        .stMainBlockContainer {
            padding-top: 0rem !important; 
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
                
        
    </style>
    """,unsafe_allow_html=True)

    st.markdown("""<h1 style=" text-align: center;">Conteo de Cajas</h1>""",unsafe_allow_html=True)
    st.divider()

    ###Empiezan las monedas ###

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
        st.write(f"El total de la caja es: **{total:.2f}** euros")
        st.write(f"Total a declarar: **{declarar:.2f}** euros")