def half_life(gamma, p):
    """Calculates the relaxation half-life of a quantum system that exchanges energy with its environment.
    This process is modeled via Generalized Amplitude Damping.

    Args:
        gamma (float): 
            The probability per unit time of the system losing a quantum of energy
            to the environment.
        p (float): The de-excitation probability due to environmental effect

    Returns:
        (float): The relaxation haf-life of the system, as explained in the problem statement.
    """

    num_wires = 1

    dev = qml.device("default.mixed", wires=num_wires)
        # Feel free to write helper functions or global variables here

    @qml.qnode(dev)
    def noise(
        gamma,
        time,  # add optional parameters, delete if you don't need any
    ):
        """Implement the sequence of Generalized Amplitude Damping channels in this QNode
        You may pass instead of return if you solved this problem analytically, it's possible!

        Args:
            gamma (float): The probability per unit time of the system losing a quantum of energy
            to the environment.
        
        Returns:
            (float): The relaxation half-life.
        """
        # Don't forget to initialize the state
        # Put your code here #
        delta_t = 0.01

        qml.Hadamard(wires=0)

        for i in range(int(time/delta_t)):
            qml.GeneralizedAmplitudeDamping(gamma*delta_t, p, wires=0)
            

        # Return something or pass if you solved this analytically!
        return qml.probs(wires=0)

    # Write any subroutines you may need to find the relaxation time here
    time = 0
    probability = 1/4
    max_ecart = 20

    for i in range(0,10000):
        prob_1 = noise(gamma, i/10)[1]
        time = i/10
        if abs(prob_1 - probability) < max_ecart:
            max_ecart = abs(prob_1 - probability)
        else:
            break

    print(time)

    return time