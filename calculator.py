from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel, QComboBox
from PyQt5.QtOpenGL import QGLWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer
# Explicitly import the necessary OpenGL functions and constants
from OpenGL.GL import glClearColor, glEnable, glViewport, glMatrixMode, glLoadIdentity, glClear, glColor3f, glBegin, glEnd, glVertex3f
from OpenGL.GL import GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_PROJECTION, GL_MODELVIEW, GL_QUADS, GL_DEPTH_TEST
from OpenGL.GLU import gluOrtho2D
import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math


class CurvedScreen(QGLWidget):
    def __init__(self, parent=None):
        super(CurvedScreen, self).__init__(parent)
        self.setMinimumSize(800, 600)
        self.text = "Welcome, what's your math problem?"
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(100)  # Update interval for wave effect (adjust to control speed)
        self.phase = 0  # Phase for wave animation

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
        glEnable(GL_DEPTH_TEST)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, w, 0, h)  # 2D orthographic projection
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        self.drawWelcomeText()

    def drawWelcomeText(self):
        # Display a wave-style welcome message
        glColor3f(0.0, 1.0, 0.0)  # Green color for the text
        x_start = self.width() // 2 - 150  # Starting x position for the text
        y_start = self.height() // 2  # Vertical center
        for i, char in enumerate(self.text):
            # Create a wave effect by adjusting the y position of each character
            y_offset = int(10 * math.sin(self.phase + i * 0.3))
            self.renderText(x_start + i * 10, y_start + y_offset, char, font=QFont("Courier", 12))
        self.phase += 0.1  # Increment phase to animate the wave effect


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Curved Display Calculator')
        self.setGeometry(100, 100, 1024, 768)

        # Set up the main widget and layout
        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)

        # Add the curved screen OpenGL widget
        self.curved_screen = CurvedScreen(self.central_widget)
        self.layout.addWidget(self.curved_screen)

        # Input field for math expressions
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Enter a math expression, e.g., np.sin(x) or np.sin(X**2 + Y**2)")
        self.layout.addWidget(self.input_field)

        # Dropdown to select plot type
        self.plot_type = QComboBox(self)
        self.plot_type.addItems(["2D Plot", "3D Plot", "Diagram"])
        self.layout.addWidget(self.plot_type)

        # Calculate button
        self.calculate_button = QPushButton('Plot Graph', self)
        self.calculate_button.clicked.connect(self.plotGraph)
        self.layout.addWidget(self.calculate_button)

        # Output label
        self.output_label = QLabel("Output will be shown here", self)
        self.layout.addWidget(self.output_label)

        self.setCentralWidget(self.central_widget)

    def plotGraph(self):
        # Get the input expression and plot type from the input field
        expression = self.input_field.text()
        graph_type = self.plot_type.currentText()

        try:
            if graph_type == "2D Plot":
                self.plot2D(expression)
            elif graph_type == "3D Plot":
                self.plot3D(expression)
            elif graph_type == "Diagram":
                self.plotDiagram(expression)
        except Exception as e:
            self.output_label.setText(f"Error: {e}")

    def plot2D(self, expression):
        x = np.linspace(-10, 10, 400)
        y = eval(expression)  # Evaluate the expression for y based on x
        plt.plot(x, y)
        plt.title(f"2D Plot of {expression}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.show()

    def plot3D(self, expression):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x, y)
        Z = eval(expression)  # Evaluate the expression for z based on X, Y
        ax.plot_surface(X, Y, Z, cmap='viridis')
        plt.title(f"3D Plot of {expression}")
        plt.show()

    def plotDiagram(self, expression):
        categories = ['A', 'B', 'C', 'D']
        values = eval(expression)  # Expected to be a list of values
        plt.bar(categories, values)
        plt.title(f"Bar Chart of {expression}")
        plt.xlabel("Categories")
        plt.ylabel("Values")
        plt.show()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()










