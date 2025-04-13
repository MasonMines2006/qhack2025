import streamlit as st
# Importing standard Qiskit libraries
from qiskit import QuantumCircuit  #Importing the QuantumCircuit function from Qiskit. We will use this to create our quantum circuits!

# We will use these functions to run our circuit and visualize its final state
from qiskit import transpile
from qiskit_aer import AerSimulator

# For array manipulation and plotting
import numpy as np
import matplotlib.pyplot as plt

def setup_circuit():
    num_qubits = st.slider(min_value=2, max_value=10, label='Select number of qubits', value=6)
    qc = QuantumCircuit(num_qubits, num_qubits)

    for qubit in range(num_qubits):
        qc.h(qubit)

    for qubit in range(0, num_qubits - 1, 2):
        qc.cx(qubit, qubit + 1)

    for i in range(num_qubits):
        qc.measure(i, i)

    return qc

qc = setup_circuit()
st.write("### Quantum Circuit:")
fig = qc.draw(output='mpl')
st.pyplot(fig)


if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def generate_circuit():
    st.session_state.clicked = True

st.button('Click me to simulate and visualize', on_click=generate_circuit)

if st.session_state.clicked:
    qc = setup_circuit()

    simulator = AerSimulator()
    shots = 64
    compiled_circuit = transpile(qc, simulator)

    result = simulator.run(compiled_circuit, shots=shots).result()
    counts = result.get_counts()
    st.write("Measurement outcomes:", counts)

    st.write("### Quantum Circuit:")
    fig = qc.draw(output='mpl')
    st.pyplot(fig)

    st.write(
        """
        This circuit applies a Hadamard gate to each qubit, then applies
        CNOT gates between pairs of qubits. Finally, it measures the qubits.
        You can experiment by changing the number of qubits or gates!
        """
    )
