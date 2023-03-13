    # Put your code here #
    dev = qml.device("default.mixed", wires=range(2))
    @qml.qnode(dev)
    def circuit(U,density_matrix):
        qml.QubitDensityMatrix(density_matrix, wires=range(2))
        qml.QubitUnitary(U, wires=range(2))
        return qml.density_matrix([1])
    
    density_matrix = np.kron(rho_0,rho)
    for i in range(n_iters):
        rho = circuit(U,density_matrix)

    return rho
def apply_timbit_gate(U, rho_0, timbit):
    """
    Function that returns the output density matrix after applying a timbit gate to a state.
    The density matrix is the one associated with the first qubit.

    Args:
        U (numpy.tensor): A 2-qubit gate in matrix form.
        rho_0 (numpy.tensor): The matrix of the input density matrix.
        timbit (numpy.tensor): The timbit associated with the operator and the state.

    Returns:
        (numpy.tensor): The output density matrices.
    """
        # Put your code here #
    dev = qml.device("default.mixed", wires=range(2))
    @qml.qnode(dev)
    def circuit(U,density_matrix):
        qml.QubitDensityMatrix(density_matrix, wires=range(2))
        qml.QubitUnitary(U, wires=range(2))
        return qml.density_matrix([0])
    
    density_matrix = np.kron(rho_0,timbit)
    
    return circuit(U,density_matrix)
def SAT(U_f, q, rho, n_bits):
    """A timbit-based algorithm used to guess if a Boolean function ever outputs 1.

    Args:
        U_f (numpy.tensor): A multi-qubit gate in matrix form.
        q (int): Number of times we apply the Timbit gate.
        rho (numpy.tensor): An initial guess at the fixed point C[rho] = rho.
        n_bits (int): The number of bits the Boolean function is defined on.

    Returns:
        numpy.tensor: The measurement probabilities on the last wire.
    """
        # Put your code here #
    dev1 = qml.device("default.mixed", wires=range(n_bits))
    @qml.qnode(dev1)
    def hadamard(U_f):
        for i in range(n_bits-1):
            qml.Hadamard(wires=i)
        qml.QubitUnitary(U_f, wires=range(n_bits))
        return qml.density_matrix([3])
    
    rho_0 = hadamard(U_f)

    for i in range(q):
        timbit = calculate_timbit(U_NP,rho_0,rho,200)
        rho_0 = apply_timbit_gate(U_NP, rho_0, timbit)
        
   
    dev2 = qml.device("default.mixed", wires=range(2))
    @qml.qnode(dev2)
    def circuit(rho):
        qml.QubitDensityMatrix(rho, wires=[0])
        return qml.probs(wires=[0])
    
    circ = circuit(rho_0)
    return circ