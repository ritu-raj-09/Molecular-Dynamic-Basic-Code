import numpy as np
import matplotlib.pyplot as plt

m = 1.0
k = 4.0
x = 0.1
v = 0.0
dt = 0.01
steps = int(10.0 / dt)

def accel(x):
    return -k * x / m

T, X, KE, PE, TE = [], [], [], [], []

a = accel(x)
v_half = v + 0.5 * a * dt

for i in range(steps):
    t = i * dt

    T.append(t)
    X.append(x)
    KE.append(0.5 * v_half**2)
    PE.append(0.5 * k * x**2)
    TE.append(KE[-1] + PE[-1])

    # update position
    x = x + v_half * dt

    # new acceleration
    a = accel(x)

    # update velocity
    v_half = v_half + a * dt

# ---- Plot ----
plt.plot(T, X)
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.title("Mass–Spring System (Leapfrog)")
plt.grid(True)
plt.show()

# ---- Final Table ----
print("t(s)\tKE\tPE\tTotal")
for i in range(0, len(T), int(0.1/dt)):
    print(f"{T[i]:.2f}\t{KE[i]:.4f}\t{PE[i]:.4f}\t{TE[i]:.4f}")
