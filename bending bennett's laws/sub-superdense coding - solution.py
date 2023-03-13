    # Put your code here #
    # convert i,j and k to dicimal
    decimal = i*4 + j*2 + k

    #print(decimal)
    if decimal == 1:
        qml.PauliX(wires=0)
        qml.PauliX(wires=1)
    elif decimal == 2:
        qml.PauliX(wires=1)
    elif decimal == 3:
        qml.PauliX(wires=0)
    elif decimal == 4:
        qml.PauliZ(wires=0)
    elif decimal == 5:
        qml.PauliZ(wires=0)
        qml.PauliX(wires=0)
        qml.PauliX(wires=1)
    elif decimal == 6:
        qml.PauliZ(wires=0)
        qml.PauliX(wires=1)
    elif decimal == 7:
        qml.PauliZ(wires=0)
        qml.PauliX(wires=0)
def decode():
    """
    Quantum decoding function. It can act on the three qubits.
    This function does not return anything, it simply applies gates.
    """
    # Put your code here #
    qml.CNOT(wires=[0,2])
    qml.CNOT(wires=[0,1])
    qml.Hadamard(wires=0)