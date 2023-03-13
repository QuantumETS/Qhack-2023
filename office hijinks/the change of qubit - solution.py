def circuit_left():
    """
    This function corresponds to the circuit on the left-hand side of the diagram in the 
    description. Simply place the necessary operations, you do not have to return anything.
    """
    qml.CNOT(wires=[0,1])

    qml.SWAP(wires=[0,1])
    qml.CNOT(wires=[1,2])
    qml.SWAP(wires=[0,1])
    

def circuit_right():
    """
    This function corresponds to the circuit on the right-hand side of the diagram in the 
    description. Simply place the necessary operations, you do not have to return anything.
    """
    qml.CNOT(wires=[0,1])

    qml.SWAP(wires=[0,1])
    qml.CNOT(wires=[1,2])
    qml.SWAP(wires=[0,1])

    # Toffoli gate using cnot, H and T gates
    def toffoli(q0, q1,q2):
        qml.Hadamard(wires=q2)

        qml.CNOT(wires=[q1,q2])

        qml.adjoint(qml.T)(wires=q2)

        qml.SWAP(wires=[q0,q1])
        qml.CNOT(wires=[q1,q2])
        qml.SWAP(wires=[q0,q1])

        qml.T(wires=q2)

        qml.CNOT(wires=[q1,q2])

        qml.adjoint(qml.T)(wires=q2)

        qml.SWAP(wires=[q0,q1])
        qml.CNOT(wires=[q1,q2])
        qml.SWAP(wires=[q0,q1])

        qml.T(wires=q1)
        qml.T(wires=q2)

        qml.Hadamard(wires=q2)
        qml.CNOT(wires=[q0,q1])

        qml.T(wires=q0)
        qml.adjoint(qml.T)(wires=q1)

        qml.CNOT(wires=[q0,q1])

    toffoli(2,1,0)
    qml.SWAP(wires=[0,1])
    qml.SWAP(wires=[1,2])