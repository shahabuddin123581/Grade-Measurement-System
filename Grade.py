import tkinter as tk
from tkinter import messagebox

# Function to determine the grade
def calculate_grade():
    try:
        score = float(entry.get())
        
        if score < 0 or score > 100:
            messagebox.showerror("Invalid Input", "Score must be between 0 and 100.")
            return
        
        # Calculate grade
        if score >= 90:
            grade = 'A'
            result_label.config(fg='green')  # Green for A
        elif score >= 80:
            grade = 'B'
            result_label.config(fg='blue')  # Blue for B
        elif score >= 70:
            grade = 'C'
            result_label.config(fg='orange')  # Orange for C
        elif score >= 60:
            grade = 'D'
            result_label.config(fg='yellow')  # Yellow for D
        else:
            grade = 'F'
            result_label.config(fg='red')  # Red for F
        
        result_label.config(text=f"Grade: {grade}")
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Student Grade Calculator")

# Set background color
root.config(bg='#f0f8ff')

# Create a label for instructions
label = tk.Label(root, text="Enter the score (0-100):", font=("Arial", 12), bg='#f0f8ff', fg='#333')
label.pack(pady=10)

# Create an entry widget for the score input
entry = tk.Entry(root, font=("Arial", 14), bg='#e0ffff', bd=2, relief="solid")
entry.pack(pady=10)

# Create a button to calculate the grade
calculate_button = tk.Button(root, text="Calculate Grade", command=calculate_grade, font=("Arial", 12), bg='#add8e6', fg='white', relief="raised")
calculate_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="Grade: ", font=("Arial", 14), bg='#f0f8ff', fg='black')
result_label.pack(pady=20)

# Run the application
root.mainloop()
