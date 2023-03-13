    # Put your solution here #
    dev = qml.device("default.qubit", wires=len(wires))
    @qml.qnode(dev)
    def circuit(state, subsystem, wires):
        qml.QubitStateVector(state, wires=wires)
        return qml.density_matrix([0])
    
    partial_trace = circuit(state, subsystem, wires)
    dm = partial_trace.numpy()

    entropy = abs(-np.trace(np.log2(dm) * dm))

    # Check if the entropy is nan 
    if np.isnan(entropy):
        return "yes"
    else:
        return "no"