# wave_equation_greens_function
Python project to solve the wave equation using Green's function
# Wave Equation Solver using Green's Function

This Python project solves the 1D wave equation using Green's function. The Green's function is implemented to compute the solution for a given initial condition, which is defined as a Gaussian pulse in this example.

## Overview

The wave equation is a fundamental partial differential equation (PDE) that describes the behavior of waves, such as sound waves, light waves, or water waves. Green's function provides a method to solve PDEs by expressing the solution in terms of an integral involving the initial conditions.

In this project, we:
- Define a `GreensFunction` class to compute the Green's function for the wave equation.
- Use the Green's function to solve the wave equation over a given domain.
- Plot the solution of the wave equation at specific times using `matplotlib`.

## Prerequisites

Ensure you have Python installed. This project also requires the following Python libraries:

- `numpy`: For numerical computations.
- `matplotlib`: For plotting the results.

To install these dependencies, run:
```bash
pip install numpy matplotlib
