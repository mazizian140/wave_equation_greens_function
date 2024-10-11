import numpy as np
import matplotlib.pyplot as plt


# Define the Green's function class
class GreensFunction:
    def __init__(self, c):
        """Initialize with wave speed c."""
        self.c = c

    def greens_function(self, x, t):
        """
        Green's function for the wave equation.
        G(x,t) = (1/(2c)) * H(t - |x|/c), where H is the Heaviside function.
        """
        return (1 / (2 * self.c)) * np.heaviside(t - np.abs(x) / self.c, 1)

    def solve_wave_equation(self, x, t, f):
        """
        Solves the wave equation using Green's function.

        Parameters:
        x : numpy array of spatial points
        t : numpy array of time points
        f : initial condition function
        """
        solution = np.zeros_like(x)

        for i, x_i in enumerate(x):
            for j, t_j in enumerate(t):
                solution[i] += self.greens_function(x_i, t_j) * f(x_i)

        return solution


# Define a function for initial condition (e.g., a Gaussian pulse)
def initial_condition(x):
    return np.exp(-x ** 2)


# Define the main function
def main():
    # Set up parameters
    c = 1.0  # Wave speed
    x = np.linspace(-5, 5, 100)  # Spatial domain
    t = np.linspace(0, 5, 100)  # Time domain

    # Initialize Green's function solver
    green_solver = GreensFunction(c)

    # Solve the wave equation
    solution = green_solver.solve_wave_equation(x, t, initial_condition)

    # Plot the solution
    plt.plot(x, solution, label="Wave at t=5")
    plt.title("Wave Equation Solution using Green's Function")
    plt.xlabel("x")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.show()


# Run the main function
if __name__ == "__main__":
    main()


