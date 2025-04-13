import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠", layout="centered")


if "page" not in st.session_state:
    st.session_state.page = "home"

def nav_bar(active):
    pages = {
        "qubits": "Qubits :bulb:",
        "superposition": "Superposition :arrows_counterclockwise:",
        "entanglement": "Entanglement :link:",
        "home": "Home :house:"
    }
    labels = [k for k in pages if k != active]  
    cols = st.columns(len(labels))
    for col, key in zip(cols, labels):
        if col.button(pages[key]):
            st.session_state.page = key
            st.rerun()

page = st.session_state.page

if page == "home":
    st.title("Home :house:")
    st.markdown("---")
    st.header("*Welcome!* :wave:")
    st.write("This is a simple web app to help you explore quantum concepts and their significance. Please use the buttons below to navigate. :blush:")
    st.markdown("---")
    st.header("*Why Quantum?* :thinking_face:")
    st.write("Quantum computing is revolutionizing how we solve complex problems by unlocking computational power far beyond classical limits — enabling breakthroughs in areas like drug discovery, where it can simulate molecules too complex for today’s supercomputers; cybersecurity, where it challenges current encryption and pushes the development of quantum-safe cryptography; and global logistics, where it can optimize routes and supply chains faster and more efficiently than ever before.")
    st.markdown("---")
    st.header("*Check Out Other Quantum Concepts* :fire:")
    nav_bar("home")
    st.caption("*Please scroll to the top of the page after selecting a topic*")
    st.markdown("---")

elif page == "qubits":
    st.title("Qubits :bulb:")
    st.markdown("---")

    st.header("What is a Qubit?")
    st.write("""
    A **qubit** (quantum bit) is the basic unit of information in quantum computing — just like a bit in classical computing.
    But while a classical bit can only be **0 or 1**, a qubit can be **both at the same time**, thanks to quantum superpowers.
    """)

    st.header("Classical Bit vs Quantum Bit")
    st.markdown("""
    | Classical Bit | Quantum Bit (Qubit) |
    |---------------|----------------------|
    | `0` or `1` only | **Superposition** of `0` and `1` |
    | On/off like a light switch | Like a spinning coin — both at once |
    """, unsafe_allow_html=True)

    st.header("Key Properties of Qubits")

    with st.expander("🌀 Superposition"):
        st.markdown("""
        Superposition means a qubit can be in a mix of both `|0⟩` and `|1⟩` until you measure it.

     > Imagine a coin spinning mid-air — it's not just heads or tails, it's both!
        """)

    with st.expander("🔗 Entanglement"):
        st.markdown("""
    When two qubits are **entangled**, changing one instantly affects the other — even if they’re far apart.

    > Like two magical dice: roll one, and the other matches every time.
    """)

    with st.expander("📏 Measurement"):
        st.markdown("""
    Once you measure a qubit, it **collapses** to either `0` or `1`. You lose the superposition.

    > Observation changes the outcome.
    """)

    st.markdown("---")

    st.header("🧭 Visualizing Qubits: The Bloch Sphere")
    st.write("""
    Qubits are often represented on a 3D sphere called the **Bloch Sphere**, where:

    - North pole = `|0⟩`
    - South pole = `|1⟩`
    - Any other point = a quantum state (mix of `0` and `1`)
    """)

    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Bloch_sphere.svg/500px-Bloch_sphere.svg.png", 
         caption="The Bloch Sphere — a 3D way to visualize a qubit", 
         use_container_width=True)


    st.markdown("---")

    st.header("🧪 How Are Qubits Built?")
    st.write("""
Physical implementations of qubits include:

- Superconducting circuits (used by IBM, Google)
- Trapped ions
- Photons (light particles)
- Topological qubits (experimental)

These require extreme precision and isolation, often at near absolute-zero temperatures.
""")

    st.markdown("---")

    st.header("📌 Summary")
    st.markdown("""
    - **Qubits** can store much more than just `0` or `1`
    - They enable quantum computers to tackle problems classical computers can't
    - Understanding qubits is the first step to understanding quantum computing!

    ---  
    """)

    st.success("Next up: Try exploring Superposition or Entanglement!")
    nav_bar("qubits")
    st.caption("*Please scroll to the top of the page after selecting a topic*")
    st.markdown("---")

