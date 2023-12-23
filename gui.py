import tkinter as tk

# Create the main window
# Set the desired width
WIDTH = 600  # Adjust as needed

# Create the main window with the specified width
root = tk.Tk()
root.title("Visina, Sirina, Kolicina")
root.geometry(f"{WIDTH}x300")  # Adjust height if needed

# Create input fields
visina_entry = tk.Entry(root)
visina_label = tk.Label(root, text="Visina:")
visina_label.pack()
visina_entry.pack()

sirina_entry = tk.Entry(root)
sirina_label = tk.Label(root, text="Sirina:")
sirina_label.pack()
sirina_entry.pack()

kolicina_entry = tk.Entry(root)
kolicina_label = tk.Label(root, text="Kolicina:")
kolicina_label.pack()
kolicina_entry.pack()

# Define a function for adding entries to the listbox
def dodaj():
    visina = visina_entry.get()
    sirina = sirina_entry.get()
    kolicina = kolicina_entry.get()
    listbox.insert(tk.END, f"Visina: {visina}, Sirina: {sirina}, Kolicina: {kolicina}")
    visina_entry.delete(0, tk.END)  # Clear the input fields
    sirina_entry.delete(0, tk.END)
    kolicina_entry.delete(0, tk.END)

# Create the "Dodaj" button
dodaj_button = tk.Button(root, text="Dodaj", command=dodaj)
dodaj_button.pack()

def obrisiListu():
    listbox.delete(first=0,last=0)

obrisiListu_button = tk.Button(root, text="Obrisi listu", command=obrisiListu)
obrisiListu_button.pack()

# Create a listbox to display the entries
listbox = tk.Listbox(root)
# When packing the listbox, use fill=tk.X to expand it horizontally
listbox.pack(fill=tk.X)


# Start the main loop
root.mainloop()
