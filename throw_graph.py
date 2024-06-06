#To run this program run this in cmd
'''
python -m venv venv
.\venv\Scripts\activate
pip install matplotlib
python throw_graph.py
'''
'''
todo:
create a graph that shows velocity on x and y axis
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
    t_max = np.abs(2* ((initial_speed_value * np.sin(initial_angle_value))/ g))

    # Time array
    t = np.linspace(0, t_max, 100)
    # Calculate horizontal and vertical positions
    x = initial_speed_value * np.cos(initial_angle_value) * t
    y = initial_height_value + initial_speed_value * t - 0.5 * g * t ** 2

# Compute the gradient (dy/dx) using numpy.gradient
    dy_dx = np.gradient(y, x)
# Choose a point to get the gradient (let's say at x = 5)
    x_point = 5
# Find the index of the x value closest to 5
    index = np.argmin(np.abs(x - x_point))

# Get the gradient at the chosen point
    gradient_at_point = dy_dx[index]

    vy0 = initial_speed_value * np.sin(theta_radians)
    t_mid = np.linspace(0, np.abs(((initial_speed_value * np.sin(initial_angle_value))/ g)), 100)
    y_velocity = np.abs(initial_speed_value - g * t)
    # y_velocity = np.arctan(dy_dx) * initial_speed_value
    # Adjust y to start from initial_height
    y = np.maximum(y, 0)
    # Set x and y limits
    ax.set_xlim(left=min(x), right=max(x) + 5)
    ax.set_ylim(bottom=min(y), top=max(y) + 10)
    ax_y_speed.set_xlim(left=0, right=t_max)
    ax_y_speed.set_ylim(bottom=-1, top=max(y_velocity))

    # Update x and y data
    line.set_xdata(x)
    line.set_ydata(y)
    line_speed_y_graph.set_xdata(t)
    line_speed_y_graph.set_ydata(np.abs(y_velocity))
    # Set x and y tick intervals and formats
    if(np.max(x) < 1):
        ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
    else:
        ax.xaxis.set_major_locator(ticker.MultipleLocator(np.max(x.__abs__()) * 0.15))
    if (np.max(y) < 1):
        ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
    else:
        ax.yaxis.set_major_locator(ticker.MultipleLocator(np.max(y.__abs__()) * 0.15))

    ax_y_speed.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax_y_speed.yaxis.set_major_locator(ticker.MultipleLocator(1))

    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.0f}"))
    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.0f}"))
    ax_y_speed.xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.0f}"))
    ax_y_speed.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.0f}"))
    # Recalculate limits and autoscale
    ax.relim()
    ax.autoscale_view()
    ax_y_speed.relim()
    ax_y_speed.autoscale_view()
    # Redraw the canvas
    canvas.draw()
    canvas_y_speed.draw()
    
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
y_speed_graph_fig, ax_y_speed = plt.subplots()

line_speed_y_graph, = ax_y_speed.plot(0, 0)

line, = ax.plot(0, 0)
ax.set_xlabel("Throw length [m]")  # Set x axis title
ax.set_ylabel("Throw height [m]")
ax_y_speed.set_xlabel("time [t]")
ax_y_speed.set_ylabel("speed on y axis [Vy]")
# Create a canvas
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()

canvas_y_speed = FigureCanvasTkAgg(y_speed_graph_fig, master=root)
canvas_widget_y_speed = canvas_y_speed.get_tk_widget()

# Pack the canvas into the main window
canvas_widget.pack(side=tk.LEFT, fill=tk.X, expand=True)
canvas_widget_y_speed.pack(side=tk.RIGHT, fill=tk.Y, expand=True)
# Enter the Tkinter event loop
root.mainloop()
