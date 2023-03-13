@qml.qnode(dev)
def time(hour, minute):
    """Generates the quantum state associated with the time passed as argument.

    Args:
        hour (int): Hour associated with the requested time
        minute (int): Minutes associated with the requested time

    Returns:
        (numpy.tensor): Probabilities associated with the state created.
    """
    # Put your code here #
    for i in range(hour):
        qml.RX(np.pi/6, wires="hour")
    
    for i in range(minute):
        qml.RX(np.pi/30, wires="minute")
        
    return qml.probs(wires=["hour", "minute"])