    # Put your code here #
    dev = qml.device('default.qubit', wires = 2)

    def U_dagger(theta):
        qml.CRZ(theta, wires = [0,1])
        qml.CRX(theta, wires = [0,1])
        qml.Hadamard(wires = 0)

    @qml.qnode(dev)
    def circuit(theta):
        """
        Quantum circuit that encodes the state and performs the measurement.

        Args:
            alpha (float): parameter used to encode the state.
            beta (float): parameter used to encode the state.

        Returns:
            (float): probability of measuring the state |0>.

        """
        U_psi(theta)

        for i in range(2):
            qml.RZ(alpha,i)
            qml.RX(beta,i)
        
        U_dagger(theta)

        return qml.probs(wires = range(2))


    # Put your code here #

    is_unsafe = False

    # Return the probabilities on the first wire
    for theta in np.linspace(0, 2*np.pi, 100):
        prob = circuit(theta)
        if prob[0] >= 1 - epsilon:
            is_unsafe = True
            break

    return is_unsafe