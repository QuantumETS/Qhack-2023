        # Put your code here #
        # noisy_PauliX(0,lmbda)
        # noisy_PauliX(1,lmbda)
        # noisy_PauliX(4,lmbda)

        noisy_PauliX(2,lmbda)
        noisy_PauliX(3,lmbda)
        Toffoli_cascade([0,1,2,3,4],[5,6,7,8],lmbda)
        return qml.probs(wires=8)

    output = circuit()

    # if you want to post-process the output, put code here also #

    return output[1]