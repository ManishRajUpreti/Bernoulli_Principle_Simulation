import numpy as np
import matplotlib.pyplot as plt

# Physical constants
rho = 1000       # water density (kg/m³)
A1 = 0.02        # initial cross-sectional area (m²)

# Pipe geometry
x = np.linspace(0, 10, 100)             

def plot_bernoulli(v1, P1):
    A_pipe = np.linspace(A1, A1 / 2, 100)
    velocity = (A1 * v1) / A_pipe
    pressure = P1 + (0.5 * rho * (v1**2 - velocity**2))

    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax1.set_xlabel("Position along pipe (m)")
    ax1.set_ylabel("Velocity (m/s)", color="b")
    ax1.plot(x, velocity, "b", linewidth=2)
    ax1.tick_params(axis="y", labelcolor="b")

    ax2 = ax1.twinx()
    ax2.set_ylabel("Pressure (Pa)", color="r")
    ax2.plot(x, pressure, "r--", linewidth=2)
    ax2.tick_params(axis="y", labelcolor="r")

    plt.title("Bernoulli’s Principle: Velocity and Pressure in a Pipe")
    plt.show()

# --- User inputs ---
v1 = float(input("Enter initial velocity v1 (m/s): "))
P1 = float(input("Enter initial pressure P1 (Pa): "))

plot_bernoulli(v1, P1)
