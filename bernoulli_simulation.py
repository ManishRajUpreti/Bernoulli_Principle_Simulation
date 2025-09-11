import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from ipywidgets import interact

# Physical constants
rho = 1000       # water density (kg/m³)
A1 = 0.02        # initial cross-sectional area (m²)

# Pipe geometry
x = np.linspace(0, 10, 100)             # pipe length positions (m)
A_pipe = np.linspace(A1, A1 / 2, 100)   # cross-sectional area reduces linearly

def plot_bernoulli(v1=2.0, P1=100000.0):
    # Continuity equation: A1*v1 = A*v
    velocity = (A1 * v1) / A_pipe

    # Bernoulli’s principle: P + 0.5*rho*v² = constant
    pressure = P1 + (0.5 * rho * (v1**2 - velocity**2))

    # --- Plot ---
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Velocity curve
    ax1.set_xlabel("Position along pipe (m)")
    ax1.set_ylabel("Velocity (m/s)", color="b")
    ax1.plot(x, velocity, color="b", linewidth=2, label="Velocity")
    ax1.fill_between(x, 0, velocity, color="b", alpha=0.1)
    ax1.tick_params(axis="y", labelcolor="b")

    # Pressure curve (second y-axis)
    ax2 = ax1.twinx()
    ax2.set_ylabel("Pressure (Pa)", color="r")
    ax2.plot(x, pressure, color="r", linestyle="--", linewidth=2, label="Pressure")
    ax2.fill_between(x, pressure, min(pressure), color="r", alpha=0.1)
    ax2.tick_params(axis="y", labelcolor="r")

    # Annotations for start and end
    ax1.annotate(f"{velocity[0]:.2f} m/s", xy=(x[0], velocity[0]), xytext=(1, velocity[0]+0.5),
                 arrowprops=dict(arrowstyle="->", color="blue"), color="blue")
    ax1.annotate(f"{velocity[-1]:.2f} m/s", xy=(x[-1], velocity[-1]), xytext=(8, velocity[-1]-1),
                 arrowprops=dict(arrowstyle="->", color="blue"), color="blue")

    ax2.annotate(f"{pressure[0]:.0f} Pa", xy=(x[0], pressure[0]), xytext=(1, pressure[0]+2000),
                 arrowprops=dict(arrowstyle="->", color="red"), color="red")
    ax2.annotate(f"{pressure[-1]:.0f} Pa", xy=(x[-1], pressure[-1]), xytext=(8, pressure[-1]-3000),
                 arrowprops=dict(arrowstyle="->", color="red"), color="red")

    plt.title("Bernoulli’s Principle: Velocity and Pressure in a Pipe", fontsize=14)
    fig.tight_layout()
    plt.show()

# Interactive input boxes instead of sliders
interact(plot_bernoulli,
         v1=widgets.FloatText(value=2.0, description="Velocity v1 (m/s):"),
         P1=widgets.FloatText(value=100000.0, description="Pressure P1 (Pa):"))
