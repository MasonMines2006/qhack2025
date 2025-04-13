import streamlit as st
from qiskit import QuantumCircuit
from qiskit import transpile
from qiskit_aer import AerSimulator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pydeck as pdk

# Set up the page
st.set_page_config(page_title="Quantum Circuit Simulation", layout="centered")
st.title("Quantum Circuit Simulation")
st.markdown("---")
st.header("Create and Simulate a Quantum Circuit")
st.write("This app allows you to create a quantum circuit, simulate it, and visualize the results.")
st.write("You can adjust the number of qubits and see how the circuit behaves.")
st.markdown("---")

def generate_slider():
        num_qubits = st.slider(min_value=2, max_value=16, label='Select number of qubits', value=6)
        return num_qubits
def setup_circuit():
    st.session_state.num_qubits = num_qubits  # Save to session state
    
    return qc

# Initialize stage state if not present
if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

# Stage 0: Initial button to start
if st.session_state.stage == 0:
    st.button('Begin', on_click=set_state, args=[1], key="begin_button")

# Stage 1: Create the quantum circuit
if st.session_state.stage >= 1:
    num_qubits = generate_slider()
    qc_demo = QuantumCircuit(num_qubits, num_qubits)
    for i in range(num_qubits):
        qc_demo.measure(i, i)
    st.write("### Quantum Circuit:")
    fig = qc_demo.draw(output='mpl')
    st.pyplot(fig)

    # Button to go to the next stage
    st.button('Next Step', on_click=set_state, args=[2], key="next_step_1")

# Stage 2: Apply gates to the quantum circuit
if st.session_state.stage >= 2:
    qc = QuantumCircuit(num_qubits, num_qubits)

    # Create a multiselect for users and a toggle for rolling average
    all_gates = ["H-Gate", "Z-Gate", "CX-Gate"]
    with st.container():
        gates = st.multiselect("Gates", all_gates, default=all_gates)
        st.session_state.additional_data = st.checkbox("Generate Additional Data")

    # 1. Apply Hadamard to all qubits to create superposition
    if "H-Gate" in gates:
        for qubit in range(num_qubits):
            qc.h(qubit)

    # 2 Add some other random gates to some of the qubits. Try using the X or cx gates
    if "CX-Gate" in gates:
        for qubit in range(0, num_qubits - 1, 2):
            qc.cx(qubit, qubit + 1)
    
    if "Z-Gate" in gates:
        for qubit in range(num_qubits):
            qc.z(qubit)

    # 3. Measure all qubits
    for i in range(num_qubits):
        #Write the code to measure qubits in here
        qc.measure(i, i)

    st.write("### Quantum Circuit with Gates:")
    fig = qc.draw(output='mpl')
    st.pyplot(fig)

    # Button to go to the next stage
    st.button('Next Step', on_click=set_state, args=[3], key="next_step_2")

# Stage 3: Simulate the quantum circuit
if st.session_state.stage >= 3:
    st.write("### Simulating the Quantum Circuit:")
    simulator = AerSimulator()
    shots = (num_qubits*num_qubits)
    compiled_circuit = transpile(qc, simulator)

    result = simulator.run(compiled_circuit, shots=shots).result()
    counts = result.get_counts()
    
    bitstring_list = []
    for bitstring, cnt in counts.items():
        bitstring_list.extend([bitstring] * cnt)

    
    int_values = []
    for bs in bitstring_list:
        value = int(bs, 2)
        int_values.append(value)

    int_array = np.array(int_values).reshape(num_qubits, num_qubits)  # Reshaping to 8x8

    if not st.session_state.additional_data:
        set_state(4)  # Skip to stage 4
    else: 
        st.write("Measurement outcomes:", counts)
        st.write("We have", len(bitstring_list), "bitstrings in total.")
        st.write("### Converted Integer Array:")
        st.write(int_array)
        # Button to go to the next stage
        st.button('Next Step', on_click=set_state, args=[4], key="next_step_3")

    

# Stage 6: Visualize the results
if st.session_state.stage >= 4:
    tab1, tab2, tab3 = st.tabs(["Pixel-Art", "3-D Plot", "DNA"])

    with tab1:
        # Create the plot
        fig, ax = plt.subplots()
        ax.imshow(int_array, cmap='coolwarm', interpolation='nearest')
        ax.set_title("Quantum Randomness in Pixel Art")

        ax.axis('off')  # Hide the axis
        # Display the plot in Streamlit
        st.pyplot(fig)
    with tab2:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        X, Y = np.meshgrid(np.arange(num_qubits), np.arange(num_qubits))
        ax.plot_surface(X, Y, int_array, cmap='coolwarm')
        st.pyplot(fig)
    with tab3:
        dna_library = {
                '0': 'A',
                '1': 'C',
                '2': 'G',
                '3': 'T'
            }
        dna_sequence = []
                
        for row in int_array:
            for value in row:
                dna_base = dna_library[str(value % 4)]  # Use modulo to ensure values map correctly
                dna_sequence.append(dna_base)

        dna_sequence_str = ''.join(dna_sequence)
        st.write("Generated DNA Sequence:", dna_sequence_str)
    
    # Option to start over
    st.button('Start Over', on_click=set_state, args=[0], key="start_over")

    # Final instructions or explanation
    st.write(
        """
    
        """
    )

