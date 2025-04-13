import streamlit as st
from qiskit import QuantumCircuit
from qiskit import transpile
from qiskit_aer import AerSimulator
import numpy as np
import matplotlib.pyplot as plt

# Set up the page
st.set_page_config(page_title="Quantum Circuit Simulation", layout="centered")
st.title("Quantum Circuit Simulation")
st.sidebar.title("Navigation")
st.sidebar.markdown("# Quantum Circuit Simulation")
st.markdown("---")
st.header("Create and Simulate a Quantum Circuit")
st.write("This app allows you to create a quantum circuit, simulate it, and visualize the results.")
st.write("You can adjust the number of qubits and see how the circuit behaves.")
st.markdown("---")

def generate_slider():
        num_qubits = st.slider(min_value=2, max_value=10, label='Select number of qubits', value=6)
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
    with st.container(border=True):
        gates = st.multiselect("Gates", all_gates, default=all_gates)
        rolling_average = st.toggle("Rolling average")

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
    shots = 64
    compiled_circuit = transpile(qc, simulator)

    result = simulator.run(compiled_circuit, shots=shots).result()
    counts = result.get_counts()
    st.write("Measurement outcomes:", counts)

    # Button to go to the next stage
    st.button('Next Step', on_click=set_state, args=[4], key="next_step_3")

# Stage 4: Process and display bitstrings
if st.session_state.stage >= 4:
    bitstring_list = []
    for bitstring, cnt in counts.items():
        bitstring_list.extend([bitstring] * cnt)

    st.write("We have", len(bitstring_list), "bitstrings in total.")

    # Button to go to the next stage
    st.button('Next Step', on_click=set_state, args=[5], key="next_step_4")

# Stage 5: Convert to integer array and display
if st.session_state.stage >= 5:
    int_values = []
    for bs in bitstring_list:
        value = int(bs, 2)
        int_values.append(value)

    int_array = np.array(int_values).reshape(8, 8)  # Reshaping to 8x8
    st.write("### Converted Integer Array:")
    st.write(int_array)

    # Button to go to the next stage
    st.button('Next Step', on_click=set_state, args=[6], key="next_step_5")

# Stage 6: Visualize the results
if st.session_state.stage >= 6:
    # Create the plot
    fig, ax = plt.subplots()
    ax.imshow(int_array, cmap='hot')
    ax.set_title("Quantum Randomness in Grayscale")
    ax.axis('off')  # Hide the axis

    # Display the plot in Streamlit
    st.pyplot(fig)

    # Option to start over
    st.button('Start Over', on_click=set_state, args=[0], key="start_over")

    # Final instructions or explanation
    st.write(
        """
        This circuit applies a Hadamard gate to each qubit, then applies
        CNOT gates between pairs of qubits. Finally, it measures the qubits.
        You can experiment by changing the number of qubits or gates!
        """
    )
