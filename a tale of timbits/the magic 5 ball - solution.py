    # Put your code here #
    n_bits = 5
    for i in range(n_bits):
        noisy_Hadamard(lmbda, i)

    qml.QubitUnitary(oracle_matrix, wires = range(5))

    for i in range(n_bits):
        noisy_Hadamard(lmbda, i)
    