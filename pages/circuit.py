import streamlit as st

# Importing standard Qiskit libraries
from qiskit import QuantumCircuit  #Importing the QuantumCircuit function from Qiskit. We will use this to create our quantum circuits!

# We will use these functions to run our circuit and visualize its final state
from qiskit import transpile
from qiskit_aer import AerSimulator

# For array manipulation and plotting
import numpy as np
import matplotlib.pyplot as plt




# Caching the circuit setup to avoid recalculating every time
def setup_circuit():
    #num qubits = 6
    num_qubits = st.slider(min_value = 2, max_value = 10,label ='Select number of qubits', value = 6)

    # Create a quantum circuit with 6 qubits and 6 classical bits
    qc = QuantumCircuit(num_qubits, num_qubits)
    
    # Apply Hadamard to all qubits to create superposition
    for qubit in range(num_qubits):
        qc.h(qubit)

    # Add some other random gates to some of the qubits
    for qubit in range(0, num_qubits - 1, 2):
        qc.cx(qubit, qubit + 1)

    # Measure all qubits
    for i in range(num_qubits):
        qc.measure(i, i)

    return qc

qc = setup_circuit()

# Display the title in Streamlit
st.title("Quantum Circuit Visualization with Qiskit & Streamlit")

# Draw the circuit using Matplotlib
st.write("### Quantum Circuit:")
fig = qc.draw(output='mpl')  # matplotlib figure

# Display the circuit figure
st.pyplot(fig)

# Instructions or additional text
st.write(
    """
    This circuit applies a Hadamard gate to each qubit, then applies
    CNOT gates between pairs of qubits. Finally, it measures the qubits.
    You can experiment with changing the gates or number of qubits!
    """
)

