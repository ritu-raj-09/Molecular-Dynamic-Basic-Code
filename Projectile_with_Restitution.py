import numpy as np
import matplotlib.pyplot as plt
import math

# parameters
g = 9.8
b = 0.05
m = 1.0
dt = 0.01
e = 0.85   # restitution

# initial conditions
y0 = 20.0
v0 = 10.0
angle = math.radians(30)
vx0 = v0 * math.cos(angle)
vy0 = v0 * math.sin(angle)

def simulate(with_drag):
    x = 0.0
    y = y0
    vx = vx0
    vy = vy0

    T = []
    X = []
    Y = []

    # accelerations
    if with_drag:
        ax = -(b/m)*vx
        ay = -g - (b/m)*vy
    else:
        ax = 0.0
        ay = -g

    # half-step velocities
    vx_half = vx + 0.5 * ax * dt
    vy_half = vy + 0.5 * ay * dt

    for i in range(20000):
        t = i * dt

        T.append(t)
        X.append(x)
        Y.append(y)

        # update positions
        x = x + vx_half * dt
        y = y + vy_half * dt

        # bounce
        if y <= 0:
            y = 0
            vy_half = -e * vy_half

        # accelerations
        if with_drag:
            ax = -(b/m)*vx_half
            ay = -g - (b/m)*vy_half
        else:
            ax = 0.0
            ay = -g

        # update velocities
        vx_half = vx_half + ax * dt
        vy_half = vy_half + ay * dt

        if y <= 0 and vy_half < 0:
            break

    return X, Y

# simulate both cases
X_no_drag, Y_no_drag = simulate(False)
X_drag,    Y_drag    = simulate(True)

# ---- Plot trajectories ----
plt.plot(X_no_drag, Y_no_drag, label="No Drag")
plt.plot(X_drag,    Y_drag,    label="With Drag")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Projectile Motion with Restitution and Drag")
plt.legend()
plt.grid(True)
plt.show()
