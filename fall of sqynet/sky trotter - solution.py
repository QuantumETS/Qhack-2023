    # Put your code here #
    for d in range(depth):
        # Ising interaction between qubits
        qml.IsingXX(time*alpha*2/(depth), wires=[0, 1])
        #qml.IsingYY(time*beta/(depth), wires=[0, 1])
    # Return the probabilities
    return qml.probs(wires=[0, 1])
    # Return the probabilities