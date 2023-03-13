def bell_preparation(wires):
    """
    Quantum function in charge of generating the bell state of 4 qubits.
    You simply add the necessary gates, do not return anything.

    Args:
        wires (list(str)): list of the 4 wires where the gate will run

    """
    qml.Hadamard(wires=wires[0])
    for i in range(1, len(wires)):
        qml.CNOT(wires=[wires[0], wires[i]])

def emergency_gate_U(wire):
    """
    Quantum function that will define the emergency protocol in a qubit.
    You simply add the necessary gates, do not return anything.

    Args:
        wire(str): name of the wire where the emergency gate will be apply.

    """
    qml.Hadamard(wires=wire)

def setting_new_robot(output, wires):
    """
    Quantum function that defines the operation between the hub and the auxiliary robot.

    Args:
        output (int): 0 or 1, indicates the measurement output of robot1 after collapsing.
                    Take a look at qml.cond to see how to condition operators to this value.

        wires(list(str)): name of the wires where the gate will be apply.

    """
    qml.CNOT(wires=['hub','auxiliary_robot'])
    qml.cond(output, qml.CZ)(wires=['hub','auxiliary_robot'])