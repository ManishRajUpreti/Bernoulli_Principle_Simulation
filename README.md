# Bernoulli’s Principle Simulation

This project demonstrates **Bernoulli’s Principle** using Python.  
It simulates the velocity and pressure of water flowing through a narrowing pipe.

---

## Theory

According to **Bernoulli’s equation**:

$P + \tfrac{1}{2}\rho v^2 = \text{constant}$

where:
- \( P \) = Pressure (Pa)  
- \( $\rho$ \) = Fluid density (kg/m³)  
- \( v \) = Velocity (m/s)  

As the pipe narrows:
- Velocity **increases** (from continuity equation \( A_1 v_1 = A v \)).  
- Pressure **decreases** to conserve energy.

---

## Code Features
- Uses `numpy` to compute velocity and pressure along the pipe.  
- Dual-axis plot with:
  - **Blue curve** → velocity (m/s).  
  - **Red dashed curve** → pressure (Pa).  
- Shaded regions under curves for better visualization.  
- Annotations showing starting and ending values.  

---

## How to Run
1. Clone the Repository
   ```bash
   git clone [https://github.com/manishrajupreti/Bernoulli_Principle_Simulation.git](https://github.com/manishrajupreti/Bernoulli_Principle_Simulation.git)
   cd Bernoulli_Principle_Simulation
   ```
2. Install dependencies:
   ```bash
   pip install numpy matplotlib ipywidgets
   ```
3. Run the script:
   ```bash
   python bernoulli_simulation.py
   ```
4. A plot will be displayed showing velocity rising and pressure falling along the pipe.

---

## Example Output

The plot shows:
Velocity rising from ~2 m/s to ~4 m/s.
Pressure dropping accordingly.
This demonstrates the inverse relationship between velocity and pressure predicted by Bernoulli’s principle.

---

## Requirements

- Python 3.x
- numpy
- matplotlib
