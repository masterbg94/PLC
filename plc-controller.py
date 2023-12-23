import tkinter as tk

# Define empty list to store user inputs
user_data = []

def add_values():
  """
  This function retrieves user input and adds it to the list.
  """
  # Get values from entry fields
  width = float(entry_width.get())
  height = float(entry_height.get())
  quantity = int(entry_quantity.get())

  # Add values to list
  user_data.append((width, height, quantity))

  # Update listbox with new data
  listbox.insert(tk.END, f"{width}, {height}, {quantity}")

  # Clear entry fields for next inputs
  entry_width.delete(0, tk.END)
  entry_height.delete(0, tk.END)
  entry_quantity.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Data Input")

# Create labels and entry fields
label_width = tk.Label(root, text="Visina:")
label_width.pack()
entry_width = tk.Entry(root, width=10)
entry_width.pack()

label_height = tk.Label(root, text="Sirina:")
label_height.pack()
entry_height = tk.Entry(root, width=10)
entry_height.pack()

label_quantity = tk.Label(root, text="Kolicina:")
label_quantity.pack()
entry_quantity = tk.Entry(root, width=10)
entry_quantity.pack()

# Create add button
button_add = tk.Button(root, text="Dodaj", command=add_values)
button_add.pack()

# Create listbox to display added data
listbox = tk.Listbox(root, width=40)
listbox.pack()

# Start the main loop
root.mainloop()
