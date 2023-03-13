@qml.qnode(dev)
def model(alpha):
    """In this qnode you will define your model in such a way that there is a single 
    parameter alpha which returns each of the basic states.

    Args:
        alpha (float): The only parameter of the model.

    Returns:
        (numpy.tensor): The probability vector of the resulting quantum state.
    """
    # Put your code here #
    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)

    def add_k_fourier(k, wires):
        for j in range(len(wires)):
            qml.RZ(k * np.pi / (2**j), wires=wires[j])
    

    add_k_fourier(alpha, range(3)) 
    qml.adjoint(qml.QFT)(wires=range(3))
    
    return qml.probs(wires=range(3))

def generate_coefficients():
    """This function must return a list of 8 different values of the parameter that
    generate the states 000, 001, 010, ..., 111, respectively, with your ansatz.

    Returns:
        (list(int)): A list of eight real numbers.
    """
    # Put your code here #

    return [0,1,2,3,4,5,6,7]