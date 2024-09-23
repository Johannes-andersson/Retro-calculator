# Curved Display Calculator

Curved Display Calculator is a Python-based application that combines a visually engaging user interface with advanced plotting capabilities. It features a retro, Matrix-style welcome screen and allows users to perform 2D, 3D, and diagram plotting of mathematical expressions using Python's powerful libraries.

## Features

- **Retro Curved Display:** A visually appealing interface with a green, wave-style welcome message on a black background, reminiscent of old terminal screens.
- **2D Plotting:** Generate 2D plots of mathematical expressions.
- **3D Plotting:** Create 3D surface plots using advanced mathematical functions.
- **Diagram Plotting:** Display bar charts based on user input for data visualization.
- **Interactive Input:** Users can enter their own math expressions and visualize the results instantly.

## Technologies Used

- **Python 3.8+**
- **PyQt5** - For the graphical user interface.
- **OpenGL** - For rendering the retro display effect.
- **Matplotlib** - For 2D and 3D plotting.
- **NumPy** - For handling mathematical computations and array operations.

## Installation

To run this project, you'll need Python 3.8 or higher installed on your machine along with the required libraries. Follow the steps below to get started:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/curved-display-calculator.git
   cd curved-display-calculator
Install Dependencies

Make sure you have the required Python libraries installed. You can install them using pip:

bash
Copy code
pip install PyQt5 OpenGL matplotlib numpy
Usage
Run the Application

Start the application by executing the following command in your terminal:

bash
Copy code
python calculator.py
Using the Calculator

Upon launching, you’ll be greeted with a retro-style welcome message.
Enter your desired mathematical expression in the input field at the bottom.
Choose the type of plot you want to generate: 2D Plot, 3D Plot, or Diagram.
Click the Plot Graph button to visualize the expression.
Examples of Valid Math Expressions
2D Plot: np.sin(x) - Plots a simple sine wave.
3D Plot: np.sin(np.sqrt(X**2 + Y**2)) - Creates a 3D surface with a ripple effect.
Diagram: [10, 20, 15, 5] - Displays a bar chart with the given values.
Screenshots
Wave-style welcome message with green text.

A 2D plot generated from a sine function.

A 3D surface plot with a ripple effect.

A simple bar chart generated from a list of values.

Troubleshooting
Missing Imports: If you encounter errors regarding missing functions or modules, ensure all dependencies are correctly installed.
Display Issues: If the graphics do not render correctly, make sure your system's OpenGL drivers are up-to-date.
Contributing
Contributions are welcome! If you have ideas for improvements or find any bugs, please open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
If you have any questions or need further assistance, feel free to reach out:

Email: johannes.ai@proton.me
GitHub: Johannes-andersson