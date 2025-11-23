import math
import matplotlib.pyplot as plt
P0 = 101325  
T0 = 288.15  
g = 9.80665  
L = 0.0065  
R = 287.05   
def calculate_pressure(h):
    """Calculate atmospheric pressure according to ISA."""
    if 0 <= h <= 11000:  # Troposphere
        return P0 * (1 - (L * h / T0)) ** (g / (R * L))
    else:
        return "Altitude beyond model limit (Try 0 to 11000 m)"
def plot_pressure():
    altitudes = range(0, 11001, 500)
    pressures = [calculate_pressure(h) for h in altitudes]
    plt.plot(altitudes, pressures)
    plt.xlabel("Altitude (m)")
    plt.ylabel("Pressure (Pa)")
    plt.title("Atmospheric Pressure vs Altitude")
    plt.grid(True)
    plt.show()
try:
    h = float(input("Enter altitude in meters (0 - 11000): "))
    pressure = calculate_pressure(h)
    if isinstance(pressure, str):
        print(pressure)
    else:
        print(f"Atmospheric Pressure at {h} m = {pressure:.2f} Pa")
except ValueError:
    print("Invalid input! Enter a numeric value.")
plot_pressure()
