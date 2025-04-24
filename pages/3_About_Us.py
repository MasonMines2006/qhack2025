import streamlit as st
from streamlit_extras.let_it_rain import rain

st.title("About Us :moyai:")
st.markdown("---")
st.header("Project: Q-Learn :sparkles:")
st.write("A beginner friendly web app geared towards testing the waters of quantum computing.")
st.markdown("---")
st.header("Functionality :microscope::")
st.write("Q-Learn aims to simplify abstract quantum concepts like qubits, superposition, and entanglement into a shortform, engaging experience. It's designed for students, enthusiasts, and curious minds just starting their quantum journey.")
st.markdown("---")
st.header("How It Was Built :building_construction::")
st.write("Frontend: Streamlit")
st.write("Backend: Qiskit, Python")
st.write("Visualization: Mathplotlib")
st.write("Deployment: Streamlit")
st.markdown("---")
st.header("Who We Are :nerd_face::")
st.write("Mason Mines - Backend ([GitHub](https://github.com/MasonMines2006))")
st.write("Conor McHaney - Frontend & UI/UX ([GitHub](https://github.com/cmchaney31))")
st.markdown("---")
rain(
        emoji="⚛",
        font_size=54,
        falling_speed=10,
        animation_length="infinite",
    )
