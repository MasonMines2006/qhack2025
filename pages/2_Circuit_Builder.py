import streamlit as st
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector, partial_trace
from qiskit.visualization import plot_bloch_multivector, plot_bloch_vector
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pydeck as pdk
import random
import seaborn as sns
from qiskit.qasm3 import dumps

from streamlit_extras.chart_container import chart_container 
from streamlit_extras.dataframe_explorer import dataframe_explorer

    

# Set up the page
st.set_page_config(page_title="Quantum Circuit Simulation", page_icon=":zap:", layout="centered")
st.title("Quantum Circuit Simulation")
st.markdown("---")
st.header("Build. Simulate. Visualize.")
st.write("Explore the fundamentals of quantum computing by designing your own quantum circuits—no prior experience required. " \
"Q-Learn lets you adjust the number of qubits, apply quantum gates, and simulate the outcome in real time.")
st.write("Whether you're a curious beginner or brushing up on core concepts, this interactive tool helps bring quantum mechanics to life—one gate at a time.")
st.markdown("---")
if "random_seed" not in st.session_state:
    st.session_state.random_seed = random.randint(0, 1_000_000)
seed = st.session_state.random_seed
def generate_slider():
        num_qubits = st.slider(min_value=2, max_value=16, label='Select number of qubits', value=6)
        return num_qubits
def setup_circuit():
    st.session_state.num_qubits = num_qubits  # Save to session state
    return qc
@st.cache_resource
def get_circuit(gates, num_qubits, measure=True, rand_seed=42):
    random.seed(rand_seed)

    qc = QuantumCircuit(num_qubits, num_qubits)

    if "Hadamard/H-Gate" in gates:
        for qubit in range(num_qubits):
            if random.random() < 0.8:
                qc.h(qubit)
    if "X-Gate" in gates:
        for qubit in range(num_qubits):
            if random.random() < 0.5:
                qc.x(qubit)
    if "Y-Gate" in gates:
        for qubit in range(num_qubits):
            if random.random() < 0.5:
                qc.y(qubit)
    if "CX-Gate" in gates:
        for qubit in range(0, num_qubits - 1, 2):
            if random.random() < 0.5:
                qc.cx(qubit, qubit + 1)
    if "Z-Gate" in gates:
        for qubit in range(num_qubits):
            if random.random() < 0.5:
                qc.z(qubit)

    qc_mod = qc.copy()
    if measure:
        for i in range(num_qubits):
            qc.measure(i, i)
    return qc, qc_mod
@st.cache_data
def simulate_circuit(circuit_hash: int, _qc: QuantumCircuit):
    simulator = AerSimulator()
    shots = (_qc.num_qubits ** 2)
    compiled_circuit = transpile(_qc, simulator)
    result = simulator.run(compiled_circuit, shots=shots).result()
    counts = result.get_counts()

    bitstring_list = []
    for bitstring, cnt in counts.items():
        bitstring_list.extend([bitstring] * cnt)

    int_values = [int(bs, 2) for bs in bitstring_list]
    int_array = np.array(int_values).reshape(qc.num_qubits, qc.num_qubits)

    return int_array, counts, bitstring_list
@st.cache_data
def get_statevector_from_hash(circuit_hash: int, _qc: QuantumCircuit):
    return Statevector.from_instruction(_qc)

# Initialize stage state if not present
if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

# Stage 0: Initial button to start
if st.session_state.stage == 0:
    st.session_state.random_seed = random.randint(0, 1_000_000)
    st.button('Begin', on_click=set_state, args=[1], key="begin_button")

# Stage 1: Create the quantum circuit
if st.session_state.stage >= 1:
    num_qubits = st.slider("Number of Qubits", 2, 16, 6)
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
    all_gates = ["Hadamard/H-Gate", "Z-Gate", "X-Gate", "Y-Gate", "CX-Gate"]
    gates = st.multiselect("Gates", all_gates, default=all_gates)
    st.checkbox("Generate Additional Data", key="generate_extra")


    st.write("### Quantum Circuit with Gates:")
    rand_seed = hash(str(gates) + str(num_qubits))  # hashable input
    qc, qc_mod = get_circuit(gates, num_qubits, True, rand_seed=rand_seed)
    fig = qc.draw(output='mpl')
    st.pyplot(fig)


    # Button to go to the next stage
    st.button('Next Step', on_click=set_state, args=[3], key="next_step_2")

# Stage 3: Simulate the quantum circuit
if st.session_state.stage >= 3:
    st.write("### Simulating the Quantum Circuit:")
    circuit_hash = hash(str(qc.data))
    int_array, counts, bitstring_list = simulate_circuit(circuit_hash, qc)

    if not st.session_state.generate_extra:
        set_state(4)  # Skip to stage 4
    else:
        st.write("Measurement outcomes:", counts)
        st.write("We have", len(bitstring_list), "bitstrings in total.")
        st.write("### Converted Integer Array:")
        columns = [f"Q-Bit {i}" for i in range(int_array.shape[1])]
        df = pd.DataFrame(int_array, columns=columns)
        filtered_df = dataframe_explorer(df, case=False)
        st.dataframe(filtered_df, use_container_width=True)

        # Button to go to the next stage
        st.button('Next Step', on_click=set_state, args=[4], key="next_step_3")
# Stage 6: Visualize the results
if st.session_state.stage >= 4:                 
    tab1, tab2, tab3, tab4, tab5= st.tabs(["Full-Data", "Bloch Spehere", "Pixel-Art", "3-D Plot", "DNA"])
    with tab1:
        columns = [f"Q-Bit {i}" for i in range(int_array.shape[1])]
        df = pd.DataFrame(int_array, columns=columns)
        with chart_container(df):
            st.area_chart(df)
    with tab3:
        # Create a Seaborn heatmap
        fig, ax = plt.subplots()
        sns.heatmap(int_array, annot=False, fmt='d', cmap='coolwarm', cbar=True)
        plt.gca().axes.get_xaxis().set_visible(False)  # Hide x-axis
        plt.gca().axes.get_yaxis().set_visible(False)  # Hide y-axis
        ax.set_title("Quantum Randomness in Seaborn")
        
        st.pyplot(fig)
    with tab4:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        X, Y = np.meshgrid(np.arange(num_qubits), np.arange(num_qubits))
        ax.plot_surface(X, Y, int_array, cmap='coolwarm')
        st.pyplot(fig)
    with tab5:
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
    with tab2: 
        max_simulation_qbits = 8
        if num_qubits >max_simulation_qbits:
            st.write(f"The Bloch Sphere visualization is limited to {max_simulation_qbits} qubits for clarity/run time.")
        else:
            circuit_hash = hash(str(qc_mod.data))
            state = get_statevector_from_hash(circuit_hash, qc_mod)
            fig = plot_bloch_multivector(state)
            st.pyplot(fig)
        
      # Final instructions
        st.markdown("---")
        st.markdown("Save your circuit output as a visualization of your quantum journey!")
    # Option to start over
    st.button('Start Over', on_click=set_state, args=[0], key="start_over")