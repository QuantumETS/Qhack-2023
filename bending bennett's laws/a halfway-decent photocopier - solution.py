    # Put your code here #
    qml.CNOT(wires = ["z0", "z1"])
    qml.Hadamard(wires = "z0")
def copier():
    """
    Quantum function encoding the copy operation cone by Zenda, on each qubit.
    This function does not return anything, you must simply write the necessary gates.
    """
        # Put your code here #
    qml.CNOT(wires = ["z0", "s0"])
    qml.CNOT(wires = ["z1", "s1"])
def printer():
    """
    Quantum function encoding the print operation done by Reece's printer.
    This function does not return anything, you must simply write the necessary gates.
    """
        # Put your code here #
    qml.CNOT(wires = ["s0", "r1"])
    qml.CNOT(wires = ["s1", "r1"])