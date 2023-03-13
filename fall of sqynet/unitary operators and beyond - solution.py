def W(alpha, beta):
    """ This function returns the matrix W in terms of
    the coefficients alpha and beta

    Args:
        - alpha (float): The prefactor alpha of U in the linear combination, as in the
        challenge statement.
        - beta (float): The prefactor beta of V in the linear combination, as in the
        challenge statement.
    Returns 
        -(numpy.ndarray): A 2x2 matrix representing the operator W,
        as defined in the challenge statement
    """
    # Put your code here #
    # Return the real matrix of the unitary W, in terms of the coefficients.
    return (1/np.sqrt(alpha + beta)) * np.array([[np.sqrt(alpha), -np.sqrt(beta)], [np.sqrt(beta), np.sqrt(alpha)]])


dev = qml.device('default.qubit', wires = 2)

@qml.qnode(dev)
def linear_combination(U, V,  alpha, beta):
    """This circuit implements the circuit that probabilistically calculates the linear combination 
    of the unitaries.

    Args:
        - U (list(list(float))): A 2x2 matrix representing the single-qubit unitary operator U.
        - V (list(list(float))): A 2x2 matrix representing the single-qubit unitary operator U.
        - alpha (float): The prefactor alpha of U in the linear combination, as above.
        - beta (float): The prefactor beta of V in the linear combination, as above.

    Returns:
        -(numpy.tensor): Probabilities of measuring the computational
        basis states on the auxiliary wire. 
    """
    # Put your code here #
    # Return the probabilities on the first wire
    qml.QubitUnitary(W(alpha, beta), wires=0)


    qml.ControlledQubitUnitary(U, control_wires=[0], wires=1,control_values = "0")
    qml.ControlledQubitUnitary(V, control_wires=[0], wires=1)

    qml.adjoint(qml.QubitUnitary(W(alpha, beta), wires=0))

    return qml.probs(wires=0)