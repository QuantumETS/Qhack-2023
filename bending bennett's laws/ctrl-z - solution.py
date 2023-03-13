    # Put your code here #
    qml.Toffoli(wires=[1,2,0])
    qml.ctrl(qml.PauliZ, control =[0, 1])(wires = [2])
    # Your code here #

    return qml.probs(wires=0)