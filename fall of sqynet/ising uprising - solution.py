def create_Hamiltonian(h):
    """
    Function in charge of generating the Hamiltonian of the statement.

    Args:
        h (float): magnetic field strength

    Returns:
        (qml.Hamiltonian): Hamiltonian of the statement associated to h
    """
    # Put your code here #
    obs = []
    coeffs = []

    n_sites = 4

    for i in range(n_sites):
        next = (i+1) % n_sites
        obs.append(qml.PauliZ(i) @ qml.PauliZ(next))
        coeffs.append(-1)
    
    for i in range(n_sites):
        obs.append(qml.PauliX(i))
        coeffs.append(-h)

    H = qml.Hamiltonian(coeffs = coeffs, observables = obs)

    return H

dev = qml.device("default.qubit", wires=4)

@qml.qnode(dev)
def model(params, H):
    """
    To implement VQE you need an ansatz for the candidate ground state!
    Define here the VQE ansatz in terms of some parameters (params) that
    create the candidate ground state. These parameters will
    be optimized later.

    Args:
        params (numpy.array): parameters to be used in the variational circuit
        H (qml.Hamiltonian): Hamiltonian used to calculate the expected value

    Returns:
        (float): Expected value with respect to the Hamiltonian H
    """
    # Put your code here #
    qml.RY(params[0], wires=[0])
    qml.RY(params[1], wires=[1])
    qml.RY(params[2], wires=[2])
    qml.RY(params[3], wires=[3])

    return qml.expval(H)

def train(h):
    """
    In this function you must design a subroutine that returns the
    parameters that best approximate the ground state.

    Args:
        h (float): magnetic field strength

    Returns:
        (numpy.array): parameters that best approximate the ground state.
    """
    # Put your code here #
    hamiltonian = create_Hamiltonian(h)
    theta = np.array([0.0, 0.0, 0.0, 0.0], requires_grad=True) # Initial guess parameters
    angle = [theta] # Store the values of the circuit parameter
    cost = [model(theta, hamiltonian)] # Store the values of the cost function

        
    opt = qml.GradientDescentOptimizer() # Our optimizer!
    max_iterations = 100 # Maximum number of calls to the optimizer 
    conv_tol = 1e-08 # Convergence threshold to stop our optimization procedure

    def model_2(params):
        return model(params, hamiltonian)
    
    for n in range(max_iterations):
        theta,  prev_cost = opt.step_and_cost(model_2, theta)

        angle.append(theta)
        cost.append(model(theta, hamiltonian))
        conv = abs(cost[-1] - prev_cost)

        if conv <= conv_tol:
            break
        

    return theta
# These functions are responsible for testing the solution.
def run(test_case_input: str) -> str:
    ins = json.loads(test_case_input)
    params = train(ins)
    return str(model(params, create_Hamiltonian(ins)))


def check(solution_output: str, expected_output: str) -> None:
    solution_output = json.loads(solution_output)
    expected_output = json.loads(expected_output)
    assert np.allclose(
        solution_output, expected_output, rtol=1e-1
    ), "The expected value is not correct."