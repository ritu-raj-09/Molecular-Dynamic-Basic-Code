import numpy as np
import matplotlib.pyplot as plt

g = 9.8
y = 1.50
v = 0.0
dt = 0.001
steps = int(3.0 / dt)

T, Y, KE, PE, TE = [], [], [], [], []

a = -g
v_half = v + 0.5 * a * dt

for i in range(steps):
    t = i * dt

    # store energies
    T.append(t)
    Y.append(y)
    KE.append(0.5 * v_half**2)
    PE.append(g * y)
    TE.append(KE[-1] + PE[-1])

    # update position
    y = y + v_half * dt

    # bounce
    if y < 0:
        y = -y
        v_half = -v_half

    # acceleration
    a = -g

    # update velocity
    v_half = v_half + a * dt

# ---- Plot ----
plt.plot(T, Y)
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Bouncing Ball (Leapfrog)")
plt.grid(True)
plt.show()

# ---- Final Table ----
print("t(s)\tKE\tPE\tTotal")
for i in range(0, len(T), int(0.1/dt)):
    print(f"{T[i]:.2f}\t{KE[i]:.4f}\t{PE[i]:.4f}\t{TE[i]:.4f}")
