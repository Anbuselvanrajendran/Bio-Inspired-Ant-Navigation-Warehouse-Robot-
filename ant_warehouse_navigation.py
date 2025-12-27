import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -----------------------------
# Warehouse parameters
# -----------------------------
warehouse_size = 10
home = np.array([0.0, 0.0])              # Docking station
shelf = np.array([6.0, 7.0])             # Storage rack
step_size = 0.15

# -----------------------------
# Robot state
# -----------------------------
position = home.copy()
theta = 0.0
out_path = [position.copy()]
return_path = []
mode = "explore"
pause_counter = 0

# -----------------------------
# IMU-like motion update
# -----------------------------
def imu_step(pos, theta):
    direction_to_shelf = np.arctan2(shelf[1]-pos[1], shelf[0]-pos[0])
    theta = 0.7 * theta + 0.3 * direction_to_shelf
    theta += np.random.uniform(-0.3, 0.3)

    dx = step_size * np.cos(theta)
    dy = step_size * np.sin(theta)
    return pos + np.array([dx, dy]), theta

# -----------------------------
# Plot setup
# -----------------------------
fig, ax = plt.subplots()
ax.set_xlim(-warehouse_size, warehouse_size)
ax.set_ylim(-warehouse_size, warehouse_size)
ax.set_title("Bio-Inspired Ant Navigation (Warehouse Robot)")

ax.plot(home[0], home[1], 'go', markersize=10, label="Dock")
ax.plot(shelf[0], shelf[1], 'ks', markersize=10, label="Shelf")

robot_dot, = ax.plot([], [], 'ro', markersize=8)
out_line, = ax.plot([], [], 'b-', label="Exploration Path")
ret_line, = ax.plot([], [], 'r--', linewidth=2, label="Return Path")

ax.legend()

# -----------------------------
# Animation update
# -----------------------------
def update(frame):
    global position, theta, mode, pause_counter

    if mode == "explore":
        position, theta = imu_step(position, theta)
        out_path.append(position.copy())

        # Check shelf contact
        if np.linalg.norm(position - shelf) < 0.3:
            mode = "pause"

    elif mode == "pause":
        pause_counter += 1
        if pause_counter > 20:
            mode = "return"
            direction = home - position
            steps = int(np.linalg.norm(direction) / step_size)
            for i in range(steps):
                return_path.append(position + direction * (i / steps))

    elif mode == "return":
        if len(return_path) > 0:
            position = return_path.pop(0)

    # Update visuals
    robot_dot.set_data([position[0]], [position[1]])

    out_np = np.array(out_path)
    out_line.set_data(out_np[:, 0], out_np[:, 1])

    if len(return_path) > 0:
        ret_np = np.array(return_path)
        ret_line.set_data(ret_np[:, 0], ret_np[:, 1])

    return robot_dot, out_line, ret_line

# -----------------------------
# Run animation
# -----------------------------
ani = FuncAnimation(fig, update, frames=400, interval=50)
plt.show()
# -----------------------------
# Proof plot
# -----------------------------
out_np = np.array(out_path)

plt.figure()
plt.plot(out_np[:,0], out_np[:,1], 'b-', label="Exploration Path")
plt.plot([shelf[0]], [shelf[1]], 'ks', label="Shelf")
plt.plot([home[0]], [home[1]], 'go', label="Dock")
plt.axis('equal')
plt.title("Ant-Inspired Path Integration Proof")
plt.legend()
plt.show()
