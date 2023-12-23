# gui.py
import tkinter as tk
from tkinter import messagebox
from plc_connection import PLCConnection

class PLCGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PLC Connection GUI")
        self.root.geometry('200x150')

        self.plc_connection = PLCConnection(port='/dev/ttyUSB0', baudrate=9600)  # Change the port accordingly

        self.start_button = tk.Button(root, text="Connect to PLC", command=self.start_button_click)
        self.start_button.pack(pady=20)

    def start_button_click(self):
        success = self.plc_connection.connect()

        if success:
            messagebox.showinfo("Connection Status", "Connected to PLC successfully!")
            # You can add additional functionality here for data exchange or other actions
        else:
            messagebox.showerror("Connection Status", "Failed to connect to PLC.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PLCGUI(root)
    root.mainloop()
