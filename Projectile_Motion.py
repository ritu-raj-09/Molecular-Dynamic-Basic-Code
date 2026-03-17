import numpy as np
import matplotlib.pyplot as plt
import math

g = 9.8
y = 20.0
x = 0.0
v0 = 10.0
angle = math.radians(30)

vx = v0 * math.cos(angle)
vy = v0 * math.sin(angle)

dt = 0.01

ax = 0.0
ay = -g

vx_half = vx + 0.5 * ax * dt
vy_half = vy + 0.5 * ay * dt

T, Y, KE, PE, TE = [], [], [], [], []

for i in range(100000):
    t = i * dt

    T.append(t)
    Y.append(y)
    KE.append(0.5 * (vx_half**2 + vy_half**2))
    PE.append(g * y)
    TE.append(KE[-1] + PE[-1])

    # update positions
    x = x + vx_half * dt
    y = y + vy_half * dt

    if y <= 0:
        break

    # acceleration
    ax = 0.0
    ay = -g

    # update velocities
    vx_half = vx_half + ax * dt
    vy_half = vy_half + ay * dt

# ---- Plot ----
plt.plot(T, Y)
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Projectile Motion (Leapfrog)")
plt.grid(True)
plt.show()

# ---- Final Table ----
print("t(s)\tKE\tPE\tTotal")
for i in range(0, len(T), int(0.1/dt)):
    print(f"{T[i]:.2f}\t{KE[i]:.4f}\t{PE[i]:.4f}\t{TE[i]:.4f}")
