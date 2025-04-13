import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Quantum Intro", layout="centered")

st.title("A basic introduction to quantum concepts and computing")

st.markdown("---")

st.header("Welcome!")
st.write("This is a simple web app to help you explore quantum computing concepts.")

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.dataframe(df)
