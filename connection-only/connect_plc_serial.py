import pymodbus.client as modbus_client

# PLC connection details (replace with your values)
serial_port = "COM1"  # Replace with the correct serial port
baudrate = 9600
bytesize = 8
parity = 'N'
stopbits = 1
timeout = 0.5
unit_id = 1  # Replace with the PLC's unit ID
register_address = 100

# Create a Modbus serial client
client = modbus_client.ModbusSerialClient(
    serial_port, baudrate=baudrate, bytesize=bytesize, parity=parity, stopbits=stopbits, timeout=timeout
)

try:
    # Connect to the PLC
    client.connect()
    if client.connected: print("Connected to PLC!!!")

    # Read a register value
    result = client.read_holding_registers(register_address, 1, unit=unit_id)
    register_value = result.registers[0]
    print("Register value:", register_value)

except Exception as e:
    print("Connection error:", e)
finally:
    # Close the connection
    client.close()
    print("Connection closed.")
