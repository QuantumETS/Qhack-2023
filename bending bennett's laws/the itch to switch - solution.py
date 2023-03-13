    # Put your code here #
    qml.CNOT(wires = ["z0", "z1"])
def reece_operator():
    """
    Quantum function corresponding to the operator to be applied by
    Reece in his qubits.This function does not return anything, 
    you must simply write the necessary gates.
    """
        # Put your code here 
    qml.CZ(wires = ["r0", "r1"])

def magic_operator():
    """
    Quantum function corresponding to the operator to be applied on the "z1"
    and "r1" qubits. This function does not return anything, you must
    simply write the necessary gates.

    """
        # Put your code here #
    qml.CNOT(wires = ["z1", "r1"])
    qml.CNOT(wires = ["r1", "z1"])
    qml.Hadamard(wires = "z1")
