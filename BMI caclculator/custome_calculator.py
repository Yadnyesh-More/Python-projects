from customtkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("500x450")
        self.root.resizable(False,False)

        # Create input fields
        self.weight_label = CTkLabel(root, text="Weight (kg):",font=("arieal",20,"bold"))
        self.weight_label.place(x=200,y=50)
        self.weight_entry = CTkEntry(root,placeholder_text="Enter Your Weight ",width=230,height=30)
        self.weight_entry.place(x=139,y=90)

        self.height_label = CTkLabel(root, text="Height (m):",font=("arieal",20,"bold"))
        self.height_label.place(x=200,y=150)
        self.height_entry = CTkEntry(root,placeholder_text="Enter Your Height ",width=230,height=30)
        self.height_entry.place(x=139,y=190)

        # Create calculate button
        self.calculate_button = CTkButton(root, text="Calculate BMI", command=self.calculate_bmi,fg_color="red",hover_color="green",width=180,height=35)
        self.calculate_button.place(x=165,y=260)

        # Create result label
        self.result_label = CTkLabel(root, text="",font=("arieal",20,"bold","underline"))
        self.result_label.place(x=130,y=315)

        # Create graph button
        self.graph_button = CTkButton(root, text="View Historical Data", command=self.view_historical_data,fg_color="red",hover_color="green",width=180,height=35)
        self.graph_button.place(x=170,y=370)

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

            self.result_label.configure(text=f"BMI: {bmi:.2f} ({category})")

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
    root = CTk()
    
    app = BMICalculator(root)
    root.mainloop()