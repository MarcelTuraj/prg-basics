import matplotlib.pyplot as plt

x = [n for n in range(-10, 11)]  # List comprehension for better performance

# Create y values based on the function y = x^2 - 3
y = [n**2 - 3 for n in x]  # Calculate y = x^2 - 3

# Print chart
plt.plot(x, y, label='y = x^2 - 3')  # Create the plot with a label
plt.title("Plot of y = x^2 - 3")  # Add a title
plt.xlabel("x values")  # Label for x-axis
plt.ylabel("y values")  # Label for y-axis
plt.axhline(0, color='black', linewidth=0.5, ls='--')  # Add horizontal line at y=0
plt.axvline(0, color='black', linewidth=0.5, ls='--')  # Add vertical line at x=0
plt.grid()  # Add a grid for better readability
plt.legend()  # Show the legend
plt.show()  # Display the plot