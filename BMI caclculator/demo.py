import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("300x250")

        # Create input fields
        self.weight_label = tk.Label(root, text="Weight (kg):")
        self.weight_label.pack()
        self.weight_entry = tk.Entry(root)
        self.weight_entry.pack()

        self.height_label = tk.Label(root, text="Height (m):")
        self.height_label.pack()
        self.height_entry = tk.Entry(root)
        self.height_entry.pack()

        # Create calculate button
        self.calculate_button = tk.Button(root, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.pack()

        # Create result label
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        # Create graph button
        self.graph_button = tk.Button(root, text="View Historical Data", command=self.view_historical_data)
        self.graph_button.pack()

        # Create data storage
        self.data_storage = {}

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())

            if weight <= 0 or height <= 0:
                raise ValueError("Invalid input")

            bmi = weight / (height ** 2)
            category = self.get_category(bmi)

            self.result_label.config(text=f"BMI: {bmi:.2f} ({category})")

            # Store data
            username = "default"  # Replace with actual username
            if username not in self.data_storage:
                self.data_storage[username] = []
            self.data_storage[username].append((weight, height, bmi))

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def get_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def view_historical_data(self):
        username = "default"  # Replace with actual username
        if username not in self.data_storage:
            messagebox.showinfo("No data", "No historical data available")
            return

        data = self.data_storage[username]
        weights, heights, bmis = zip(*data)

        plt.plot(bmis)
        plt.xlabel("Measurement")
        plt.ylabel("BMI")
        plt.title("BMI Trend")
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()