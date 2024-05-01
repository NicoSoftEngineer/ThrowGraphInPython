#To run this program run this in cmd
'''
python -m venv venv
.\venv\Scripts\activate
pip install matplotlib
python throw_graph.py
'''

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# Create the main window
root = tk.Tk()
max_height = 0.0
total_time = 0.0

def create_graph():
    initial_speed_value = float(initialSpeed.get())
    initial_height_value = float(initialHeight.get())
    initial_angle_value = float(initialAngle.get())
    g = float(gravity.get())

    # Convert launch angle to radians
    theta_radians = np.deg2rad(initial_angle_value)

    # Calculate time of flight
    t_max = (initial_speed_value * np.sin(theta_radians) +
             np.sqrt((initial_speed_value * np.sin(theta_radians)) ** 2 + 2 * g * initial_height_value)) / g

    # Time array
    t = np.linspace(0, t_max, 100)

    # Calculate horizontal and vertical positions
    x = initial_speed_value * np.cos(theta_radians) * t
    y = initial_height_value + initial_speed_value * np.sin(theta_radians) * t - 0.5 * g * t ** 2

    # Adjust y to start from initial_height
    y = np.maximum(y, 0)

    # Set x and y limits
    ax.set_xlim(left=min(x), right=max(x) + 5)
    ax.set_ylim(bottom=min(y), top=max(y) + 10)

    # Update x and y data
    line.set_xdata(x)
    line.set_ydata(y)
    print(np.count_nonzero(y) / 5)
    print(np.max(y) * 0.2)

    # Set x and y tick intervals and formats
    ax.xaxis.set_major_locator(ticker.MultipleLocator(np.max(x) * 0.15))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(np.max(y) * 0.15))
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.0f}"))
    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.0f}"))

    # Recalculate limits and autoscale
    ax.relim()
    ax.autoscale_view()

    # Redraw the canvas
    canvas.draw()

    # Update labels
    max_height_label.config(text=f'Max height:{round(max(y))}')
    total_time_label.config(text=f'Total time in air:{round(t_max)}')
    throw_length_label.config(text=f'Throw length:{round(max(x))}')


# Set the ui
root.title("Throw Graph")
label = tk.Label(root, text="Initial velocity [m/s]")
label.pack()
initialSpeed = tk.Entry(root)
initialSpeed.pack()
label = tk.Label(root, text="Initial height [m]")
label.pack()
initialHeight = tk.Entry(root)
initialHeight.pack()
label = tk.Label(root, text="Initial angle [°]")
label.pack()
initialAngle = tk.Entry(root)
initialAngle.pack()
label = tk.Label(root, text="Acceleration due to gravity [m/s^2]")
label.pack()
gravity = tk.Entry(root)
gravity.pack()
button = tk.Button(root, text="Create graph", command=create_graph)
button.pack()

max_height_label = tk.Label(root, text="")
max_height_label.pack()
total_time_label = tk.Label(root, text="")
total_time_label.pack()
throw_length_label = tk.Label(root, text="")
throw_length_label.pack()
fig, ax = plt.subplots()
line, = ax.plot(0, 0)
ax.set_xlabel("Throw length [m]")  # Set x axis title
ax.set_ylabel("Throw height [m]")

# Create a canvas
canvas = FigureCanvasTkAgg(fig, master=root)

canvas_widget = canvas.get_tk_widget()

# Pack the canvas into the main window
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Enter the Tkinter event loop
root.mainloop()
throw_graph.py