import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Memorization Competition Judge Panel")
root.geometry("400x300")

# Add a label
label = tk.Label(root, text="Welcome to the Judge Panel!")
label.pack(pady=20)

# Run the application
root.mainloop()