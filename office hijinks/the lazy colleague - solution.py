@qml.qnode(dev)
def circuit(project_execution):
    """This is the circuit we will use to detect which is the lazy worker. Remember 
    that we will only execute one shot.

    Args:
        project_execution (qml.ops): 
            The gate in charge of marking in the last qubit if the project has been finished
            as indicated in the statement.

    Returns:
        (numpy.tensor): Measurement output in the 5 qubits after a shot.
    """
    # Put your code here #
    state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    state[28] = 0.5
    state[26] = 0.5
    state[22] = 0.5
    state[14] = 0.5
    qml.AmplitudeEmbedding(state, wires = wires)

    
    qml.PauliX(wires='result')
    qml.Hadamard(wires='result')
    project_execution(wires=wires)
    qml.Hadamard(wires='result')
    qml.PauliX(wires='result')

    qml.PauliX(wires='e1')
    qml.PauliX(wires='e2')
    qml.PauliX(wires='e3')
    qml.PauliX(wires='e4')

    qml.CNOT(wires=['e4', 'e1'])
    qml.CNOT(wires=['e4', 'e2'])
    qml.MultiControlledX(control_wires=['e1', 'e2'], wires='e4')

    qml.MultiControlledX(control_wires=['e1', 'e2',"e4"], wires='e3', control_values="000")
    

    # Use CZ and Hadamard to get the phase of the correct state
    qml.CZ(wires=['e1', 'e2'])
    qml.Hadamard(wires='e1')
    qml.Hadamard(wires='e2')
    # Put your code here #
    return qml.sample(wires=dev.wires)

def process_output(measurement):
    """This function will take the circuit measurement and process it to determine who is the lazy worker.

    Args:
        measurement (numpy.tensor): Measurement output in the 5 qubits after a shot.

    Returns:
        (str): This function must return "e1", "e2" "e3" or "e4" - the lazy worker.
    """
    # Put your code here #
    if measurement[0] and measurement[1]:
        return "e3"
    elif measurement[0] and not measurement[1]:
        return "e1"
    elif not measurement[0] and measurement[1]:
        return "e2"
    else:
        return "e4"
