import streamlit as st

# Importing standard Qiskit libraries
from qiskit import QuantumCircuit  #Importing the QuantumCircuit function from Qiskit. We will use this to create our quantum circuits!

# We will use these functions to run our circuit and visualize its final state
from qiskit import transpile
from qiskit_aer import AerSimulator

# For array manipulation and plotting
import numpy as np
import matplotlib.pyplot as plt

print("Libraries imported successfully!")


st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")