    # Put your code here #
    # Apply the error
    qml.CNOT(wires=[0, 3])
    qml.CNOT(wires=[0, 6])
    qml.Hadamard(wires=0)
    qml.Hadamard(wires=3)
    qml.Hadamard(wires=6)

    qml.CNOT(wires=[0, 1])
    qml.CNOT(wires=[0, 2])

    qml.CNOT(wires=[3, 4])
    qml.CNOT(wires=[3, 5])

    qml.CNOT(wires=[6, 7])
    qml.CNOT(wires=[6, 8])

    error(error_key, qubit)

    qml.CNOT(wires=[0, 1])
    qml.CNOT(wires=[0, 2])
    qml.Toffoli(wires=[2, 1, 0])

    qml.CNOT(wires=[3, 4])
    qml.CNOT(wires=[3, 5])
    qml.Toffoli(wires=[5, 4, 3])

    qml.CNOT(wires=[6, 7])
    qml.CNOT(wires=[6, 8])
    qml.Toffoli(wires=[8, 7, 6])

    qml.Hadamard(wires=0)
    qml.Hadamard(wires=3)
    qml.Hadamard(wires=6)

    qml.CNOT(wires=[0, 3])
    qml.CNOT(wires=[0, 6])
    qml.Toffoli(wires=[6, 3, 0])

    return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]