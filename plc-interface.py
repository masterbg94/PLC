import tkinter as tk
from tkinter import ttk
from pymodbus.client import ModbusSerialClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder, BinaryPayloadBuilder

class PLCInterface:
    def __init__(self, master):
        self.master = master
        master.title("PLC Interfejs")

        # Parametri za serijski port
        self.serial_port = '/dev/ttyUSB0'  # Prilagodite putanju serijskog porta prema vašem sistemu
        self.baudrate = 9600
        self.parity = 'N'
        self.stopbits = 1
        self.bytesize = 8

        # Adresa PLC uređaja
        self.plc_address = 1  # Adresa PLC uređaja

        # Adresa registra koji želite čitati/promeniti
        self.register_address = 1000

        # GUI elementi
        self.label_height = ttk.Label(master, text="Visina:")
        self.label_width = ttk.Label(master, text="Širina:")
        self.label_quantity = ttk.Label(master, text="Količina:")

        self.entry_height = ttk.Entry(master)
        self.entry_width = ttk.Entry(master)
        self.entry_quantity = ttk.Entry(master)

        self.button_add_data = ttk.Button(master, text="Dodaj u tabelu", command=self.add_to_table)

        self.tree = ttk.Treeview(master, columns=("Visina", "Širina", "Količina"))
        self.tree.heading("#0", text="Redni broj")
        self.tree.heading("Visina", text="Visina")
        self.tree.heading("Širina", text="Širina")
        self.tree.heading("Količina", text="Količina")

        # Postavi raspored elemenata u GUI
        self.label_height.grid(row=0, column=0, padx=10, pady=5)
        self.entry_height.grid(row=0, column=1, padx=10, pady=5)
        self.label_width.grid(row=1, column=0, padx=10, pady=5)
        self.entry_width.grid(row=1, column=1, padx=10, pady=5)
        self.label_quantity.grid(row=2, column=0, padx=10, pady=5)
        self.entry_quantity.grid(row=2, column=1, padx=10, pady=5)
        self.button_add_data.grid(row=3, column=0, columnspan=2, pady=10)
        self.tree.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    def add_to_table(self):
        # Čitanje unetih podataka
        height = float(self.entry_height.get())
        width = float(self.entry_width.get())
        quantity = int(self.entry_quantity.get())

        # Dodaj podatke u tabelu
        index = len(self.tree.get_children())
        self.tree.insert("", index, values=(height, width, quantity))

        # Poveži se sa PLC-om i promeni vrednost u registru (prilagodite ovoj sekciji prema vašim potrebama)
        with ModbusSerialClient(
                method='rtu',
                port=self.serial_port,
                baudrate=self.baudrate,
                parity=self.parity,
                stopbits=self.stopbits,
                bytesize=self.bytesize,
                timeout=1
        ) as client:
            if client.connect():
                builder = BinaryPayloadBuilder(byteorder=Endian.Big)
                builder.add_32bit_float(height)
                builder.add_32bit_float(width)
                builder.add_32bit_float(quantity)
                payload = builder.to_registers()

                write_response = client.write_registers(self.register_address, payload, unit=self.plc_address)
                if write_response.isError():
                    print("Greška prilikom pisanja u registar:", write_response)
                else:
                    print(f"Podaci su uspešno poslati u PLC registar {self.register_address}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PLCInterface(root)
    root.mainloop()
