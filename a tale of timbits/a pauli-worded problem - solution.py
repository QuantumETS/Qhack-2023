    # Put your code here #
    pauli_word = qml.pauli.string_to_pauli_word(word)
    print(pauli_word)
    matrix = (qml.pauli.pauli_word_to_matrix(pauli_word)+np.identity(2**word_dist(word)))/2**word_dist(word)
    qml.QubitDensityMatrix(matrix, wires=range(word_dist(word)))
    for i in range(word_dist(word)):
        # if word[i] == 'I':
        #     qml.Identity(wires=i)
        # elif word[i] == 'X':
        #     qml.PauliX(wires=i)
        # elif word[i] == 'Y':
        #     qml.PauliY(wires=i)
        # elif word[i] == 'Z':
        #     qml.PauliZ(wires=i)
        qml.DepolarizingChannel(lmbda,wires=i)
# Compute the trace distance from a noisy Pauli density to the maximally mixed density

def maxmix_trace_dist(word, lmbda):
    """
       A function compute the trace distance between a noisy density matrix, specified
       by a Pauli word, and the maximally mixed matrix.

    Args:
            word (str): A Pauli word represented as a string with characters I, X, Y and Z.
            lmbda (float): The probability of replacing a qubit with something random.

    Returns:
            float: The trace distance between two matrices encoding Pauli words.
    """
    dev = qml.device("default.mixed", wires=word_dist(word))
    @qml.qnode(dev)
    def circuit():
        noisy_Pauli_density(word,lmbda)
        return qml.state()#qml.density_matrix(wires=range(len(word)))#
        
    rho = circuit()

    rho_matrix = circuit()

    sigma = np.identity(2**word_dist(word))/(2**word_dist(word))


    result = abs_dist(rho,sigma)

    Trhop = 0.5*np.trace(result)

    return Trhop
def bound_verifier(word, lmbda):
    """
       A simple check function which verifies the trace distance from a noisy Pauli density
       to the maximally mixed matrix is bounded by (1 - lambda)^|P|.

    Args:
            word (str): A Pauli word represented as a string with characters I, X, Y and Z.
            lmbda (float): The probability of replacing a qubit with something random.

    Returns:
            float: The difference between (1 - lambda)^|P| and T(rho_P(lambda), rho_0).
    """
    # Put your code here #
    abs_p = word_dist(word)

    # Put your code here #
    return (1 - lmbda)**abs_p - maxmix_trace_dist(word, lmbda)