elif page == "superposition":
    st.title("Superposition :arrows_counterclockwise:")

    st.markdown("---")

    st.header("What is Superposition?")
    st.write("""
    Superposition is one of the most fundamental concepts in quantum computing.

    In classical computing, a bit is either `0` or `1`. But a **qubit** in superposition can be **both 0 and 1 at the same time** — until it is measured.
    """)

    st.markdown("""
    > 🎯 Think of a coin spinning in the air — it's not heads or tails until it lands.  
    > In the same way, a qubit in superposition doesn’t commit to `0` or `1` until we measure it.
    """)

    st.markdown("---")

    st.header("Superposition in Action")

    with st.expander("⚙️ How It Works Mathematically"):
        st.markdown("""
        A qubit's state can be written as a combination (or superposition) of the basis states:

        ```
        |ψ⟩ = α|0⟩ + β|1⟩
        ```

        - `|ψ⟩` is the qubit's quantum state
        - `α` and `β` are complex numbers called **amplitudes**
        - The probabilities of measuring `0` or `1` are given by `|α|²` and `|β|²`
        - The total probability must always add up to 1:
        ```
         |α|² + |β|² = 1
         ```
        """)

    with st.expander("🔬 What Happens When We Measure?"):
        st.markdown("""
        When a qubit is in superposition, it **collapses** to either `0` or `1` when you measure it.

        - If `|α|² = 0.6`, there's a 60% chance you'll get `0`
        - If `|β|² = 0.4`, there's a 40% chance you'll get `1`

        > 🧠 Before measuring, the qubit is **both**. After measuring, it's **one or the other**.
        """)

    st.markdown("---")

    st.header("🧭 Visualizing Superposition")

    st.write("""
    The **Bloch Sphere** is a 3D model used to represent a qubit's state. Superposition lives along the surface — not just at the poles (0 or 1).
    """)

    st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Bloch_sphere.svg/500px-Bloch_sphere.svg.png",
    caption="A qubit in superposition is a point between |0⟩ and |1⟩ on the Bloch Sphere",
    use_container_width=True
    )

    st.markdown("---")

    st.header("🌐 Why Superposition Matters")

    st.write("""
    Superposition gives quantum computers their **massive parallelism** — they can explore many possible states at once.

    This makes them powerful for tasks like:
    - Searching unsorted data (e.g., Grover’s algorithm)
    - Simulating quantum systems
    - Exploring large optimization spaces
    """)

    st.write("Superposition is the magic behind a qubit's flexibility — and the starting point for quantum power.")

    st.markdown("---")
    st.success("Next up: Try exploring Entanglement or Qubits!")
    nav_bar("superposition")
    st.caption("*Please scroll to the top of the page after selecting a topic*")
    st.markdown("---")

elif page == "entanglement":
    st.title("Entanglement :link:")
    st.markdown("---")

    st.header("What is Entanglement?")
    st.write("""
    **Entanglement** is one of the most mind-blowing principles in quantum physics.

    It refers to a special connection between two or more qubits, such that the state of one **instantly affects** the state of the other — no matter how far apart they are.
    """)

    st.markdown("""
    > ✨ Einstein called it “spooky action at a distance.”  
    > Once two qubits are entangled, they become part of a **shared state**.
    """)

    st.markdown("---")

    st.header("How It Works")

    with st.expander("⚛️ An Entangled Pair"):
        st.markdown("""
    Consider two qubits in this entangled state:

    ```
    |ψ⟩ = 1/√2 (|00⟩ + |11⟩)
    ```

    This means:
    - There's a 50% chance of measuring `00`
    - A 50% chance of measuring `11`
    - But never `01` or `10`

    > Once you measure the first qubit and get `0`, the second **must** be `0` too — even if it's light-years away.
    """)

    with st.expander("🧪 Why This is Different from Classical Correlation"):
        st.markdown("""
    Classical systems can be correlated (e.g., two coins both set to heads), but entanglement is deeper:

    - It's not just that the outcomes match
    - It's that the outcomes **don't exist until measured**, and yet still stay perfectly correlated

    > The measurement of one qubit **determines** the state of the other — instantly.
    """)

    st.markdown("---")

    st.header("🔬 Visualizing Entanglement")

    st.write("""
    Entangled states **can’t be described independently**. They must be treated as a single, inseparable system.

    Imagine two spinning coins that always land on the same side — no matter how far apart they are. That’s the core intuition.
    """)

    st.header("📸 A Simple Visual of Entangled Qubits")

    st.image(
    "https://cdn.pixabay.com/photo/2020/11/22/08/37/quantum-physics-5762950_1280.jpg",
    caption="Artistic visualization of quantum entanglement — two particles sharing a quantum connection.",
    use_container_width=True
    )




    st.markdown("---")

    st.header("🌐 Why Entanglement Matters")

    st.write("""
    Entanglement is the key to:

    - **Quantum teleportation** — transferring qubit states across space
    - **Quantum cryptography** — enabling ultra-secure communication
    - **Quantum error correction** — preserving data in noisy environments
    - **Quantum speedups** — used in algorithms like Shor’s and Grover’s

    It's one of the most powerful and mysterious tools in quantum computing.
    """)

    st.write("Entanglement links qubits in a way that defies classical logic — and powers quantum technologies we’re only beginning to explore.")

    st.markdown("---")
    st.success("Next up: Try exploring Qubits or Superposition!")
    nav_bar("entanglement")
    st.caption("*Please scroll to the top of the page after selecting a topic*")
    st.markdown("---")
