@qml.qnode(dev)
def circuit(U):
    """This will be the circuit you will use to determine which of the two angles we have.
    Remember that only a single shot will be executed.

    Args:
        U (qml.ops): It is the gate to discriminate between  RY(2pi/3) or RY(4pi/3).

    Returns:
        (numpy.tensor): Vector of two elements representing the output measured in each of the qubits.
    """
    # Put your code here #
    # to use U,  call 'U(wires = <wire where you want to apply the gate>)'
    # to use Control-U, call 'qml.ctrl(U, control = <control wire>)(wires = <wire where you want to apply the gate>)'
    for i in range(6):
        qml.Hadamard(wires=0)
        qml.Hadamard(wires=1)
        U(wires=1)
        qml.ctrl(U, control = 0)(wires=1)
        qml.CNOT(wires=[0,1])
        qml.CNOT(wires=[1,0])
    
    return qml.sample(wires=range(2))

def process_output(measurement):
    """This function processes the output of the circuit to discriminate between gates.

    Args:
        measurement (numpy.array): Output of the previous circuit a vector of dimension 2.

    Returns:
        (int): return 2 or 4 depending on the associated RY gate.
    """
    # Put your code here #
    if measurement[0] == 1:
        return 2
    else:
        return 4