import math
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Function to calculate pi based on the number of sides and diameter
def calculate_pi(n, diameter):
    r = diameter / 2
    circumference = 0
    points = []  # To store the points of the polygon
    for i in range(n):
        x1 = r * math.cos(2 * math.pi * i / n)
        y1 = r * math.sin(2 * math.pi * i / n)
        points.append((x1, y1))  # Save the points for plotting
        x2 = r * math.cos(2 * math.pi * (i + 1) / n)
        y2 = r * math.sin(2 * math.pi * (i + 1) / n)
        side_length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        circumference += side_length
    pi = circumference / diameter
    return pi, points

# Function to plot the circle and polygon
def plot_polygon_and_circle(n, diameter, points, pi_value):
    fig, ax = plt.subplots(figsize=(7, 6))  # Fixed window size

    # Plot the circle
    circle = plt.Circle((0, 0), diameter / 2, color='blue', fill=False, label='Circle')
    ax.add_artist(circle)

    # Plot the polygon
    polygon_points = points + [points[0]]  # Close the polygon
    polygon_x, polygon_y = zip(*polygon_points)
    ax.plot(polygon_x, polygon_y, color='red', label=f'{n}-gon')

    ax.set_aspect('equal')
    ax.set_xlim(-diameter / 2 - 0.1, diameter / 2 + 0.1)
    ax.set_ylim(-diameter / 2 - 0.1, diameter / 2 + 0.3)

    # Labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f'{n}-gon Inscribed in a Circle (Diameter = {diameter})')

    # Legend
    ax.legend()

    # Pi value
    ax.text(-diameter / 2 - 0.05, -diameter / 2 - 0.2, f'π ≈ {pi_value:.6f}',
            horizontalalignment='left', verticalalignment='center', fontsize=12, color='green')

    plt.show()

# Function to handle the 'Calculate' button press
def on_calculate():
    try:
        diameter = float(diameter_entry.get())
        sides = int(sides_entry.get())
        if sides < 3:
            messagebox.showerror("Error", "Number of sides must be 3 or more.")
            return
        pi_value, points = calculate_pi(sides, diameter)
        result_label.config(text=f"Calculated pi: {pi_value:.6f}")
        plot_polygon_and_circle(sides, diameter, points, pi_value)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create main window with ttkbootstrap
root = ttk.Window(themename="darkly")  # Choose a theme like 'darkly', 'flatly', etc.
root.title("Modern Pi Calculator")

# Styling the window layout
style = ttk.Style()
style.configure('TButton', font=('Arial', 12))
style.configure('TLabel', font=('Arial', 12))

# Diameter input
ttk.Label(root, text="Diameter of the Circle:", bootstyle="info").grid(row=0, column=0, padx=10, pady=10)
diameter_entry = ttk.Entry(root, font=("Arial", 12))
diameter_entry.grid(row=0, column=1, padx=10, pady=10)
diameter_entry.insert(0, "1")  # Default value

# Number of sides input
ttk.Label(root, text="Number of Sides:", bootstyle="info").grid(row=1, column=0, padx=10, pady=10)
sides_entry = ttk.Entry(root, font=("Arial", 12))
sides_entry.grid(row=1, column=1, padx=10, pady=10)
sides_entry.insert(0, "3")  # Default value

# Calculate button
calculate_button = ttk.Button(root, text="Calculate", command=on_calculate, bootstyle=SUCCESS)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result label
result_label = ttk.Label(root, text="Calculated pi: ", bootstyle="success")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Start the application
root.mainloop()
