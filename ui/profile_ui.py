import streamlit as st

def render_profile_form():
    with st.expander("👤 Perfil del Adulto Mayor", expanded=False):
        nombre = st.text_input("Nombre del adulto mayor")
        age = st.number_input("Edad", min_value=1, max_value=120)

        st.write("💊 Registro de Medicamentos")

        if "medicamentos_data" not in st.session_state:
            st.session_state.medicamentos_data = [{"Medicamento":"", "Dosis":"", "Hora(s)":""}]

        meds_df = st.data_editor(
            st.session_state.medicamentos_data,
            num_rows="dynamic",
            width="stretch"
            #use_container_width=True
        )

        guardar = st.button("Guardar perfil")

    medications_str = ""

    for med in meds_df:
        if med.get("Medicamento"):
            medications_str += f"- {med['Medicamento']} | Dosis: {med['Dosis']} | Hora: {med['Hora(s)']}\n"

    return {
        "nombre": nombre,
        "age": age,
        "medications": medications_str.strip(),
        "guardar": guardar
    }